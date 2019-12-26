# encoding: utf-8
import random
ran = random.randint(1, 100)
print("ran=%d" % ran)
if ran > 25 and ran < 50 or ran > 75 and ran < 100:
    print("yes")
else:
    print("no")
