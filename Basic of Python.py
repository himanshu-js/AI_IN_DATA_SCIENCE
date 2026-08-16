Hello World Program
print("hello world")
# VARIABLES
x = 2
print(type(x))
y = 2.3
print(type(y))
xy = "I am String"
print(type(xy))
%whos
del xy
%whos
# OPERTAORS
v = 10
r = 20
result = v+r
print(result)
result2 = v-r
print(result2)
10/2 # there is a in-built command that stores the result if variables is not assigned to store the result, command is (-), return float
type(10/2)
10//3  # this gives us the quotient with no decimal values , always return the integer value
%whos
doubleMultiplication = ((v+r)**3)/30
print(doubleMultiplication)
e = 3.0
addingIntWithFloat = v+e # adding a integer value with a float value always gives the result float
print(addingIntWithFloat)
type(addingIntWithFloat)
10%3 # always gives the remainder
s1 = "hello"
s2 = "world"
s = s1+s2
print(s)
%whos
# BOOLEAN
a = True
b = True
c = False
%whos
print(a and b)
print(a and c)
print(c and a)

print(a or b)
print(a or c)
print(c or b)
not(a)  
not(c)
 not((a and b) or (c or a))
# COMPARISON OPERATOR
# the result of comparison operator is always boolean
a = 10
b = 10
c = 5
a == b   # == , true if values are same, otherwise false
a == c
a != c # !, true if values are not the same, otherwise false
a != b
a < b # <, true if a is lesser than b, otherwise false
c < a 
a > b # >, true if a is greater than b, otherwise false
a > c
a <= b # <= , true if a is lesser or equal to b, otherwise false
a >= c # >= , true if a is greater or equal to b, otherwise false
print(not((2!=3) and True) or (False and True))
#  ROUND FUNCTION
 It rounds the input value to a specified number of places or to the nearest integer
print(round(4.2221))
print(round(2.567))
print(round(3.456789,4)) # if next digit is greater than 5, then 1 will be added to the 4th digit
print(round(3.454789,2)) # if next digit is lesser than 5 , then mentioned digit will be same
# DIVMOD FUNCTION
Outputs the quotient and the remainder in a tuple
 qAndRemainder = divmod(34,2)
print(qAndRemainder)
qAndRemainder[0]
qAndRemainder[1]
type(qAndRemainder)
divmod(55,3)
# ISINSTANCE FUNCTION
isinstance(1,int)
isinstance(2.0,float)
isinstance(4.4,(int,float))
isinstance(2+3j,(int,float))
isinstance(2+3j,complex)
# POWER FUNCTION
pow(2,3)
pow(2,3,4)
pow(12,34,23)
# INPUT FUNCTION
a = input("Enter your name :")
type(a)
b = int(input("Enter a number:"))
type(b)
c  = float(input("enter a real value:"))
type(c)
round??