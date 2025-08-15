# 20 questions on  Varialbles , Data Types and Operators
#1 swap numbers using temp variable

a=5
b=8
print("before swapping", a,b)
temp=a
a=b
b=temp
print( "after swapping",a,b)

#2 identify data types

c=input()
d=int(input()) 
e=float(input())
print("type is" ,type(c))
print("type is", type(d))
print("type is", type(e))

#3 simple calculator
f=23
g=7
print("addition",f+g)
print("subtraction" ,f-g)
print("multiplication",f*g)
print(  "division", f/g)
print("double division" ,f//g)
print("moduolus (remainder)", f%g)

#4 salary hike
sal=15000
hike=15
new_sal=((hike/100)*sal)+sal
print("new salary is", new_sal)


#5 area and perimeter ofcircle
r=int(input())
area=(3.14159*(r**2))
print("area of circle is", area)
perimeter=2*3.14159*r
print("perimeter of circle is",perimeter)

#6 ASCII
h=input()
print(ord(h))

#7
num=int(input())
if num%2==0:
    print("Even")
else:
    print("Odd")

#8
i = 5
j = 8

i += 1
print("+= ", i)

j -= 1
print("-= ", j)

i *= j
print("*= ", i)

i /= j
print("/= ", i)

# Integer division
i //= j
print("//= ", i)

i %= j
print("%= ", i)



#9 BOOLENA AND LOGICAL
a = 5
b = 7
print(a and b)
print(a or b)
print(not a)


#10 bit wise shift pratice
a = 17
b = 5
print(a<<b)
print(a>>b)


##11bitwise AND ,OR ,XOR, NOT
a=12
b=5
print(a&b)
print(a|b)
print(a^b)
print(~a) #NOT operator



##12 data type conversition
# convert str to int
a = "123"
b=int(a)
print(type(b))
print(b)
print()
## convert int to float
a = 123
b=float(a)
print(b)
print(type(b))
print()
# convert float to str
a = 123.45
b=str(a)
print(b)
print(type(b))
print()
# convert int to bool
a = 123
b=bool(a)
print(b) #True
print(type(b))



#13 conversition of temperature
tem_c=33
tem_f=(tem_c*9/5)+32
print(" temperature in fahrenheit",tem_f)

#14
k=55
l=3
print("remainder",k%l)
print("quotient",k//l)




#15
str1='Akash Kumar'
print("all lower is =",str1.lower())
print("all upper is =", str1.upper())
print("length of string is=", len(str1))
print( "akash" in str1)
print("Akash" in str1)




#16
input1=256
sum=0
while input1>0:
    dig=input1%10
    sum=sum+dig
    input1=input1//10
print(sum)

#17 identify and equality == and is with two list to compare
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
print(list1==list2) #True
print(list1 is list2) #False

#18 age in months and days

age=int(input("enter the age"))
months=age*12
days=age*365
print("age in months",months)
print("age in days",days)

#19 anakyse type of x=10+3.5, y="age"+ str(30), z=True+False+2
x=10+3.5
y="age"+ str(30)
z=True+False+2
print("type of x is",type(x))
print("type of y is",type(y))
print("type of z is",type(z))
 

 # 20 explain this
n=5
print("n<<1 is ",n<<1)
print("n>>2",n>>2)
#n<<1 means the bit wise operator move left 1 step 
# 5 is 0101 after moving 1010 is 10
#n>>2 means the bit wise operator move right 2 step
# 5 is 0101 after moving 001 is 0