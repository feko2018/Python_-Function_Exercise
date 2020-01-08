# -*- encoding:utf-8 -*-


# 10、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码


# 读取账号密码文件，存储在字典 形式：{'feko': ['112233'], 'feko1': ['112233'], 'feko2': ['112233']}
f = open('passwd.txt', 'r', encoding='utf-8')
account = []
account_dict = {}
for line in f:
    account = line.strip().split('::')
    account_dict.update({account[0]: [account[1]]})
f.close()


# 登陆验证模块，判断用户名，是否登陆，登陆密码是否存在
auth = {"is_authenticated": False}


def login(func):
    def inner():
        if not auth["is_authenticated"]:   #  判断是否登陆过
            username = input("user:")
            password = input("password:")
            for i in account_dict:     #  循环字典中的用户密码信息
                if account_dict.get(username):     #  判用户是否存在
                    if  password == account_dict[username][0]:
                        auth["is_authenticated"] = True
                        print("登陆成功")
                        func()   #  传的参数为music,相当于调用music() 函数
                        break
                    else:
                        print("密码错误")
                        break
                else:
                    print("用户不存在")
                    break
        else:
            print("已登陆")
            func()   #  传的参数为music,相当于调用music() 函数
    return inner

@login   #  装饰器，语法糖
def music():
    print("欢迎登陆到音乐专区")

@login  #  装饰器
def video():
    print("欢迎登陆到影视专区")


# music = login(music)   #  即是inner = login  顺便传个函数参数 == @login
# video = login(video)   #  即是inner = login  顺便传个函数参数
# music()    #  返回inner内存地址,
# video()    #  返回inner内存地址,

music()
video()