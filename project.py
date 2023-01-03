s = input("what you want to do write insert new  users 1  or 2 to login ")
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
    login = input("enter your login name")
    fileobj = open("labn.txt", 'r')
    user = fileobj.readlines()
    for u in user:
            x = u.strip('\n')
            l = x.split(":")
            if login == l[0]:
                print("your name is correct now enter your password")
                bas = input("bassword")
                if bas == l[5]:
                    print("login is done")
                    while True:
                        s = input("what you want to do write insert 1 to add project or 2 to view all project 3 to edit"
                                  "4 to delete"
                                  "\n  5 to search for project ")
                        m = int(s)
                        if m == 1:
                            # from insert import myowner
                            # owner = myowner()
                            from insert import myTitle

                            title = myTitle()
                            from insert import myDetails

                            Details = myDetails()
                            from insert import Total_targe

                            total = Total_targe()
                            from insert import startdate

                            sdate = startdate()
                            from insert import enddate

                            edate = enddate()

                            urerifo = f"{login}:{title}:{Details}:{total}:{sdate}:{edate}\n"
                            print(urerifo)
                            # put login name in owner
                            try:
                                fileproject = open("project.txt", 'a')
                            except Exception as e:
                                print(e)
                            else:
                                fileproject.write(urerifo)
                                fileproject.close()
                        elif m == 2:
                            try:
                                fileproject = open("project.txt", 'r')
                            except Exception as e:
                                print(e)
                            else:
                                data = fileproject.read()
                                print(data)
                                fileproject.close()



                        elif m == 2:

                            try:

                             fileproject = open("project.txt", 'r')

                            except Exception as e:

                                print(e)

                            else:

                                data = fileproject.readlines()

                                for data in fileproject:
                                    print(data)

                                fileproject.close()

                        elif m == 3:
                            from insert import startdate
                            ddd= startdate()
                            xx= str(ddd)
                            kk=input("enter 1 to change title or 2 to change Details or 3 to change total target or"
                                     "4 to change start date or 5 to change end date ")
                            filedit = open("project.txt", 'r')
                            us = filedit.readlines()
                            fileobj.close()
                            fi = open("project.txt", 'w')
                            for u in user:
                                x = u.strip('\n')
                                jj = x.split(":")
                                if login == jj[0] and xx == jj[4]:
                                    if kk == 1:
                                        tit = input("enter new title")
                                        fi.write(u.replace(jj[1],tit))
                                    elif kk==2:
                                        det = input("enter new details")
                                        fi.write(u.replace(jj[2],det))
                                    elif kk == 3:
                                        total = input("enter new total target")
                                        fi.write(u.replace(jj[3],total))
                                    elif kk==4:
                                        from insert import startdate
                                        vvv = startdate()
                                        hh = str(vvv)
                                        fi.write(u.replace(jj[4],hh))
                                    elif kk == 5:
                                        from insert import enddate
                                        yyy = enddate()
                                        hll = str(yyy)
                                        fi.write(u.replace(jj[4],hll))
                                    else:
                                        print("enter right number ")
                                    fi.close()

                            fi.close()

                        elif m == 4:
                            from insert import startdate
                            gip = startdate()
                            vv= str(gip)
                            fileobj = open("project.txt", 'r')
                            user = fileobj.readlines()
                            fileobj.close()
                            fil = open("project.txt", 'w')
                            for u in user:
                                x = u.strip('\n')
                                nn = x.split(":")
                                if login == nn[0] and vv == nn[4]:
                                    continue
                                else:
                                 fil.write(u)

                            fil.close()
#search for project
                        else:
                         from insert import startdate
                         gi=startdate()
                         v=str(gi)
                         from insert import enddate
                         gh=enddate()
                         b=str(gh)
                         fileob = open("project.txt", 'r')
                         use = fileob.readlines()
                         for u in use:
                            x = u.strip('\n')
                            y=x.split(":")
                            if login==y[0] and v==y[4] and b==y[5] :
                             print(u)
                         fileob.close()


                else:
                    print("wrong password")

            else:
             continue