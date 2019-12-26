# encoding: utf-8
import random
print("hello python")
print("你好 python")
name = "小明"
sex = True
height = 25
print(name)
print(sex)
print(height)

if height > 10:
    # print("height>10")
    if height > 20:
        print("height>20")
    else:
        print("10<height<20")
else:
    print("height<=10")

ran = random.randint(1, 100)
print("ran=%d" % ran)
if ran > 20 and ran < 50 or ran == 50:
    print("yes")
else:
    print("no")
# if condition:
#     if condition:
#         pass
#     elif expression:
#         pass
#     else:
#         pass
# else:
#     pass
k = 5
while k > 0:
    print(k, end=' ')
    # print(k)
    k -= 1

a = 120
b = str(a)
for k in b:
    print(k)
print(type(b))

a = "5401"
print(a.find("2"))
if a.find("2") != -1 or a.find("7") != -1:
    print("yes")
else:
    print("no")
count = 0
for x in range(5401, 98654311):
    y = str(x)
    for k in y:
        if (y.find("2") != -1) or (y.find("7") != -1) or (y.count(k) > 1):
            break
    else:
        count += 1
print(count)
print("count={}".format(count))
