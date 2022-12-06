import logging
import random
import re
from urllib import parse

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradeCreateModel import AlipayTradeCreateModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.util.SignatureUtils import verify_with_rsa

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a', )
logger = logging.getLogger('')

app_private_key = "MIIEowIBAAKCAQEAiWcbVJ6BfbzvLo8DuPoYq62NSSaMowhDTuJIk9F8gEFKnb5XEWCQrsPu4jq0VGCDeaLpjnWHFX51TJHQ0+myUBOFxMfz5M0kDSX46/qEw+yXtFF5AWpYI4NhtMYyMRhjllzU8jOmtiXDEX+emkLsNoNBQmhtWb5Fj3ZU7ijajgFq2rcnoshEZbdJq/x759kTOOTLWgRLeABPgGMfzC23fHygRoDWMqoX2iu2yTsKK5A90bCfHvjNAknO3WbzgeUcCbq7kwbGxdgmlxAy8ORiMsN2VynwFAENc65ynCW/iLOgTUGpcZntekpvKdjXT28M6T+EoKfZb3TzCCmP43ysXQIDAQABAoIBAD1hlz8FFDn0ljEJaJNQ/oZrIIvGMdt/DHqH8f4+/kxZXpj7d+/mYJwCIYxkxzxOZU2Ibqfabv82H/aVyWFxq9vD7OVMofLbhbht9zaMEpVn8xl1sAXm2Pr8bUCRrchq6co5LFQKqPYEBpGhnluxe86aciPVfMwziOWe6i/+hiwbXEkKo5CNE29/JQ3iI0SnsGNPlDrcjbiUsTmEbxfCQv552jkHmodOYcR9GgAC7zGGoCwAW+UV/SA4XxbeYjn1fLfQRcozndb2f+Ac13cuTZs3z3HvyvZtCNz+ffC94IXXwhCiaT64KwfEApeS5Lrsqbk+ZELUxWEdQz5EvixJAuECgYEA/8+NxPB7RfPo7XtphDt30NNHdodOEj61edA5tm53H1SzBqM4LLSDQJslsQk+cGUOVFFIoDryfhCp80mcCAKYyNbooDIMeBCheNeMzvvxlYHB4NquH+tQLWq4O/8sDKKuBd+u3eLiuiQhrWLLb9sHFowoPCXHoRjPagkgAAfhE6UCgYEAiYEg5gNg/eFC+ZLs+AQk/HQB8c9oj/j1aCq4uLMEay/eTMvHdHO6xbKusy//r4AaEfsrE6C0gXuTQTvU+8aVD5qxClUeBJITtC/nN2WZqhho7JsIiEEsoJr1VKxZW0kSe+qiuBnNyeR38Kh6lq7ZFmBgsaJYpnZUWiQRjxRR+FkCgYB8suWN6hh9ih+ynGVcU0zd3BBLBDwXgsAeKFXpy0GAYV5/ztLUYA5XUQn3meT5DxoEGjeH/BQ3RdJCyVApS3LE/JYbeSpA4QKFkLWQNJqYYc9r183nu2KzMQGsJYCIjEi+jkKE4VPan0BXcABxf1ieMiZu44/DxP9e1iHmQfEDDQKBgF56cQZZ7/zBGGmvQE8xWdB0TRm+7xNtdgE6yW1u42xamZ2ers8e7YgFO/A23LHTjRYpw/FajGwjYoyB9deBHM559Ycp8NQnIo6+E1qG3sx2tTFNXNFyJp27mzGwsjz8ukyWbXOdlz5PUvHycTizrsmnMwkaiVrnFxJQkhgDWEcRAoGBALzWrQ+bPAGA7XYRTOI9+7ep4d7yrrH24mctIiabmO4sxuAOely8LwRw6ryFvrTTq4dAEaomdoXJv56pRWGiY7cC8Eds/+/YtObNn756Ew5jQcyTY4TH7WVNEDjbCz4k+jBStgQMcRojMwcix2tXOwkDycQvkuBpvWTMjNEyb1sr"
alipay_public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvQK9D45PsrXL+noa/1czyjWAHnn0KN5l3b/W7sHwhWZBTK02BPYK7uxWkXM70/qJu0CXpW82G1NZUpl8kLx9d/uYzZ9RIb7zWLiuUre3RwK0hNbNDzBTOQw0yrBwW5KnA5G3aE4N71+b+Zp6mF78MKGsr83Fr1BKyRTorOKik1sh1lP3vTUvwdSmT9xZe93z+rnWB7VjKJiq3tSzdU/mHDCs3HuN4CuYqiz2MjspO3vc2vb8RT0N543qS8s9Oz0yFD73i7UKu0sramnc1XnrcCq7Tcr2UvS5K0akXyboxUP4RDlvTJ4ZCxmxX3kPwco7HW7fD3+JBhKOCoc1rmMEXQIDAQAB"


def ali_Pay(id,amount):
    # 实例化客户端
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
    alipay_client_config.app_id = '2021000121692140'
    alipay_client_config.app_private_key = app_private_key
    alipay_client_config.alipay_public_key = alipay_public_key
    client = DefaultAlipayClient(alipay_client_config, logger)
    # 构造支付模型
    model = AlipayTradeCreateModel()
    model.out_trade_no = str(random.randrange(100000, 999999))
    model.total_amount = str(amount)
    model.subject = "充值"
    model.timeout_express = '30m'
    model.product_code = 'FAST_INSTANT_TRADE_PAY'
    model.buyer_id= str(id)
    request = AlipayTradePagePayRequest(biz_model=model)
    request.return_url = "http://119.91.27.246:9999"
    request.notify_url = "http://119.91.27.246:9999"  # 设置回调通知地址
    response = client.page_execute(request, http_method='GET')  # 获取支付链接
    return response


def pay_result(res_message):  # 定义处理回调通知的函数
    total_amount = float(re.findall(r"buyer_pay_amount=(.+?)&", res_message)[0])
    buyer_id=str(re.findall(r"buyer_id=(.+?)&", res_message)[0])
    print('支付成功！')
    return (buyer_id,total_amount)