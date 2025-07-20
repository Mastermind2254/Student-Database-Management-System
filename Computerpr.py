import mysql.connector as my
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.geometry("750x615")
root.title("Student management system")
db=my.connect(host="localhost",user="root", password="Doge2254")
cr=db.cursor()
cr.execute("create database if not exists school")
cr.execute("use school")
l=[]
for i in range(6,13):
    l.append("student"+str(i))
    d="create table if not exists student{0}(Regn_no int, Name char(50), Class int, Roll_no int, Mobile_no bigint)".format(i,)
    cr.execute(d)    
def stu_rec():
    cr.reset()
    frame.after(10)
    t=Toplevel()
    t.geometry("640x400")
    frame1=Frame(t,width=640,height=640)
    frame1.pack()
    l=Label(frame1,text="Enter the registration number").pack(anchor="w")
    e=Entry(frame1,width=50)
    e.pack(anchor="e")
    l1=Label(frame1,text="Enter the name").pack(anchor="w")
    e1=Entry(frame1,width=50)
    e1.pack(anchor="e")
    l2=Label(frame1,text="Enter the class").pack(anchor="w")
    e2=Entry(frame1,width=50)
    e2.pack(anchor="e")
    l3=Label(frame1,text="Enter the roll number").pack(anchor="w")
    e3=Entry(frame1,width=50)
    e3.pack(anchor="e")
    l4=Label(frame1,text="Enter the mobile number").pack(anchor="w")
    e4=Entry(frame1,width=50)
    e4.pack(anchor="e")
    bt=Button(frame1,text="Submit",command=lambda: add_db(e,e1,e2,e3,e4,t)).pack(anchor="center")
def add_db(e,e1,e2,e3,e4,t):
    cr.reset()
    l=[]
    for i in range(6,13):
        tu=(i,e.get())
        z="Select * from Student%s where Regn_no=%s"
        cr.execute(z,tu)
        x=cr.fetchone()
        if x!=None:
            l=list(x)                
    if not l:        
        x="insert into student%s values(%s,%s,%s,%s,%s)"
        cr.execute(x,(int(e2.get()),int(e.get()),str(e1.get()),int(e2.get()),int(e3.get()),int(e4.get())))
        db.commit()
        t.after(10,t.destroy())
    else:
        res=messagebox.showerror("Student entry","Regn no. already taken!")   
def stu_edit(y):
    y.after(10,y.destroy())
    frame.after(10)
    t=Toplevel()
    t.geometry("640x400")
    frame1=Frame(t,width=640,height=640)
    frame1.pack()
    l=Label(frame1,text="Enter the registration number").pack(anchor="w")
    e=Entry(frame1,width=50)
    e.pack(anchor="e")
    l1=Label(frame1,text="Check the fields you want to edit:").pack(anchor=W)
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    ch1=Checkbutton(frame1,text="Regn No.",variable=var1)
    ch1.pack(anchor=W)
    ch2=Checkbutton(frame1,text="Name",variable=var2)
    ch2.pack(anchor=W)
    ch3=Checkbutton(frame1,text="Class",variable=var3)
    ch3.pack(anchor=W)
    ch4=Checkbutton(frame1,text="Roll No.",variable=var4)
    ch4.pack(anchor=W)
    ch5=Checkbutton(frame1,text="Mobile No.",variable=var5)
    ch5.pack(anchor=W)
    bt=Button(frame1,text="Submit",command=lambda: edit_db(e,t,var1,var2,var3,var4,var5)).pack(anchor="center")
