# encoding: UTF-8
# 求100之内的质数
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')
else:
    print("循环结束")

# 打印九九乘法表
print("打印\n九九乘法表")
for i in range(1, 10):
    for j in range(1, i+1):
        # print(i, "*", j, "=", i * j, end=' ')
        print("%d*%d=%d" % (i, j, i * j), end='\t')
    # else:
    #     print("")
    print(' ')
