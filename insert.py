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
    day=input("enter start day ")
    month=input("enter start month ")
    year=input("enter start year ")
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
    da=input("enter end day ")
    mont=input("enter end month ")
    yea=input("enter end year ")
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