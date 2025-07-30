# print("Twinkle, twinkle, little star,","\nHow I wonder what you are!","\nUp above the world so high,",
# "\nLike a diamond in the sky.","\nTwinkle, twinkle, little star,","\nHow I wonder what you are")

# a = input("please input a num:")
# print(type(a))

# a = int(input("plese inseri num1:"))
# b = int(input("plese inseri num2:"))
# print(a+b)
# print(a-b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a*b)
# print(a**b)

# a = int(input("plese inseri num1:"))
# b = input("plese inseri name:")
# print(b[a])
# print(b*a)

# a = int(input("plese inseri num1:"))
# q= int(a)
# print(type(q))
# b = float(a)
# print(type(b))

# radius = float(input("plese enter your r:"))
# from math import pi
# area = radius ** 2 * pi
# print(f"area is:{area}")

# a = input("plese inseri num1:")
# q = int(a) + int((a)*2) + int((a)*3)
# print(q)

# a = input("plese inseri firt_name:")
# b = input("plese inseri last_name:")
# c = input("plese inseri age:")
# d = input("plese inseri city:")
# print(f"you name is:{a} {b}\nyour age is {c}\nand your city is:{d}")

# lst = [1,2,3,4]
# sum = 0
# irt = 0
# for i in lst:
#     sum += i
#     irt += 1
# print(f"average is: {sum/irt}")

# lst = [12,14,32,18,25,26]
# min_num = lst[0]
# max_num = lst[0]
# for i in lst:
#     if i <= min_num:
#         min_num = i
# for j in lst:
#     if j >= max_num:
#         max_num = j
# print(f"min is : {min_num}, max is : {max_num}")

# import random
# random_int = random.randint(1,20)
# print(random_int)
# a = int(input("plese enter your guess:"))
# while a > random_int:
#     print ("too high")
#     a = int(input("plese enter your guess:"))
#     while a < random_int:
#         print ("too small")
#         a = int(input("plese enter your guess:"))

# print("your guess is true")

# a = int(input("plese enter your num:"))
# fact = 1
# for i in range(1,a+1):
#     fact *= i
# print(f"factorial is :{fact}")
    

# a = input("plese inseri firt_name:")
# b = input("plese inseri last_name:")
# x = a[:-1] + b[-1]
# y = b[:-1] + a[-1]
# print(f"{x} {y}")

# a = input("plese inseri a text:")
# text = a[0]
# for i in a[1:]:
#     if i.isupper():
#         text = text + " "
#     text += i
# print(text)


# a = int(input("plese enter your num:"))
# for i in range(1,a+1):
#     print("*" * i)
# for j in range(a-1,0,-1):
#     print("*" * j)

lst = ["atefe farahbod","maryam farahbod","raha farahbod"]
# print(f"{lst[0:3]}")
# del lst[0]
# print(lst)
# lst.pop()
# print(lst)
# lst.remove("atefe farahbod")
# print(lst)

import pandas
pd = pandas
tbl1 = pd.read_excel(r'C:\Users\user\Desktop\a.xlsx')
print(tbl1)




