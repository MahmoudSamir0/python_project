def myTitle():
 while True:
   Title = input("enter Title of the project")
   if  Title.isspace()==True:
    continue
   else:
      return Title



def myDetails():
 while True:
   Details = input("enter Details of the project ")
   if  Details.isspace()==True:
    continue
   else:
      return Details




def Total_targe():
 while True:
   Total_targe = input("enter Total targe of the project ")
   if  Total_targe.isdigit()==False:
    continue
   else:
      return Total_targe+'EGP'

import datetime

def startdate():
 while True:
    day=input("enter start day of the project (number) ")
    month=input("enter start month of the project (number) ")
    year=input("enter start year of the project")
    if day.isdigit() == False and month.isdigit() == False and year.isdigit() == False:
        continue
    else:
        d = int(day)
        m = int(month)
        y = int(year)
        x = datetime.date(y, m, d)
        return x


def enddate():
 while True:
    da=input("enter end day of the project (number) ")
    mont=input("enter end month of the project (number) ")
    yea=input("enter end year of the project")
    if da.isdigit() == False and mont.isdigit() == False and yea.isdigit() == False:
        continue
    else:
        d = int(da)
        m = int(mont)
        y = int(yea)
        gg = datetime.date(y, m, d)
        return gg

def myowner():
 while True:
   owner = input("enter your name")
   if  owner.isspace()==True:
    continue
   else:
      return owner