#Q.1

def area(r):
    a=4*3.14*(r**2)
    return a
n=int(input("enter radius: "))
print("area of sphere is : ",area(n))

#Q.2

l=[]
def perfect(n):
    p=0
    
    for i in range(1,n):
        if n%i==0:
            p=p+i
    if p==n:
        l.append(p)
    return l
for j in range(1,1000):
    a=perfect(j)

print(a)

#Q.3

n=int(input("enter a number: "))
for i in range(1,11):
    a=n*i
    print(n,"X",i,"=",a)

#Q.4

def pow(x,y):
    if y==1:
        return x
    else:
        return x * pow(x,y-1)
n1=int(input("enter a number: "))
n2=int(input("enter a number: "))
print("power of number is",pow(n1,n2))
