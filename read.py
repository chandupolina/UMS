import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='sai123'
)
cur=conn.cursor()
class readed:
    def departmentread(x,colname,value):
        cur.execute(f"select * from department where {colname}={value}")
        print(cur.fetchall())
        print("Data  read successfully")
    def courseread(x,colname,value):
        cur.execute(f"select * from  course where {colname}={value}")
        print(cur.fetchall())
        print("Data  read successfully")
    def studentread(x,colname,value):
        cur.execute(f"select * from student where {colname}={value}")
        print(cur.fetchall())
        print("Data  read successfully")
    def facultyread(x,colname,value):
        cur.execute(f"select * from department where {colname}={value}")
        print(cur.fetchall())
        print("Data  read successfully")