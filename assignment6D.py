#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:10:12 2024


Your boss calls you into a meeting. She tells you about a new project
that is about to begin. It needs a database back-end, and she would
like you to do some research to figure out which database is the best
solution. She says that the first phase of the project is just to test
feasibility, so they need a very simple, fast solution that doesn’t
need a lot of setup or special hardware/software to get going. It needs
to be cross platform but doesn’t require any special network access. She
says for the feasibility phase, only one user will be accessing the database 
from their computer. She says it needs to be easy to backup to a usb stick
so it can be copied from one computer to another. Cost is of utmost importance
during this first phase of this project. It’s ok if the database backend is
replaced with something else in later phases, once all the requirements have
been worked out. Oh, and one last thing, it needs to be compatible with
Python, since that’s what will be used throughout this project.

Given the above information, make a list of features (criteria) that are
important to your boss for this phase of the project. Rank how important
each criterion is, where 1 is not very important, and 5 is very important.
Show your criteria and the rank you assigned each one.

Evaluate the following databases against your criteria:

MSSQL
Oracle
SQLite
MySQL (or MariaDB)
PostgreSQL
Microsoft Access
LibreOffice Base
Rate each database against the criteria, where 0 means it doesn’t meet
the criteria at all, and 5 meets the criteria extremely well. Show your
rating for each database, against each criterion.

Multiply your numbers and add them up, just like the class example. Find
which database should work the best for this phase of the project and
state your findings.


@author: alexjuma
"""

import sqlite3

try:
    conn = sqlite3.connect('database_rank_final.sql')
    print('Database was opened sucessfully!')

except Exception as e:
    print('Error opening DB:',e)
 

try:
    c = conn.cursor()
    c.execute("""create table db_ranks
                 (id integer primary key autoincrement not null,
                  db_name text not null,
                  simplicity int not null,
                  speed int not null,
                  cross_platform int not null,
                  single_user int not null,
                  backup int not null,
                  cost int not null,
                  combatibility int not null);""")
    conn.commit()
    print('Table created successfully!')

except Exception as e:
    print("Error creating table:",e)
    
"""
USER CRITERIA ORDER OF IMPORTANCE

Simplicity of Setup and Use: 6
Speed: 7
Cross-Platform Compatibility: 5
Single User Access: 3
Easy Backup and Portability: 4
Cost: 2
Python Compatibility: 1
"""
    
user_criteria_rank = [6,7,5,3,4,2,1]
    
databases = [
    ('MSSQL', 2, 4, 1, 5, 2, 1, 3),
    ('Oracle', 2, 4, 2, 5, 2, 1, 3),
    ('SQLite', 5, 5, 5, 5, 5, 5, 5),
    ('MySQL', 4, 4, 4, 5, 4, 5, 5),
    ('PostgreSQL', 4, 4, 4, 5, 4, 5, 5),
    ('Microsoft Access', 5, 3, 2, 5, 5, 4, 2),
    ('LibreOffice Base', 4, 3, 4, 5, 4, 5, 3)
]  

try:
    sql = """insert into db_ranks (db_name,simplicity,speed,cross_platform,
             single_user,backup,cost,combatibility)
             values (?,?,?,?,?,?,?,?)"""
    #data = ('2018-05-24', 'Winnipeg, MB', -12.6, 10.2, 5.4)
    for data in databases:
        c.execute(sql, data)
    conn.commit()
    print("Added sample data successfully.")
    
except Exception as e:
    print("Error inserting sample data.", e)
    
try:
    # Add a new column named "Total" to the table
    c.execute("""alter table db_ranks add column Total int""")
    conn.commit()
    print('Column "Total" added successfully!')

except Exception as e:
    print("Error adding column:", e)

# Multiply each existing column by a certain value and update the "Total" column
try:
    c.execute(f"""update db_ranks 
             SET Total = simplicity * {user_criteria_rank[0]} + speed *
             {user_criteria_rank[1]} + cross_platform * {user_criteria_rank[2]}
             + single_user * {user_criteria_rank[3]} + backup *
             {user_criteria_rank[4]} + cost * {user_criteria_rank[5]} +
             combatibility * {user_criteria_rank[6]}""")
             
    conn.commit()
    print("Total column values updated successfully.")

except Exception as e:
    print("Error updating Total column:", e)
    
try:
    for row in c.execute("select * from db_ranks"):
        print(row)
except Exception as e:
    print("Error fetching sample data.", e)

conn.close()

#JUDGING BY THE CRITERIA GIVEN BY THE PROBLEM HOLDER, THE BEST DATABASE TO USE
#IS THE SQLITE DATABASE WITH A TOTAL SCORE OF SQLite. 
    
    



