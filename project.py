while True:
    s = input("what you want to do write insert new  users 1  or 2 to login ")
    if s.isdigit():
        a = int(s)
        if a == 1:
            from lab3 import myfristname

            frist_name = myfristname()
            from lab3 import mylastname

            last_name = mylastname()
            from lab3 import mailedrss

            email = mailedrss()
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
                            ii = input(
                                "what you want to do write insert 1 to add project or 2 to view all project \n 3 to edit\t"
                                " 4 to delete"
                                " 5 to search ")
                            if ii.isdigit():
                                m = int(ii)
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
                                    #edit the project
                                elif m == 3:
                                    from insert import startdate

                                    ddd = startdate()
                                    xx = str(ddd)
                                    ky = input("enter 1 to change title or 2 to change Details or 3 to change total target or"
                                               "\n 4 to change start date or 5 to change end date ")
                                    if ky.isdigit():
                                        kk=int(ky)
                                        filedit = open("project.txt", 'r')
                                        us = filedit.readlines()
                                        fileobj.close()
                                        fi = open("project.txt", 'w')
                                        for tt in us:
                                            x = tt.strip('\n')
                                            jj = x.split(":")
                                            if login == jj[0] and xx == jj[4]:
                                                if kk == 1:
                                                    tit = input("enter new title")
                                                    tt = tt.replace(jj[1], tit)
                                                    fi.write(tt)
                                                elif kk == 2:
                                                    det = input("enter new details")
                                                    tt = tt.replace(jj[2], det)
                                                    fi.write(tt)
                                                elif kk == 3:
                                                    total = input("enter new total target")
                                                    egp="EGP"
                                                    tota=total+egp
                                                    tt = tt.replace(jj[3], tota)
                                                    fi.write(tt)
                                                elif kk == 4:
                                                    print("enter new start date ")
                                                    from insert import startdate
                                                    vvv = startdate()
                                                    hh = str(vvv)
                                                    tt = tt.replace(jj[4], hh)
                                                    fi.write(tt)
                                                elif kk == 5:
                                                    print("enter new end date ")
                                                    from insert import enddate
                                                    yyy = enddate()
                                                    hll = str(yyy)
                                                    tt = tt.replace(jj[5], hll)
                                                    fi.write(tt)
                                                else:
                                                    print("enter right number ")
                                            else:
                                                fi.write(tt)

                                        fi.close()
                                    else:
                                        print("enter correct input ")
                                elif m == 4:
                                    #delete projects
                                    print("enter the start date of the project you want to delete ")
                                    from insert import startdate
                                    gip = startdate()
                                    vv = str(gip)
                                    fileobj = open("project.txt", 'r')
                                    user = fileobj.readlines()
                                    fileobj.close()
                                    fil = open("project.txt", 'w')
                                    for pi in user:
                                        x = pi.strip('\n')
                                        nn = x.split(":")
                                        if login == nn[0] and vv == nn[4]:
                                            continue
                                        else:
                                            fil.write(pi)

                                    fil.close()
                                # search for project
                                else:
                                    from insert import startdate

                                    gi = startdate()
                                    v = str(gi)
                                    from insert import enddate

                                    gh = enddate()
                                    b = str(gh)
                                    fileob = open("project.txt", 'r')
                                    use = fileob.readlines()
                                    for oo in use:
                                        x = oo.strip('\n')
                                        y = x.split(":")
                                        if login == y[0] and v == y[4] and b == y[5]:
                                            print(oo)
                                    fileob.close()
                            else:
                                print("enter correct input ")

                    else:
                        print("wrong password")

                else:
                    continue
    else:
        print("enter correct input ")
