def myfristname():
 while True:
   frist = input("enter your frist name")
   if  frist.isspace()==True:
    continue
   else:
      return frist



def mylastname():
 while True:
   last = input("enter your last name")
   if  last.isspace()==True:
    continue
   else:
      return last


def mypassword():
   password = input("enter your password")
   return password



import re
def mailedrss():
    while True:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email=input("enter your mail")
        if(re.fullmatch(regex, email)):
            return email
        else:
            print("Invalid Email")
            continue


