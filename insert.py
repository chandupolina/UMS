import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='sai123'
)
cur=conn.cursor()
class inserted:
    def departmentinsert(x,department_id,department_name):
        cur.execute(f"insert into department values({department_id},'{department_name}')")
        conn.commit()
        print("data is inserted successfully")
    def courseinsert(x,course_id,course_name,course_fee,duration):
        cur.execute(f"insert into course values({course_id},'{course_name}',{course_fee},{duration})")
        conn.commit()
        print("Data is inserted successfully")
    def facultyinsert(x,faculty_id,faculty_name,department_id,salary,course_id):
        cur.execute(f"insert into faculty values({faculty_id},'{faculty_name}',{department_id},{salary},{course_id})")
        conn.commit()
        print("Data is inserted successfully")
    def studentinsert(x,student_id,student_name,course_id,department_id):
        cur.execute(f"insert into student values({student_id},'{student_name}',{course_id},{department_id})")
        conn.commit()
        print("Data is inserted successfully")
    
