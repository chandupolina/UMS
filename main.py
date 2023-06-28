from insert import inserted
from update  import updated
from delete import deleted
from read import readed
obj=inserted()
obj2=updated()
obj3=deleted()
obj4=readed()


print('---------------This is UMS project---------')
print("Welcome to the University Management System!")
print("Database Information:")
print("- Number of tables: 4")
print("- Table names: Student, Department, Faculty, Course")

# Displaying student table information
print("\nStudent Table Information:")
print("- Number of records: 4")
print("- Columns: sid, sname, courseid, dptid")

# Displaying department table information
print("\nDepartment Table Information:")
print("- Number of records: 2")
print("- Columns: departmentid, departmentname")

# Displaying faculty table information
print("\nFaculty Table Information:")
print("- Number of records: 5")
print("- Columns: facultyid, facultyname, departmentid, salary, courseid")

# Displaying course table information
print("\nCourse Table Information:")
print("- Number of records: 4")
print("- Columns: courseid, coursename, coursefees, duration")


print('---------------------')
print('for inserting data in department table press--1')
print('for inserting data in course table press--2')
print('for inserting data in student table press--3')
print('for inserting data in faculty table press--4')
print('---------------------')
print('for updating data in department table press--1')
print('for updating data in course table press--2')
print('for updating data in student table press--3')
print('for updating data in faculty table press--4')
print('---------------------')
print('for deleting data in department table press--1')
print('for deleting data in course table press--2')
print('for deleting data in student table press--3')
print('for deleting data in faculty table press--4')
print('---------------------')
print('for reading data in department table press--1')
print('for reading data in course table press--2')
print('for reading data in student table press--3')
print('for reading data in faculty table press--4')


print('----------------')
print("we have four operations:")
print("enter *add* to insert data",)
print("enter *update* to update data")
print("enter *delete* to delete data")
print("enter *read* to read data")
opr=input("enter the operation")
tab=int(input("please select your table by entering the number to do the given operation"))

if opr=='add' and tab==1:
    depid=int(input("please enter depid:"))
    depname=input("please enter department name:")
    obj.departmentinsert(depid,depname)
if opr=='add' and tab==2:
    courseid=int(input("please enter courseid:"))
    coursename=input("please enter course name:")
    coursefee=int(input("please enter the course fee:"))
    duration=int(input("please enter the duration:"))
    obj.courseinsert(courseid,coursename,coursefee,duration)
if opr=='add' and tab==3:
    sid=int(input("please enter  student id:"))
    studentname=input("please enter student name:")
    courseid=int(input("please enter the course id:"))
    depid=int(input("please enter the department id"))
    obj.studentinsert(sid,studentname,courseid,depid)
if opr=='add' and tab==4:
    facid=int(input("please enter facultyid:"))
    facname=input("please enter course name:")
    depid=int(input("please enter the deartment id:"))
    sal=int(input("please enter the salary:"))
    courid=int(input("please enter the course id"))
    obj.facultyinsert(facid,facname,depid,sal,courid)

        
if opr=='update' and tab==1:
    print("for updating the data in department table please  press 1")
    col=input("please enter colname:")
    new=input("please enter newvalue:")
    oldvalue=input("please enter oldvalue:")
    obj2.departmentupdate(col,new,oldvalue)
if opr=='update' and tab==2:
    print("for updating the data in course table please  press 2")
    col=input("please enter colname:")
    new=input("please enter newvalue:")
    oldvalue=input("please enter oldvalue:")
    obj2.courseupdate(col,new,oldvalue)
if opr=='update' and tab==3:
    print("for updating the data in student table please  press 3")
    col=input("please enter colname:")
    new=input("please enter newvalue:")
    oldvalue=input("please enter oldvalue:")
    obj2.studentupdate(col,new,oldvalue)
if opr=='update' and tab==4:
    print("for updating the data in faculty table please  press 4")
    col=input("please enter colname:")
    new=input("please enter newvalue:")
    oldvalue=input("please enter oldvalue:")
    obj2.facultyupdate(col,new,oldvalue)



if opr=='delete' and tab==1:
    print("for deleting the data in department table please  press 1")
    id=int(input("please enter the department_id:"))
    obj3.departmentdelete(id)
if opr=='delete' and tab==2:
    print("for deleting the data in course table please  press 2")
    id=int(input("please enter the course_id:"))
    obj3.coursedelete(id)
if opr=='delete' and tab==3:
    print("for deleting the data in student table please  press 3")
    id=int(input("please enter the student_id:"))
    obj3.studentdelete(id)
if opr=='delete' and tab==4:
    print("for deleting the data in faculty table please  press 4")
    id=int(input("please enter the faculty_id:"))
    obj3.facultydelete(id)



if opr=='read' and tab==1:
    print("for reading the data in department table please  press 1")
    id=input("please enter the column name:")
    val=input("please enter the value ")
    obj4.departmentread(id,val)
if opr=='read' and tab==2:
    print("for reading the data in course table please  press 2")
    id=input("please enter the column name:")
    val=input("please enter the value ")
    obj4.courseread(id,val)
if opr=='read' and tab==3:
    print("for reading the data in student table please  press 3")
    id=input("please enter the column name:")
    val=input("please enter the value ")
    obj4.studentread(id,val)
if opr=='read' and tab==4:
    print("for reading the data in faculty table please  press 4")
    id=input("please enter the column name:")
    val=input("please enter the value ")
    obj4.facultyread(id,val)


    
    

    