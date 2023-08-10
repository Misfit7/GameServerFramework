# GameServerFramework
通过服务器框架的设计实现对客户端的发送数据进行处理及反馈，用户的所有数据保存在数据库中，主要使用的技术为TCP/UDP通信和多线程以及其他Python包，实现的功能如下：  
（1）登陆、注册、退出、充值(TCP)：登陆时验证账号密码对错、账号是否重复登陆；注册时验证账号名重复、密码格式是否正确；账号退出时保存数据；充值时提供支付链接、支付成功时更新账号数据。  
（2）间隔保存、暂离踢出(线程计时器)：每隔X分钟自动保存一次玩家数据；每隔X分钟检测一次未操作的玩家将其踢出并保存。  
（3）系统广播、在线礼包(任务计时器)：每隔X分钟自动向所有在线玩家发送一条系统信息；到设定时间时向所有在线玩家发送奖励并更新账号数据。  
（4）私聊、广播：玩家向另一位指定玩家发送信息；玩家向所有在线玩家群体发送一条信息。  
（5）攻击、恢复、状态、移动、加点(UDP)：玩家可以对另一位指定玩家攻击扣除血量；玩家可以为任意指定玩家恢复血量；玩家可以查看个人信息；玩家可以移动并显示坐标；玩家可以用升级点数增加属性。  
（6）管理员后台管理：在服务器后台可以显示所有玩家，指定玩家修改其数据。  