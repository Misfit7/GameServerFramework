mainMenu = "----------------------------\n" \
           "1、登陆\n" \
           "2、注册\n" \
           "3、退出游戏\n" \
           "----------------------------"

funcMenu = "----------------------------\n" \
           "1、广播\n" \
           "2、私聊\n" \
           "3、在线礼包\n" \
           "4、攻击\n" \
           "5、退出账号\n" \
           "----------------------------"


class Menu():
    def __init__(self):
        self.mainMenu = mainMenu
        self.funcMenu = funcMenu


if __name__ == '__main__':
    m = Menu()
    print(m.mainMenu)
    print(m.funcMenu)
