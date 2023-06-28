import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='sai123'
)
cur=conn.cursor()
class updated:
    def departmentupdate(x,colname,newvalue,oldvalue):
        cur.execute(f"update department set {colname}='{newvalue}' where {colname}='{oldvalue}'")
        conn.commit()
        print("Data is updated successfully")
    def courseupdate(x,colname,newvalue,oldvalue):
        cur.execute(f"update course set {colname}='{newvalue}' where {colname}='{oldvalue}'")
        conn.commit()
        print("Data is updated successfully")
    def facultyupdate(x,colname,newvalue,oldvalue):
        cur.execute(f"update faculty set {colname}='{newvalue}' where {colname}='{oldvalue}'")
        conn.commit()
        print("Data is updated successfully")
    def stdentupdate(x,colname,newvalue,oldvalue):
        cur.execute(f"update student set {colname}='{newvalue}' where {colname}='{oldvalue}'")
        conn.commit()
        print("Data is updated successfully")