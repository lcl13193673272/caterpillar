import random

# i = [1, 2, 3]
# for i in range(1, 10):
#  print(i)
#
# x = range(10)
# print(x)
# print(type(x))

# # float数据类型
# x = 27e4
# y = 15E2
# z = -49.8e100
# print(type(x))
# print(x)
# print(type(y))
# print(y)
# print(type(z))
# print(z)
#
# # 复数数据类型
# x = 2+3j
# y = 7j
# z = -7j
# print(type(x))
# print(x)
# print(type(y))
# print(y)
# print(type(z))
# print(z)

#不同数据类型之间可以相互转换，但是复数不可以转换为其他数据类型

#生成随机数
# print(random.randrange(198,199))#该区间左闭右开

# thislist = ["apple", "strawberry", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)
# thatlist = ["apple", "strawberry", "peach"]

# for x in range(3, 50, 6):
#   print(x)

# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)


# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(30))

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# 使用 Person 来创建对象，然后执行 printname 方法：

# x = Person("Bill", "Gates")
# x.printname()
# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
# y=Student("fan","li",25)
# y.welcome()

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))

# import platform
# x = dir(platform)
# print(x)

# import datetime
# x = datetime.datetime.now()
# print(x)

# import re
# str = "China is a great country"
# x = re.search("a", str)
# print(x) #this will print an object
# print(x.start())
# print(x.group())

import camelcase


c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))