marks =[76,74,87,90,56]
print(marks)
print(type(marks))
print(marks[2])
print(marks[4])

student =["rahul",78.5,21,"ranchi"]
student[2] =20
print(student)
print(student[2])

# # marks =[45,76,98,87,76]
var1 =["apple","mango","banana","orange","pinapple"] #variable
print(var1[1:4])
print(var1[4:]) #[4:0]
print(var1[:4]) #[0:4]
print(var1[-3:-1])

 #list.append()
list =[2,3,5]
list.append(4)
print(list)

#list.sort()    (ascending order)
list =[2,8,2,4,1]
list.sort()
print(list)

#list.sort(reverse =True)  (descendind order)
list =[3,5,1,6,8,6]
list.sort(reverse =True)
print(list)

#list.reverse()
list =["a","d","g","t","b","c"]
list.reverse()
print(list)

#list.insert(idx,el)
list =[3,5,6,4]
list.insert(5,4)
print(list)

#list.remove
list =[2,4,6,7]
list.remove(6)
print(list)

#list.pop(idx)
list = [3, 5, 7, 6, 6]
list.pop(4)
print(list)

#tuple
tup =(3,4,6,7,7)
print(tup)
print(type(tup))
print(tup[3])
# tup[0] =54 #NOT allowed in python

#tup.index(el)
tup =(4,6,8,7,5,3)
print(tup.index(8))
 
#tup.count(el)
tup = (4,5,6,4,6)
print(tup.count(6))


#practic question
movies =[]
movies.append(input("enter first movie:"))
movies.append(input("enter second movie:"))
movies.append(input("enter third movie:"))
print(movies)

# list1 = ["m","a","a","m"]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

tup = ("c","d","a","a","b","b","a")
print(tup.count("a"))

list = ["c","d","a","a","b","b","a"]
print(list.sort(),list)