info ={"name":"monu","cgpa":"9.6","marks":[98,87,65.76]}
print(info)
print(type(info))
print(len(info))

info = {
    "name":"rohan",
    "subject":["python","java","c++","c"],
    "topic":("dict","set"),
    "age":21,
    "is_adult":True,
    
}
print(info)
print(type(info))
print(info["name"])
print(info["subject"])
info["name"] = "rahul"
print(info["name"])

#null dictionary
null_dict ={}
null_dict ["name"] = "monu"
print(null_dict)

#Nested dictionary
student = {
    "name":input("enter name :"),
    "subjects":{
        "phy":97,
        "che":98,
        "maths":99
    }
}

print(student["subjects"]["che"])


#dict.keys()
student = {
    "name":input("enter name :"),
    "subjects":{
        "phy":97,
        "che":98,
        "maths":99
    }
}

print(len(student.keys()))
print(type(student))

#dict.values()
student = {
    "name":input("enter name :"),
    "subjects":{
        "phy":97,
        "che":98,
        "maths":99
    }
}

print((student.values()))
print(list(student.values()))
# print(type(student))

#dict .items()
student = {
    "name":"aryan",
    "subjects":{
        "phy":97,
        "che":98,
        "maths":99
    }
}
print(student.items())
print(list(student.items()))

 #dict.get("key")
student = {
    "name":"aryan",
    "subjects":{
        "phy":97,
        "che":98,
        "maths":99
    }
}
print(student.get("name"))

#dict.update(new dict)

student = {
    "name":"aryan",
    "subjects":{
        "phy":97,
        "che":98,
        "maths":99
    }
}
new_dict = {"name":"ayush","age":22}
student.update(new_dict)
print(student)

#set 

collection = {1,2,2,"hello", "hello", "world",4}
print(collection)
print(len(collection))

#set method

#set.add(el)
collection =set()
collection.add(1)
collection.add(2)
collection.add("appnacollege")

print(collection)
print(type(collection))

#set.remove(el)
collection =set()
collection.add(1)
collection.add(2)
collection.add("appnacollege")

collection.remove(1)
print(collection)
print(type(collection))

#set.clear()
collection =set()
collection.add(1)
collection.add(2)
collection.add("appnacollege")

collection.clear()
print(collection)
print(len(collection))

#set.pop()
collection ={"python","hello","appnacollege","world"}
print(collection.pop())
print(collection.pop())

#set.union(set2)
set1 ={1,2,3}
set2 ={3,4,5}
print(set1.union(set2))

#set.intersection(set2)
set1 ={1,2,3}
set2 ={3,4,5}
print(set1.intersection(set2))

#let's practics
dict ={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figure"]
}

print(dict)

subjects ={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(subjects))

marks = {}
x = int(input("enter phy:"))
marks.update({"ph":x})

x = int(input("enter che:"))
marks.update({"che":x})

x = int(input("enter maths:"))
marks.update({"maths":x})

print(marks)

values = {9,"9.0"}
print(values)



