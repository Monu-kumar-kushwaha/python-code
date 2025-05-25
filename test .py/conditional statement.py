# trafic light code

# light =input("light colour :")
# if (light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("go")
# else:
#    print("light is broken ")        

# #grade of student

# marks = int(input("marks :"))
# if(marks >=80 and marks <90 ):
#     print( "grade A")
# elif(marks >=70 and marks <80 ):
#     print("grade B")  
# elif(marks >=60 and marks <70 ):
#     print("grade C")
# else:
#     print("grade D")      

# #practic question

# A = int(input("A:"))
# G = input("M/F:")

# if((A==1 or A==2) and G=="M"):
#     print("fee is 100")
# elif(A==3 or A==4 or G=="F"):
#     print("fee is 200")
# elif(A==5 and G=="M"):
#     print("fee is 300")
# else:
#     print("no fee") 

# single line if/Ternary operator

# food = input("food:")
# eat = "yes" if food =="cake" else "no"
# print("eat:",eat)

# food =input("food:")
# print("sweet" if food =="cake" or food =="samosa" else "not sweet")

# clever if / Ternary operator

age = int(input("age:"))
vote =("no","yes") [age>=18]
print("vote:",vote)

sal =float(input("salary:"))
tax =sal*(0.1,0.2) [sal <=50000]
print(tax)

P =float(input("P:"))
R =float(input("R:"))
T =float(input("T:"))
SI =(P*R*T)/100
print(SI)