'''a=int(input("Enter a nomber for addition"))                  #--------------1 add and div
b=int(input("Enter another nomber for addition"))
print("sum is",a+b)
if a>b:
    print("div is",a/b)
else:
     print("div is",b/a)

#------------------------------------------------------------------------------2 area of triangle
a=float(input("enter the height of triangle "))
b=float(input("enter the weidht of triangle "))
area=0.5*a*b
print("area of triangle is",area)

#-------------------------------------------------------------------------------3 swap
name='karan'
age=18
tmp=name
name=age
age=tmp
print(name)
print(age)

#------------------------------------------------------------------------------4 random num
import random
print(random.randint(1,99))

#------------------------------------------------------------------------------5 km to miles
km=float(input("enter the distance in km"))
mile=0
mile=km*0.621371
print("distance in miles is",mile)

#------------------------------------------------------------------------------6 celsius to Farenhiet
celsius=int(input('enter the temperature in celsius='))
farenhite=(celsius*9/5)+32
print('temp in farenhite is ',farenhite)

#-------------------------------------------------------------------------------7 calendar 
import calendar
year=int(input('enter the year='))
month=int(input('enter the month='))
print(calendar.month(year,month))

#------------------------------------------------------------------------------8 quadratic equation
import math
a=int(input('enter the second degree coeffecient of the equation='))
b=int(input('enter the first degree coeffecient of the equation='))
c=int(input('enter the zero degree coeffecient of the equation='))
d=(b**2)-4*a*c
if d>=0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('the roots of the quadratci equation are',x1 ,'&', x2)
else:
    real=-b/2*a
    imaginary=math.sqrt(abs(d))/2*a
    print(real,'+',imaginary,'i')
    print(real,'-',imaginary,'i')

#------------------------------------------------------------------------------9 swap without temp
name="karan"
age=18
name,age=age,name
print('name',name)
print('age',age)

#-------------------------------------------------------------------------------10 check polarity
test=int(input("enter a number to test="))
if test>0:
    print("number is positive")
elif test<0:
    print("number is positive")
else:
    print('its ZERO!')

#------------------------------------------------------------------------------11 odd or even
test=int(input('enter a number to test evenor odd='))
if test%2==0:
    print("its EVEN!")
else:
    print("its ODD!")

#------------------------------------------------------------------------------12 check leap year
test=int(input('enter a year to check leap year or not='))
if test%400==0 and test%100==0:
    print(test,'is a leap year')
elif test%4==0 and test%100!=0:
    print(test,'is a leap year')
else:
    print(test,'is not a leap year')

#-----------------------------------------------------------------------------13 check prime
test=int(input('enter the number to check prime='))
flag=False
if test==1:
    print('number is not a prime')
for i in range (2,test):
    if test%i==0:
        flag=True
        break
if flag:
    print('number is not a prime')
else:
    print("number is a prime")

#----------------------------------------------------------------------------14 prime in interval 
print('prime number between 1 and 10 are:')
for num in range(1,11):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
#---------------------------------------------------------------------------15 factorial
n=int(input('enter the number to find factorial'))
def fact(i):
    return 1 if (i==1 or i==0) else i*fact(i-1)  
print(fact(n))
#--------------------------------------------------------------------------16 table
n=int(input('enter the table number='))
for i in range (1,11):
    print(n,'x',i,'=',n*i)

#---------------------------------------------------------------------------17 fibonacci 
n=int(input('enter the number for fibonacci series='))
L=[0]
for i in range(0,n):
    if L[-1]==0:
        L.append(i+1)
    else:
        L.append(L[-2]+L[-1])
print(L)

#--------------------------------------------------------------------------18 armstrong
n=int(input('enter a number='))
num=str(n)
size=len(num)
temp=n
sum_num=0
while temp>0:
    digit=temp%10
    sum_num+=digit**size
    temp//=10
if sum_num==n:
    print('its an armstrong number')
else:
    print('its not an armstrong')

#--------------------------------------------------------------------------19 armstrong in interval
upper=int(input('enter the range upper limit='))
lower=int(input('enter the range lower limit='))
def check_arms(n):
    num=str(n)
    size=len(num)
    temp=n
    sum_num=0
    while temp>0:
        digit=temp%10
        sum_num+=digit**size
        temp//=10
    if sum_num==n:
        print(n)
for i in range(lower,upper):
    check_arms(i)
'''
limit=int(input('enter the limit='))
sum=0
for i in range(0,limit+1):
    sum+=i
print('sum of natural numbers upto',limit,'is',sum)
'''
#--------------------------------------------------------------------------20 
def lcm_finder(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while True:
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    return lcm
x=int(input('enter a number='))
y=int(input('enter another number='))
a=lcm_finder(x,y)
print('the lcm of numbers is=',a)

#------------------------------------------------------------------------
def hcf_finder(x,y):
    if x>y:
        smallerr=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
x=int(input('enter a number='))
y=int(input('enter another number='))
a=hcf_finder(x,y)
print('the hcf of numbers is=',a)

#--------------------------------------------------------------------------
dec=int(input('enter a number='))
print('binary equivalent',bin(dec))
print('octal equivalent',oct(dec))
print('hexadecimal equivalent',hex(dec))

#--------------------------------------------------------------------------
char=str(input('enter a character='))
print('the ascii value of the character is',ord(char))

#---------------------------------------------------------------------------
def add(a,b):
    return a+b
def sub(a,b):
    if a>b:
        return a-b
    else:
        return b-a
def mul(a,b):
    return a*b
def div(a,b):
    if a>b:
        return a//b
    else:
        return b//a
a=int(input("enter a number="))
b=int(input("enter another number="))
anssum=add(a,b)
anssub=sub(a,b)
ansmul=mul(a,b)
ansdiv=div(a,b)
print("the sum=",anssum)
print("the sub=",anssub)
print("the mul=",ansmul)
print("the div=",ansdiv)
'''
#-----------------------------------------------------------------------------
