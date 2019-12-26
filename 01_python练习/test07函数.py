# encoding:UTF-8


def sey_hello():
    """打印hello python"""
    print("hello\npython")
    # sum = lambda arg1, arg2: arg1 + arg2
    # # 调用sum函数
    # print("sum=", sum(20, 20))
    return
    print("结束")


def printstar(str1, num):
    "打印字符串"
    print(str1 * num)


sey_hello()
printstar("ok", 30)

list1 = ["a", 2, "baidu", 3.5, "google"]
list2 = [1, 2, 3, 4, 5]


def printlist(list):
    print("列表等于:", end='')
    print(list)
    print("依次输出列表:", end='')
    for x in list:
        print(x, end=' ')
    print()
    print("输出列表后半部分:", end='')
    for x in range(len(list)//2, len(list)):
        print(list[x], end=' ')
    print()
    for x in range(len(list)):
        list[x] = "ok"
    # for x in list:
    #     x = "kkkk"
    list = [2*x for x in list]
    # print(x)
    print("函数中修改后列表等于:", end='')
    print(list)


printlist(list2)
print("修改后的list=", list2, end='')
print()
vec = [2, 4, 6]
vec = [3*x for x in vec]
print(vec)
print(vec[1:])
vec1 = tuple(vec)
print(vec)
print(vec1)

print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
