while True:
    s=input("what you want to do write insert 1 to add project or 2 to view all project  ")
    a=int(s)
    if a==1:
        from insert import myowner
        owner = myowner()
        from insert import myTitle
        title=myTitle()
        from insert import myDetails
        Details=myDetails()
        from insert import Total_targe
        total=Total_targe()
        from insert import startdate
        sdate= startdate()
        from insert import enddate
        edate = enddate()

        urerifo=f"{owner}:{title}:{Details}:{total}:{sdate}:{edate}\n"
        print(urerifo)
#put login name in owner
        try:
         fileproject=open("project.txt",'a')
        except Exception as e:
         print(e)
        else:
         fileproject.write(urerifo)
         fileproject.close()
    elif a==2:
        try:
            fileproject = open("project.txt", 'r')
        except Exception as e:
            print(e)
        else:
            data=fileproject.read()
            print(data)
            fileproject.close()


    elif a==2:
        try:
            fileproject = open("project.txt", 'r')
        except Exception as e:
            print(e)
        else:
            data=fileproject.readlines()
            for data in fileproject:
                print(data)
            fileproject.close()
    else :
        word = input("enter your project name to delete ")
        fileobj = open("labn.txt", 'r')
        user = fileobj.readlines()
        fileobj = open("labn.txt", 'w')
        for u in user:
            x = u.strip('\n')
            if login != x[0] and l[1] != word:
                fileproject.write(u)

        # with open("yourfile.txt", "w") as f:
        #     for line in lines:
        #         if line.strip("\n") != "nickname_to_delete":
        #             f.write(line)
                    word=input("enter your project name to delete ")
                    fileobj = open("labn.txt", 'r')
                    user = fileobj.readlines()
                    print(user)
                    fileobj = open("labn.txt", 'w')
                    for u in user:
                        x = u.strip('\n')
                        l = x.split(":")
                        if login != l[0] and l[1]!=word:
                            fileproject.write(u)