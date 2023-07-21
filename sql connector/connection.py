import mysql.connector

mydb=mysql.connector.connect(host='localhost', user='root',password='av@py2/ramsan')

# print(mydb)

mycursor=mydb.cursor()

# mycursor.execute("create database MYdb_Python")
#
mycursor.execute("use Mydb_Python")
# mycursor.execute("create table employee( name varchar(250),dept varchar(250),salary int)")
# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)

# sql="insert into employee values('jack','python',10000)"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="insert into employee (name,dept,salary) values (%s,%s,%s)"
#
# val=[
#     ('sandra','python',25000),
#     ('sourag', 'java', 30000),
#     ('sayanth','.net',25000)
#
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")
# mycursor.execute("select * from employee")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)
# #
# myresult = mycursor.fetchone()
# print(myresult)
# sql="update employee set name='sayooj'where name='sayanth'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# sql="select * from employee order by name asc"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)


# sql="select * from employee order by name desc"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)
# #

# sql='select distinct dept from employee'
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)
#
# sql='select count(distinct dept) from employee'
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)
# mycursor.execute("select * from employee ")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

# mycursor.execute("create table person_info(id int,name varchar(250),age int,contact varchar(10),place varchar(250))")

sql="insert into person_info(id,name,age,contact,place) values (%s,%s,%s,%s,%s)"

val=[
    (1,'sourav',25,7025023544,'kannur'),
    (2,'ameya',12,8796541230,'idukki'),
    (3,'sandra',24,8593899578,'wayanad'),
    (4,'ramsan',10,9685741425,'ernakulam')
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")