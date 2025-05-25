#square fill pattern

n = 5
for i in range(n+1):
    for j in range(n+1):
        print("*",end="")
    print()


#right half pyramid pattern

n = 6
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()


#reverse half pyramid pattern

n = 6
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()


#Triangle star pattern

n = 5
for i in range(1,n+1):
    for j in range(n-1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()


#Number increasing pyramid

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end='')
    print()


#Number changing pyramid

n = 4
k = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k, end='')
        k = k+1
    print()


#left Triangle alphabet pattern

for i in range(n):
    for j in range(i+1):
        print(chr(j+65),end="")
    print()