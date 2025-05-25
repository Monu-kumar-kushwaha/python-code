#function 
# Block of statement that perform specific task.

#syntax
# def func_name(param 1, param2): #function defination
#     #some work
#     return Val
# func_name(arg1, arg2) #function call

# def sum(a,b):
#     sum = a+b
#     return sum
# print(sum(2,1))

# def calu_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum
# calu_sum(12,56)

# #average of 3 number 

# def calu_avg(a,b,c):
#     sum =a+b+c
#     avg =sum/3
#     print(avg)
#     return avg
# calu_avg(12,34,45)

# #default parameter 
# def calu_prod(a,b=5):
#     print(a*b)
#     return a*b
# calu_prod(3)

# cities = ["delhi", "gurgaoun","mumbai", "noida","chennai", "puna"]
# heroes =["ironman", "thor", "superman", "saktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)    


# heroes = ["ironman", "thor", "superman", "saktiman"]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
#     print()  # To move to the next line after printing all items

# print_list(heroes)
# print(heroes)

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# cal_fact(5)

# def converter(usd_val):
#     inr_val = usd_val*83
#     print(usd_val, "USD", inr_val,"INR")
# converter(34)

# #Recursion 
# #when fnction call itself repeatedily

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(3)

# def fact(n):
#     if(n ==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# def calu_sum(n):
#     if(n==0):
#         return 0
#     return calu_sum(n-1)+n

# sum = calu_sum(5)
# print(sum)


def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx + 1)

fruits = ["apple", "banana", "grapes", "litchi"]

print_list(fruits)

