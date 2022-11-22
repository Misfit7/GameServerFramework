from datetime import datetime
import time
from schedule import every, repeat, run_pending,run_all


# 此装饰器效果等同于 schedule.every(10).seconds.do(job)
@repeat(every(300).seconds)
def job1():
    print("今日充值活动已开启")


@repeat(every(60).seconds)
def job2():
    end = datetime.now()
    time = int((end - start).seconds/60)
    print("您已在线",time,"分钟，金币+10")


start = datetime.now()

if __name__ == '__main__':
    run_all()
    while True:
        run_pending()
        time.sleep(1)