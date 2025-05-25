#string and numeric value can operate together with *
A,B =2,3
Text ="@"
print(2*Text*3)

#string and string operand with +
A,B ="2",3
Text ="@"
print((A+Text)*3)

#numeric value can operand with all arithmetic operator
A,B =2,3
C =12
print(A+B*C)

#Arithmetic expression with integer and float will result in float
A,B =1,2
C =A*B
print(C)

#Result of division operator with two integer will be float
A,B =1,2
C =A/B
print(C)

#Integer division with float and int will give in displayed as float
A,B =1.5,3
C =A//B
print(C,A/B)
  

#closest integers
A,B =12,5
C =A//B
print(C)

A,B =-12,5
C =A//B
print(C)

A,B =12,-5
C =A//B
print(C)