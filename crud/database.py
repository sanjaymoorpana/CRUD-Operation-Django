import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sk@516990",
    database = "sanjay",
)

mycursor = mydb.cursor()

#(CREATE TABLE QUERY)
# mycursor.execute("create table kenisha (name varchar(50), address varchar(50), email varchar(50),mobile varchar(50))")

#(INSERT QUERY MULTIPLE)
# sql = "insert into kenisha (name,address,email,mobile) values(%s,%s,%s,%s)"
# val = [
#     ("Sanjay Moorpana","Samor Residency","sjm@gmail.com",9769521250),
#     ("Kenisha Moorpana","Samor Residency","keny@gmail.com",9769739940),
#     ("Kayra Moorpana","Samor Residency","kayra@gmail.com",9769521250),
# ]

# mycursor.executemany(sql,val)
# mydb.commit()

#(SELECT QUERY)
# mycursor.execute("select * from kenisha")
# result = mycursor.fetchall()
# print(result)
# result1 = mycursor.fetchone()
# print(result1)

#(WHERE QUERY)
# sql = "select * from kenisha where name='sanjay moorpana'"
# mycursor.execute(sql)
# result = mycursor.fetchall()
# print(result)
