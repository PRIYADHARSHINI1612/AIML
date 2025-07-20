#!/usr/bin/env python
# coding: utf-8

# In[24]:


pip install mysql-connector-python


# In[25]:


import mysql.connector


# In[29]:


mydb = mysql.connector.connect(
    host='localhost',
    port='330',
    user='root',
    password='Priya#321',
    database='employee_jupyter'
)

print(mydb)


# In[30]:


cursor = mydb.cursor()


# In[31]:


sql = "CREATE DATABASE employee"


# In[32]:


sql = """
CREATE TABLE salary (
    empid INT,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    email VARCHAR(50),
    phone VARCHAR(15),
    hire_date DATE,
    job_id VARCHAR(15),
    salary INT
)
"""


# In[33]:


cursor.execute(sql)


# In[36]:


import csv
import datetime
filename = r"C:\Users\priya\OneDrive\Documents\employees1.csv"


# In[37]:


with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    a = next(csvreader)  # Skip header
    for row in csvreader:
        print(row)
        empid = int(row[0])
        firstname = row[1]
        lastname = row[2]
        email = row[3]
        phone = row[4]
        hire_date = datetime.datetime.strptime(row[5], '%d-%b-%y').date()
        job_id = row[6]
        salary = int(row[7])  # Or: int(row[7][:-3]) if it includes "000" like "50000.00"

        sql = """INSERT INTO salary
        (empid, firstname, lastname, email, phone, hire_date, job_id, salary)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        val = (empid, firstname, lastname, email, phone, hire_date, job_id, salary)
        cursor.execute(sql, val)

mydb.commit()
print("Data inserted successfully.")


# In[38]:


import os
print(os.getcwd())


# In[39]:


get_ipython().system('jupyter nbconvert --to script SQL-Database.ipynb')


# In[ ]:




