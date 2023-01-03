s = input("what you want to do write insert 1 to add or 2 to login ")
a = int(s)
if a == 1:
    from lab3 import myfristname

    frist_name = myfristname()
    from lab3 import mylastname

    last_name = mylastname()
    from lab3 import mypassword

    password = mypassword()
    while True:
        confirm = input("confirm password")
        if confirm != password:
            print("wrong confirm")
            continue
        else:
            print("done")
            break
    email = input("enter your email")
    phone = input("enter your phone number")

    urerifo = f"{frist_name}:{last_name}:{email}:{phone}:{password}:{confirm}\n"
    print(urerifo)

    try:
        fileobj = open("labn.txt", 'a')
    except Exception as e:
        print(e)
    else:
        fileobj.write(urerifo)
        fileobj.close()
else:
    fileobj = open("labn.txt", 'r')
    user = fileobj.readline()
    u = user.strip("\n")
    l = u.split(':')
    login = input("enter your login name")
    while True:
        if login == l[0]:
            print("your name is correct now enter your password")
            bas = input("bassword")
            if bas == l[5]:
                print("login is done")
                # addhere
                break
        else:
            print("your name is wronge")
            break
