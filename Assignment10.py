#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop. 

n1=int(input("enter total number of keys: "))
d1={}
for i in range(1,n1+1):
    v=input("enter value of key: ")
    d1[i]=v
l=[]
for j in d1:
    l.append(j)
print("keys of dictionary is: ",l)

#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject.

don={"don1":{"maths":85,"science":86,"computer":67,"english":79},"don2":{"maths":74,"english":67,"thermo":45,"science":76},"don3:{"som":85,"maths":65,"ed":53,"electrical":78}}
n=input("enter student name (a,b,c) to print marks: ")
for i in don:
    if n.lower()==i:
        print(don[n.lower()])
