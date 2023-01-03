fileobj = open("labn.txt", 'r')
user = fileobj.readline()
u=user.strip("\n")
l=u.split(':')
login=input("enter your login name")
while True:
 if login==l[0]:
    print ("your name is correct now enter your password")
    bas=input("bassword")
    if bas==l[5]:
        print("login is done")
        break
 else:
    print ("your name is wronge")
    break


