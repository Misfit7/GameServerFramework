class Menu():
    def __init__(self):
        self.mainMenu=mainMenu
        self.funcMenu=funcMenu

mainMenu="----------------------------\n" \
         "1、登陆\n" \
         "2、注册\n" \
         "----------------------------\n"

funcMenu="----------------------------\n" \
         "1、私聊\n" \
         "2、广播\n" \
         "3、在线礼包\n" \
         "4、攻击\n" \
         "5、退出\n" \
         "----------------------------\n"

if __name__ == '__main__':
    m=Menu()
    print(m.mainMenu)
    print(m.funcMenu)