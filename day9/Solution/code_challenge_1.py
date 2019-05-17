# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:04:47 2019

@author: user
"""

import os
import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'db_University.db' )

c = conn.cursor()
#c.execute("DROP TABLE University;")

c.execute ("""CREATE TABLE University(
          Student_Name TEXT,
          Student_Age INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")

c.execute("INSERT INTO db_University VALUES ('Vishal Singh', 19, 123001, 'ML & AI')")
c.execute("INSERT INTO db_University VALUES ('Lavish Sharma', 20, 123002, 'ML & AI')")
c.execute("INSERT INTO db_University VALUES ('Dushyant Khichi', 19, 123003, 'ML & AI')")
c.execute("INSERT INTO db_University VALUES ('Ashwani Dhankar', 21, 123004, 'ML & AI')")
c.execute("INSERT INTO db_University VALUES ('Shubham Luxkar', 19, 123005, 'ML & AI')")
c.execute("INSERT INTO db_University VALUES ('Lakshya Jain', 20, 123006, 'ML & AI')")
c.execute("INSERT INTO db_University VALUES ('Neeshu Sharma', 19, 123007, 'ML & AI')")
c.execute("INSERT INTO db_University VALUES ('Ashif Khan', 20, 123008, 'ML & AI')")
c.execute("INSERT INTO db_University VALUES ('Lokesh Ladna', 20, 123009, 'ML & AI')")
c.execute("INSERT INTO db_University VALUES ('Dinesh Prajapat', 20, 123010, 'ML & AI')")

c.execute("SELECT * FROM db_University")

print ( c.fetchall() )

conn.commit()

conn.close()