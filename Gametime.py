# import random as r

# user1 = int(input("Guess "))
# user2 = int(input("Guess "))

# sysNumber = r.randrange(1,100)
# print(sysNumber)

# if (abs(user2 - sysNumber)) < (abs(user1 - sysNumber)):
#     print("user2 won")
# elif (abs(user2 - sysNumber)) > (abs(user1 - sysNumber)):
#     print('user1 won')

# Task1
# num = int(input("enter a number "))
# factorial = 1
# if num == 0:
#     print("factorial of 0 is 1")
# elif num < 0:
#     print("factorial does not exit nagative numbers")
# else:
#     for i in range(1, num+1):
#         factorial *= i
#     print(factorial)

# Task2
# import random as rrr
# correct_answer = rrr.randrange(1,1000)

# guess_count = 0
# guess_limit = 5
# while guess_count < guess_limit:
#     a = int(input("Texmin "))
#     guess_count += 1
#     if a == correct_answer:
#         print("Tebrikler dogru secim etdiniz")
#         break
#     elif a > correct_answer:
#         print("daha kicik")
#     elif a < correct_answer:
#          print("daha boyuk")

# print(correct_answer)

# 8544
# a = int(input())
# x = 1
# aa=[]
# while True:
#     if pow(x,2) <= a:
#         aa.append(pow(x,2))
#         x+=1
#     else:
#         break

# print(*aa)

# a = int(input())


# Task1
# num = int(input("enter a number "))
# factorial = 1
# if num == 0:
#     print("factorial of 0 is 1")
# elif num < 0:
#     print("factorial does not exit nagative numbers")
# else:
#     for i in range(1, num+1):
#         factorial *= i
#     print(factorial)

# Task2
# import random as rrr
# correct_answer = rrr.randrange(1,1000)

# guess_count = 0
# guess_limit = 5
# while guess_count < guess_limit:
#     a = int(input("Texmin "))
#     guess_count += 1
#     if a == correct_answer:
#         print("Tebrikler dogru secim etdiniz")
#         break
#     elif a > correct_answer:
#         print("daha kicik")
#     elif a < correct_answer:
#          print("daha boyuk")

# print(correct_answer)

# task3

# sum_plus = 0
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     else:
#         if a > 0:
#             sum_plus += a
# print(sum_plus)

# task5
# sum_plus = 0
# while True:
#     a = int(input("Eded daxil edin "))
#     if a < 0:
#         break
#     else:
#         if a %2 != 0:
#             sum_plus += a
# print(pow(sum_plus,2))

# biggest_one = 0
# while True:
#     a = str(input())
#     if a == 0:
#         break
#     else:
#         if a != 0:
#             biggest_one = max(a)


# 1606
# num = int(input())
# if num < 0:
#     num *= -1
# dublicate = num

# length = 0

# while num > 0:
#     num = int(num/10)
#     length +=1

# first = int(dublicate / pow(10,(length-1)))
# last = int(dublicate % 10)

# print(first+last)


# 1606
# a = int(input())
# if a < 0:
#     a *= -1
# length = len(str(a))
# first = int(a / pow(10,(length-1)))
# last = int(a % 10)
# print(first+last)


# 1605
# num = int(input())
# if num < 0:
#     num *= -1
# dublicate = num

# length = 0

# while num > 0:
#     num = int(num/10)
#     length +=1


# second = int(dublicate // pow(10,length - 2) % 10)
# print(second)

