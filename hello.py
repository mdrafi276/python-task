

# print(amount.pop(1))

# mylist = ["apple", "banana", "cherry"]
# print(mylist[1])
# my_list = ['rafi', "shakib", "rifat", "arafat"]
# print(type(my_list))
# list1 = ["abc", 34, True, 40, "male"]
# print(list1)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:6])
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
# thislist1 = ["apple", "banana", "cherry"]
# for x in range(len(thislist1)):
#     print(x)

# for x in range(2, 4):
#   print()
# def add(num1, num2):
#     return num1 + num2
# add(3, 8)
# a = 5
# b = 10

# sum = a + b
# print(sum)

# more lines of code

# a = 2
# b = 10
# sum = a * b
# print(sum)
# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum
# calc_sum(1, 2)
# calc_sum(2, 10)
# calc_sum(3, 8)


# function definition

# def calc_sum1(x, y): #parameters
#     return  x * y
    
# sum = calc_sum1(2, 3) # function call; prguments
# sum = calc_sum1(5, 10)
# print(sum)




# avarage of 3 numbers

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg
# calc_avg(98, 97, 95)
# calc_avg(89, 75, 90)
# calc_avg(92, 90, 90)


# cities = ["delhi", "gurgaon", "pune", "noida", "mumbai", "chennai"]
# hrros = ["thor", "ironman", "captain america", "shaktiman", "spiderman"]
# def print_len(list):
#     print (len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
    
# print_list(hrros)
# print_list(cities )



# def cal_fect(n):
#     fact = 1
#     for i in range(1, n+1):
#        fact *= i
#     print(fact)

# cal_fect(5)


# ? convet to usd $ to indian ropi inr

# def converter(usd_val):
#       inr_val = usd_val * 83
#       print(usd_val, "usd =", inr_val, "INR")
    
# converter(2)

# def converter(usd_val):
#       bd_val = usd_val * 115
#       print(usd_val, "usd =", bd_val, "BD")
    
# converter(2)

# recursive function 
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(10)

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(4))
# def cal_sum(n):
#    if(n == 0):
#        return 0
#    return cal_sum(n-1) + n
      

# print(cal_sum(2))

# -0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0
# write a recursrive function to calculate the sum of first n natural numbers.

# write a recursive function to print all elements in a list 

# Hint: use list & index as parameters.


# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)
# fruits = ["mango"," litchi ", "apple", "banana"]
# print_list(fruits)
