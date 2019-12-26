# encoding: UTF-8
# if-else循环
print("玩一个小游戏")
temp = input("输入你想到的第一个数字：")
guess = int(temp)
if guess == 6:
    print("你和我想的一样")
    print("真是心有灵犀啊")
else:
    print("我和你想的不一样，我想的数字是6")
print("游戏结束")
# 转义换行符的使用
str = "hello\npython"
print(str)
str = r"hello\npython"
print(str)
