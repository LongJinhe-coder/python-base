# encoding: UTF-8
name = "小明"
# print("我的名字叫%s,很高兴认识你" % name)
print("我的名字叫{},很高兴认识你".format(name))
studentid = 1825122033
# print("我的学号是%d" % studentid)
print("我的学号是{}".format(studentid))
price = 7.5
weight = 6
money = price * weight
# print("苹果的单价是%0.1f，购买了%d斤，总价钱是%0.1f" % (price, weight, money))
print("苹果的单价是{}，购买了{}斤，总价钱是{}".format(price, weight, money))
scale = 0.1
# print("数据比例是%0.2f%%" % (scale * 100))
print("数据比例是{}%".format(scale * 100))
