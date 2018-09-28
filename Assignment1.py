#Q.1- Create a list with user defined inputs.
lst=list(input().split())
print(lst)

# Q.2- Add the following list to above created list: 
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’].
lst=[10,20,30,'python','java','perl']
print(lst)
lst2 = lst + ['google','apple','facebook','microsoft','tesla']
print(lst2)


#Q.3 - Count the number of time an object occurs in a list.
lst=['google','apple','facebook','microsoft','tesla']
z=lst.count('google')
print(z)


#Q.4 - create a list with numbers and sort it in ascending order.
lst=[10,20,5,8,3,-2,1]
lst.sort()
print(lst)


#Q.5 - Given are two one-dimensional arrays A and B which are sorted in ascending order.
#Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
A=[1,3,9,5,11,7]
B=[2,8,6,4,12,10]
C=A+B
C=sorted(C)
print(C)



#Q.6 - Count even and odd numbers in that list.
lst=[2,6,3,8,5,1]
no_even=0
no_odd=0
for i in lst:
    if i%2==0:
        no_even+=1
    else:
        no_odd+=1
print("count of even number:"+str(no_even))
print("count of odd number:"+str(no_odd))


Tuples

#Q.1-Print a tuple in reverse order.
tup=[1,2,3,4,5,6]
print(tup[::-1])


#Q.2-Find largest and smallest elements of a tuples.
str="123456"
print(str.isdigit())


Strings

#Q.1- Convert a string to uppercase.
str="hello Chota Don"
str=str.upper()
print(str)


#Q.2- Print true if the string contains all numeric characters.
str="123456"
print(str.isnumeric())


#Q.3- Replace the word "World" with your name in the string "Hello World".
str="Hello World"
str=str.replace("World","Chota Don")
print(str)
