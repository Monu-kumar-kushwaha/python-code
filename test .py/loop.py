# count = 1
# while count <= 5:
#     print("hello")
#     count += 1

# i = 1 
# while i <= 500:
#     print("apple",i)
#     i += 1

#  #print number 1 to 5
# i = 1
# while i<=5:
#     print(i)
#     i += 1



# num = [1,4,9,16,25,36,49,64,81,100]

# i = 0
# while i < len(num):
#     print(num[i])
#     i += 1

# #search for a number of x
# num = [1,4,9,16,25,36,49,64,81,100]
# x = 36
# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("found at idx", i)
#     else:
#         print("finding...")

#     i += 1

# #break and continue

# #break statement
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

# #continue statement
# i = 1
# while i <= 10:
#     if(i == 3):
#     # if(i%2 == 0): # for odd number
#     # if(i%2 != 0): # for even number
#         i += 1
#         continue #skip
#     print(i)

#     i += 1

# #loop 

# nums = [1,2,3,4,5,6]

# for val in nums:
#     print(val)

# tup =(1,3,6,3,5,6,4)

# for nums in tup:
#     print(nums)

# veg =("ladyfinger", "cucumber", "potato", "tomato")
# for word in veg:
#     print(word)

# str = "apple"

# for char in str:
#     print(char)


# # for loop with else
# str = "apple"
# for char in str:
#     print(char)
# else:
#     print("END")

# #Let's practice

# nums = [1,4,9,16,25,36,49,64,81,100]

# for val in nums:
#     print(val)

# nums =(1,4,9,16,25,36,49,64,81,100)
# x = 49
# idx = 0

# for el in nums:
#     if(el ==x):
#         print("number found at idx ", idx)
#         break
#         idx +=1

#range
# for el in range(5): # range (start)
#     print(el)

# for el in range(1,5): #range (start, stop)
#     print(el)

# for el in range(2, 100, 2): #range (start, stop, step) (for even )
#     print(el)

# for el in range(1, 100, 2): #range (start, stop, step) (for odd )
#     print(el)

# for el in range(100, 0, -1): #range (start, stop, step) (reverse)
#     print(el)


# #Let's practics

# for i in range(1,100):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# n= int(input("enter number :"))

# for i in range(1,11):
#     print(n*i)

# #pass

# for i in range(5):
#     pass
# print(" welcom")

#let's practice 

#for loop Q1
# n = int(input("enter number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i

# print("total sum:", sum)


# #while loop Q1

# n = int(input("enter number: "))
# sum = 0

# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print("total sum:", sum)

# #WHILE LOOP Q2
# n = int(input("enter number: "))
# fact = 1

# i = 1
# while i <= n:
#     fact *= i
#     i += 1

# print("factorial:", fact)

#for loop Q2

n = int(input("enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("factorial:", fact)