def edit_db(e,t,v1,v2,v3,v4,v5):
    cr.reset()
    for i in range(6,13):
        tu=(i,e.get())
        z="Select * from Student%s where Regn_no=%s"
        cr.execute(z,tu)
        x=cr.fetchone()
        if x!=None:
            l=list(x)
    m=e.get()        
    t.after(10,t.destroy())
    t1=Toplevel()
    t1.geometry("640x400")
    frame1=Frame(t1,width=640,height=640)
    frame1.pack()
    if v1.get()==1:
        l1=Label(frame1,text="Enter the new registration number").pack(anchor="w")
        e1=Entry(frame1,width=50)
        e1.pack(anchor="e")
    else:
        e1=""
    if v2.get()==1:
        l2=Label(frame1,text="Enter the new name").pack(anchor="w")
        e2=Entry(frame1,width=50)
        e2.pack(anchor="e")
    else:
        e2=""    
    if v3.get()==1:
        l3=Label(frame1,text="Enter the new class").pack(anchor="w")
        e3=Entry(frame1,width=50)
        e3.pack(anchor="e")
    else:
        e3=""    
    if v4.get()==1:
        l4=Label(frame1,text="Enter the new roll no.").pack(anchor="w")
        e4=Entry(frame1,width=50)
        e4.pack(anchor="e")
    else:
        e4=""    
    if v5.get()==1:
        l5=Label(frame1,text="Enter the new phone no.").pack(anchor="w")
        e5=Entry(frame1,width=50)
        e5.pack(anchor="e")
    else:
        e5=""        
    bt=Button(frame1,text="Submit",command=lambda: editt(m,t1,e1,e2,e3,e4,e5,v1,v2,v3,v4,v5,l)).pack(anchor="center")
def editt(m,t1,e1,e2,e3,e4,e5,v1,v2,v3,v4,v5,l):
    if v1.get()==1:
        l[0]=e1.get()    
    if v2.get()==1:
        l[1]=e2.get()
    if v3.get()==1:
        x="Delete from Student%s where Regn_no=%s"
        cr.execute(x,(l[2],m))
        l[2]=e3.get()
    if v4.get()==1:
        l[3]=e4.get()
    if v5.get()==1:
        l[4]=e5.get()
    t1.after(10,t1.destroy())
    if v3.get()==0:
        x1="Update Student%s set Regn_no=%s where Regn_no=%s"
        x2="Update Student%s set Name=%s where Regn_no=%s"
        x3="Update Student%s set Class=%s where Regn_no=%s"
        x4="Update Student%s set Roll_no=%s where Regn_no=%s"
        x5="Update Student%s set Mobile_no=%s where Regn_no=%s"
        cr.execute(x1,(l[2],l[0],m))
        cr.execute(x2,(l[2],l[1],m))
        cr.execute(x3,(l[2],l[2],m))
        cr.execute(x4,(l[2],l[3],m))
        cr.execute(x5,(l[2],l[4],m))
        db.commit()
    if v3.get()==1:
        x="insert into Student%s values(%s,%s,%s,%s,%s)"
        cr.execute(x,(int(l[2]),int(l[0]),l[1],int(l[2]),int(l[3]),int(l[4])))
        db.commit()                 
def stu_see():
    cr.reset()
    frame.after(10)
    t=Toplevel()
    t.geometry("640x480")
    frame1=Frame(t,width=1200,height=1200)
    frame1.pack()
    tr=ttk.Treeview(frame1)
    tr["columns"]=("Regn No.","Name","Class","Roll No.","Mobile no.")
    tr.column("#0",width=0)
    tr.column("Regn No.",width=120,anchor=W)
    tr.column("Name",anchor=W,width=120)
    tr.column("Class",anchor=CENTER,width=120)
    tr.column("Roll No.",anchor=CENTER,width=120)
    tr.column("Mobile no.",anchor=E,width=120)
    tr.heading("#0",text="",anchor=W)
    tr.heading("Regn No.",text="Regn No.",anchor=W)
    tr.heading("Name",text="Name",anchor=W)
    tr.heading("Class",text="Class",anchor=CENTER)
    tr.heading("Roll No.",text="Roll No.",anchor=CENTER)
    tr.heading("Mobile no.",text="Mobile No.",anchor=E)
    x=0
    ln=[0,0,0,0,0,0,0]
    for i in range(6,13):
        tu=(i,)
        z="Select * from Student%s"
        cr.execute(z,tu)
        ln[i-6]=cr.fetchall()
    for i in ln:    
        for j in i:     
            tr.insert(parent='',index='end',iid=x,text="",values=j)
            x+=1
    tr.pack()   
