import sqlite3
import sys
conn=sqlite3.connect(r'c:\II BCA_NEP\Database\NDRKFGC.db')
while 1:
    print("Welcome to Database operations on Tables")
    print("1--->Create Table")
    print("2--->Insert Data to Tables")
    print("3--->Delete the record from Table")
    print("4--->Display All the Records from Table")
    print("5--->Update Record")
    print("6--->Drop Table")
    print("7--->Exit")
    ch=int(input("Enter Your Choice"))

    if ch==1:
            conn.execute("Create table student(Student_Reg_Number INT,Student_Name VARCHAR(50),Student_Address VARCHAR(30))")
    elif ch==2:
            print("Enter Student_Register,Student_Name,Student_Address")
            stud_Reg=input()
            stud_Name=input()
            stud_Add=input()
            conn.execute("insert into student(Student_Reg_Number,Student_Name,Student_Address)values(?,?,?)",(stud_Reg,stud_Name,stud_Add))
            conn.commit()
            print('Records inserted successfully')
    elif ch==3:
            Stud_Reg=input("Enter student Register to delete the record")
            conn.execute("delete from student where Student_Reg_Number=?",(Stud_Reg,))
            conn.commit()
            print('Records Deleted Successfully')
    elif ch==4:
            print("***********Student All Records***********")
            data=conn.execute("select*from student")
            for row in data:
                print("student_Register=",row[0])
                print("Student_Name",row[1])
                print("Student_Address",row[2],"\n")
    elif ch==5:
            Stud_Reg=input("Enter Register number:")
            Stud_Address=input("Enter the address of student to update:")
            conn.execute("update student set Student_Address=?where Student_Reg_number=?",(Stud_Address,Stud_Reg))
    elif ch==6:
            conn.execute("DROP TABLE student")
    elif ch==7:
            sys.exit()
    else:
            break
conn.close()
      
            
            
    
