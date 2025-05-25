# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","w")
# f.write("i am learning javascript\n")
# print(f.write)
# f.close()

# f = open("demo.txt","r")
# line1 = f.readline()
# print(line1)
# line2 =f.readline()
# print(line2)

# f.close()

# f = open("demo.txt","a")
# f.write("from appnacollege")
# f.close()

# f = open("sample.txt","w")
# f.close()

# f = open("demo.txt","r+")
# f.write("abc")
# f.close()

# f = open("demo.txt","w+")
# print(f.read())
# f.write("abc")
# f.close()

# f = open("demo.txt","a+")
# print(f.read())
# f.write("def")
# f.close()

# with open("demo.Txt","r") as f :
#     data = f.read()

# with open("demo.txt","r") as f :
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f :
#     f.write("new data")

# f = open("sample.txt" ,"w")
# f.close

# import os
# os.remove("sample.txt")

# with open("practice.txt","w")as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using java\ni like programming in java.")

# with open("practice.txt","r")as f:
#     data = f.read()

# new_data = data.replace("java", "python")
# print(new_data)

# with open("practice.txt","w")as f:
#     f.write(new_data)

# def check_for_word():
#     word = "learning"
#     with open("practice.txt","r")as f:
#         data = f.read()
#         if(data.find(word) !=-1):
#             print("found")
#         else:
#             print("not found")

# check_for_word()

# def check_for_line():
#     word ="learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r")as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# print(check_for_line())    


count = 0
with open("practice.txt","r")as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)




