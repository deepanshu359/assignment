#Q.1- Reverse the whole list using list methods.
lst=[10,'Python','java',52,'google']
z=lst[::-1]
print(z)

#Q.2- Print all the uppercase letters from a string.
s="World is Small Place"
for i in s:
    if i==i.upper():
        print(i,end="")

print()


#Q.3- Split the user input on comma's and store the values in a list as integers.
a='15'
b='5'
c='65'
d='7'
e='35'
f='16'
print(a,b,c,d,e,f,sep=',')


#Q.4- Check whether a string is palindromic or not.
s=input(" Enter a no:")
if s[::-1]==s:
    print("It is palindromic ")
else:
    print("It is not palindromic")


#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
a=['python',10,'java',40,30]
id(a)
b=a
id(b)
c=a.copy()
id(c)
del c[-1]
print(a)
print(b)
print(c)

#In this, the a and b is the shallow copy because of the same id where c is the deep copy because of its different id.


