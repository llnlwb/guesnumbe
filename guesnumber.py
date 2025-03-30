import random
num=random.randint(1,1000)
while True:
    gues=int(input("请输入你的猜测："))
    if gues>num:
        print("猜大了")
    elif gues<num:
        print("猜小了")
    elif gues==num:
        print("猜对了")
        break
    else:
        print("输入错误")