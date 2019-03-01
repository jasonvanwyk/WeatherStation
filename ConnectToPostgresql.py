#!/usr/bin/python
# -*- coding: utf-8 -*-

#added this coment to test git
 
import psycopg2
#import sys comented out this line to test git
import datetime
import time
import random
import serial


con = None
 
for loop in range(0,10):
    try:
        x = random.randint(1,101)
        t = datetime.datetime.now() 
        con = psycopg2.connect("host='localhost' dbname='Jason' user='postgres' password='S0nd3l@1'")   
        cur = con.cursor()
        #cur.execute("INSERT INTO tempdata VALUES(now(), %(x))")
        cur.execute("INSERT INTO tempdata VALUES (%s, %s)", (x, t,))
        con.commit()

     
    finally:   
        if con:
            con.close()

    print(x) 
    time.sleep(1)
# copyright 2019