def stu_del():
    frame.after(10)
    t=Toplevel()
    t.geometry("640x400")
    frame1=Frame(t,width=640,height=640)
    frame1.pack()
    l=Label(frame1,text="Enter the registration number").pack(anchor="w")
    e=Entry(frame1,width=50)
    e.pack(anchor="e") 
    bt=Button(frame1,text="Submit",command=lambda: del_db(t,e)).pack(anchor="center")
def del_db(t,e):
    cr.reset()
    for i in range(6,13):
        tu=(i,e.get())
        z="Select * from Student%s where Regn_no=%s"
        cr.execute(z,tu)
        x=cr.fetchone()
        if x!=None:
            l=list(x)
    x="Delete from Student%s where Regn_no=%s"
    cr.execute(x,(l[2],e.get()))
    db.commit()
    t.after(10,t.destroy())
def stu_sear():
    frame.after(10)
    t=Toplevel()
    t.geometry("640x400")
    frame1=Frame(t,width=640,height=640)
    frame1.pack()
    l=Label(frame1,text="Enter the registration number").pack(anchor="w")
    e=Entry(frame1,width=50)
    e.pack(anchor="e") 
    bt=Button(frame1,text="Submit",command=lambda: sear_db(t,e)).pack(anchor="center")
def sear_db(t,e):
    cr.reset()
    for i in range(6,13):
        tu=(i,e.get())
        z="Select * from Student%s where Regn_no=%s"
        cr.execute(z,tu)
        x=cr.fetchone()
        if x!=None:
            l=list(x)
    t.after(10,t.destroy())
    t1=Toplevel()
    t1.geometry("1000x500")
    frame1=Frame(t1,width=1000,height=600)
    frame1.pack()
    l1=Label(frame1,text="------------------------------------------------------------------------------------",font=("System",35)).pack(anchor=CENTER)
    l2=Label(frame1,text="Regn No.:"+str(l[0]),font=("System",15)).pack(anchor=CENTER)
    l3=Label(frame1,text="------------------------------------------------------------------------------------",font=("System",35)).pack(anchor=CENTER)
    l5=Label(frame1,text="Name:"+str(l[1]),font=("System",15)).pack(anchor=CENTER)
    l6=Label(frame1,text="------------------------------------------------------------------------------------",font=("System",35)).pack(anchor=CENTER)
    l8=Label(frame1,text="Class:"+str(l[2]),font=("System",15)).pack(anchor=CENTER)
    l7=Label(frame1,text="------------------------------------------------------------------------------------",font=("System",35)).pack(anchor=CENTER)
    l9=Label(frame1,text="Roll No.:"+str(l[3]),font=("System",15)).pack(anchor=CENTER)
    l4=Label(frame1,text="------------------------------------------------------------------------------------",font=("System",35)).pack(anchor=CENTER)
    l=Label(frame1,text="Mobile No.:"+str(l[4]),font=("System",15)).pack(anchor=CENTER)
    ll=Label(frame1,text="------------------------------------------------------------------------------------",font=("System",35)).pack(anchor=CENTER)
    b6=Button(frame1,text="Edit profile",command=lambda: stu_edit(t1)).pack(anchor="center")        
frame=Frame(root,width=750,height=670)
frame.pack()
t1=Frame(root)
btn1=Button(frame,text="Enter student records",height=7,width=110,relief=RAISED,bg="#55c2da",command=stu_rec).place(x=0,y=0)
btn2=Button(frame,text="Edit student records",height=7,width=110,relief=RAISED,bg="#55c2da",command=lambda: stu_edit(t1)).place(x=0,y=100)
btn3=Button(frame,text="View student records",height=7,width=110,relief=RAISED,bg="#55c2da",command=stu_see).place(x=0,y=200)
bt4=Button(frame,text="Delete student records",height=7,width=110,relief=RAISED,bg="#55c2da",command=stu_del).place(x=0,y=300)
bt4=Button(frame,text="Search for student records",height=7,width=110,relief=RAISED,bg="#55c2da",command=stu_sear).place(x=0,y=400)
btn=Button(frame,text="Exit",height=7,width=110,relief=RAISED,bg="#55c2da",command=root.destroy).place(x=0,y=500)
root.mainloop()