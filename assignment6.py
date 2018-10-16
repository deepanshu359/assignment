#Q.1
import re
def email():
    email = input("enter the mail address::")
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)

    if match:
        print ("valid email :", match.group())
    else:
        print ("not valid:")

email()

#Q.2
import re 
  
def isValid(d): 
    daku = re.compile("(0/+91)?[6-9][0-9]{9}") 
    return daku.match(d) 
   
d = "9625657805"
if (isValid(d)):  
    print ("Valid Number")      
else : 
    print ("Invalid Number") 
