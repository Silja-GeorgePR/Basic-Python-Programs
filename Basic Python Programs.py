
# Write a Python program which accepts the radius of a circle from the user and compute the area. 

radius=input("enter the radius:")
r=float(radius)
area= 3.14*r*r
print("Area of Circle is:", area)



# Write a Python Program to accept the details of a student like name, roll number and mark and display it.
# Sample input: Enter the name: Anisha
#  Enter the roll number: 21
#  Enter the mark: 78
# Sample output: Name: Anisha
#  Roll No: 21
#  Mark: 78

name=input("Enter the name:")
roll=input("Enter the roll number:")
mark=input("Enter the mark:")
print("\nName:", name, "\nRoll No:", roll, "\nMark:", mark)



# Write a Python program to get the largest number from a list

num = []
n = int(input("Enter the number of elements: "))


for i in range(0, n):
    ele = int(input())
    num.append(ele) 
    

print(max(num),"is the largest number")





# Write a Python program to accept a string value from the user and display the count of each character in that string.

userString = input("Enter any string: ")
count ={}
for i in userString:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(str(count))





# Write a Python program to copy element 44 and 55 from the following tuple into a new tuple. tuple1 = (11, 22, 33, 44, 55, 66) 

tuple1=(11,22,33,44,55,66)
tuple1Copy=tuple1[3:5]
print(tuple1Copy)





# write a Python program to iterate from start number to the end number and print the sum of the current and previous number.

n=int(input("enter the starting range: "))
previousNum = n-1
for i in range(n,(n+10)):
    sum = previousNum + i
    print('Current Number '+ str(i)+'Previous Number ' + str(previousNum) + ' sum is ' + str(sum)) # <- This is the issue.
    previousNum=i




# Write a Python program to print only those numbers which are divisible of 5. 

x = list(map(int, input("Enter multiple values: ").split()))  
y=[]
for i in range(len(x)):
    if ((x[i]) %5 == 0):
        y.append(x[i])
print(y)




# Write a Python program to check whether a number is prime or not. 



num = int(input("Enter the number: "))
flag=False

if num > 1:
    for i in range(2, int(num/2)):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")





# Write a Python program to reverse a list using for loop. 

lists = list(map(int, input("Enter values: ").split())) 

# for i in range(len(lists)):
#     last_item = lists.pop()
#     lists.insert(i, last_item)
# print(lists)
lists.reverse()
print(lists)





# Write a Python program to print the following pattern.
#  *
#  **
#  ***
#  **** 
 

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")





# Write a Python function to find the maximum of three numbers 

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
a,b,c =input("Enter three values: ").split()  
print("Maximum of numbers: ", max_of_three(a,b,c))





# Write a Python function called exponent(base,exp) that returns an integer value of base raises to the power of exp. 

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))





# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers 
# smaller than the specified number. 

def sum_of_cubes(n):
    tot=0
    if n>0:
        for i in range(1, n):
            tot +=i*i*i
    else :
        return(print(" enter a positive number"))
   
    return tot
num=int(input("enter a number: "))
print("Sum of cubes smaller than the specified number: ", sum_of_cubes(num))





# Write a Python program to construct the following pattern, using a nested for loop.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

n=int(input("Enter the number of rows"))
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')





# Write a Python program which iterates from 1 to 10. For multiples of 2, print “Fizz” instead of the number and for the
# multiples of 5, print “Buzz”. For numbers which are multiples of both 2 and 5, print “FizzBuzz”. 


for i in range(1,11):
  
  if(i%2==0 and i%5==0):
    print("FizzBuzz")
  
  elif(i%2 == 0):
    print("Fizz")
 
  elif(i%5 == 0):
    print("Buzz")
 
  else:
    print(i)





# Write a Python program to find the most frequent item in a list of numbers. 

def frequent(lists):
    counts = 0
    num = lists[0]
    for i in lists:
        items = lists.count(i)
        if(items > counts):
            counts = items
            num = i

    return num

lists = list(map(int, input("Enter values: ").split())) 
print(frequent(lists))





# Write a Python program to find the sum of squares of the numbers in a list.

lists = list(map(int, input("Enter values: ").split())) 

res = sum(map(lambda i : i * i, lists))
print ("The sum of squares of list is : " + str(res))
  





# Write a Python program using for loop that will iterate from 1 to 15. For each iteration, check if the current number is odd
# or even, and display the message to the screen as odd or even. 

for i in range(1,16):
    if (i% 2)==0:
        print(i,"- even")
    else :
        print(i,"- odd")





# Write a Python program to convert temperatures to and from Celsius Fahrenheit. [Formula: c/5=f-32/9 where c=temperature
# in Celsius and f= temperature in Fahrenheit.] 

import sys


temp = input("Input the  temperature(F/C at the end) : ")
degree = int(temp[:-1])
temp_in = temp[-1]
temp_convert=None
result=None
if temp_in.upper() == "C":
        result = int(round((9 * degree) / 5 + 32))
        temp_convert = "Fahrenheit"
elif temp_in.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    temp_convert = "Celsius"
else:
#     print("Improper convention.")
    sys.exit("Invalid input")
   
    
print("The temperature in",temp_convert , "is", result, "degrees.")





# Write a Python function to calculate the factorial of a number (a nonnegative integer). 
# The function accepts the number as an argument. 

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

n=int(input("Enter a number to find factorial : "))

print("The factorial is: ",factorial(n))





# Code to find the area of an equilateral triangle. Output should be as displayed

import math
side = float(input("Enter the side of the equilateral triangle: "))
area = ((math.sqrt(3))/4)*pow(side,2)
print(round(area,3))





# Write a program to find the area and perimeter of a rectangle using functions

def area(a,b):
    return (a*b)
def perimeter(a,b):
    return (2*(a+b))
l=float(input("Enter length: "))
b= float(input("Enter width: "))
print("Area is : ", area(l,b))
print("Perimeter is: ", perimeter(l,b))





# Write a program to print the fibonacci series till a specified number

n=int(input("Enter the limit: "))
a=0
b=1
i=0
if n<=0:
  print("Enter positive number ")
elif n==1:
  print(a)
else:
  print("Fibonacci sequence:")
  while i < n:
       print(a)
       next = a+ b

       a = b
       b = next
       i += 1





# code to find the minimum of 3 number using conditional statements. Output should be as displayed

a,b,c = input("Enter three numbers followed by  : ").split()

print("First number :",a)
print("Second number :",b)
print("Third number :",c)
if a==b==c:
     print("Entered numbers are equal!!!")
elif a<b and a<c:
     print(a," is smallest")
elif b<a and b<c:
    print(b," is smallest")
else:
    print(c," is smallest")





# Write a program to print star pyramind. The number of rows should be taken as input from the user

rows = int(input("Enter the number of rows: "));
for i in range(0, rows):
    for j in range(0, rows-i-1):
        print(end=" ")
    for j in  range(0, i+1):
        print("*", end=" ")
    print()





# code to convert hour into seconds. Output should be as displayed

def to_seconds(t):
     return (t*3600)
time_in_hours = int(input("Enter time in hours: "))
print(time_in_hours ," Hour is equal to" ,to_seconds(time_in_hours) ," Seconds")





# Write a program to print multiplication table(upto 10)

num = int(input("Enter a number to find the multiplication table: "))
for i in range(1, 11):
    print(i, 'x', num,  '=', num*i)





# Write a program to take your 5 favorite food as list and print each as 'I like Biriyani'

print('Enter your 5 favorite food items: ')
items=[]
for i in range(0,5):
    food=str(input())
    items.append(food)
for j in range(0,5):
    print('I like ',items[j])







