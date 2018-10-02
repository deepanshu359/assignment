#Q.1- Take an input year from user and decide whether it is a leap year or not.
year = 2000
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("Year is a leap year".format(year))
       else:
           print("Year is not a leap year".format(year))
   else:
       print("Year is a leap year".format(year))
else:
   print("Year is not a leap year".format(year))


#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
print("Enter length")
length = input()
print("Enter breadth")
breadth = input()
if length == breadth:
  print("It is square")
else:
  print("It is Rectangle")


#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
print("Enter first age")
first = input()
print("Enter second age")
second = input()
print("Enter third age")
third = input()

if first >= second and first >= third:
  print("Oldest is first:",first)
elif second >= first and second >= third:
  print("Oldest is second:",second)
elif third >= first and third >= second:
  print("Oldest is third:",third)
else:
  print("All are equal")


#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR".
age=input("Enter age")
sex=input("SEX?,(M or F)")
marry=input("MARRIED?,(Y or N)")

if (sex=="F"):
   print("Urban areas only")
elif (sex=="M")and(age<=20)and(age>=40):
   print("You can work anywhere")
elif (sex=="M")and(age<=40)and(age>=60):
   print("Urban areas only")
else:
   print("ERROR")



#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
 print("Enter quantity")
quantity = int(input())
if quantity*100>1000:
  print ("Cost is",((quantity*100)-(.1*quantity*100)))
else:
  print("Cost is",quantity*100)


LOOPS

#Q.1- Take 10 integers from user and print it on screen.
a = input('Enter a value: ')
b = input('Enter a value: ')
c = input('Enter a value: ')
d = input('Enter a value: ')
e = input('Enter a value: ')
f = input('Enter a value: ')
g = input('Enter a value: ')
h = input('Enter a value: ')
i = input('Enter a value: ')
j = input('Enter a value: ')

lst1 = [a, b, c, d, e, f, g, h, i, j]
print(lst1)

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
int = 1
while int == 1 :  
   num =input("Enter a number  :")
   print("You entered: ", num)

print("Good bye!")

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
s=("Enter a no:")
print(s)
m=list(map(int,input().split()))
m_square=[]
for i in m:
  m_square.append(i**2)
  print(m_square)
#Q.4- From a list containing ints, strings and floats, make three lists to store them separately.
n=[10,30,"java",50,20.3,0.2,30,"Python"]
n_int=[]
n_float=[]
n_string=[]
for i in n:
    if type(i)==int:
        n_int.append(i)
    elif type(i)==float:
        n_float.append(i)
    else:
        n_string.append(i)
print(n_int)
print(n_float)
print(n_string)


#Q.5- Using range(1,101), make a list containing only prime numbers.
num=[]
for i in range(1,101):
  flag=False
  for j in range(2,i):
    if i%j==0:
      flag=True
  if not flag:
    num.append(i)
print(num)


#Q.6- Print the following patterns: 
#* 
#** 
#*** 
#****
n=6
for i in range(1,6):
    print(""*n+"* "*i)
    n-=1

#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found.
#Iterate over list using for loop.
l=list(map(int,input("Enter list elements:").split()))
ele=int(input("Eter the element to search:"))
if ele in l:
  print("Element found")
  del l[l.index(ele)]
print(l)




    


					

  






   









