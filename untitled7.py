# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:08:21 2021

@author: ANYONE
"""

import csv
f=open("student.csv","w")
stuwriter=csv.writer(f)
#stuwriter.writerow["rollno.","name","marks"]
for i in range(1,4):
    r=int(input("enter rol no  "))
    n=input("enter a name  ")
    m=int(input("enter marks  "))
    srec=[r,n,m]
    stuwriter.writerow(srec)
f.close()