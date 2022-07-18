from email import message
from pdb import post_mortem
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import Image,ImageTk
import sqlite3 as sql3
import hotel
class add_employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1240x750+280+100")
        self.root.title("Add Employee")
        # self.root.configure(background='#0d3c59')
        self.root.config(bg="white")
       


        #f1=Frame(self.root,bg='#0d3c59',height=40, width=1,highlightbackground='#0d3c59',highlightthicknes=1)
        #1.place(anchor='center')
        #f1.grid(row=0,column=0,padx=120,pady=120,ipadx=120,ipady=120)
        self.f2=Frame(self.root,bg="white")
        
        # self.f2.place(x=0,y=0,width=500,height=500)


        self.f2=Frame(self.root,height=40, width=1)

        # self.f2.place(anchor='center')
        self.f2.grid(row=0,column=0,padx=0,pady=0,ipadx=500,ipady=500)


        img1=Image.open(r"Images\e1.jpg")
        img1=img1.resize((300,500),Image.ANTIALIAS)
        photoimg1=ImageTk.PhotoImage(img1)

        l4=Label(self.root,image=photoimg1,bd=4,relief=RIDGE)
        l4.place(x=730,y=40,width=300,height=500)

        l1=Label(self.f2,text='ADD EMPLOYEE',fg='Black', font=("times new roman",30,"bold"))
        l1.grid(row=0,column=1,padx=10,pady=10)
        #=================NAME====================
        l2=Label(self.f2,text='Employee Name:',fg='black', font=("times new roman",20,"bold"))
        l2.grid(row=3,column=0,padx=10,pady=10)
        self.textbox1=Entry(self.f2,fg='black',font=(16))
        self.textbox1.grid(row=3,column=1)
        # #=================ADHAR====================

        l2=Label(self.f2,text='Aadhar Number:',fg='black',font=("times new roman",20,"bold"),padx=15,pady=15)
        l2.grid(row=5,column=0,padx=10,pady=10)
        self.textbox2=Entry(self.f2,fg='black',font=(16))
        self.textbox2.grid(row=5,column=1)


        #=================DOB====================
        l3=Label(self.f2,text='DOB:',fg='black',font=("times new roman",20,"bold"),padx=15,pady=15)
        l3.grid(row=7,column=0,padx=10,pady=10)
        self.textbox3=Entry(self.f2,fg='black',font=(16))
        self.textbox3.grid(row=7,column=1)
        # #=================PHONE====================
        l4=Label(self.f2,text='Phone Number:',fg='black', font=("times new roman",20,"bold"),padx=15,pady=15)
        l4.grid(row=9,column=0,padx=10,pady=10)
        self.textbox4=Entry(self.f2,fg='black',font=(16))
        self.textbox4.grid(row=9,column=1)


        g=["Male","Female","Other"]
        # #=================GENDER====================
        l5=Label(self.f2,text='Gender:',fg='black', font=("times new roman",20,"bold"),padx=15,pady=15)
        l5.grid(row=11,column=0,padx=10,pady=10)
        self.gender=StringVar()
        self.cmb=ttk.Combobox(self.f2,text="select1",textvariable=self.gender,value=g,width=32,)
        self.cmb.grid(row=11,column=1,ipadx=5,ipady=5)
        self.cmb.current(0)
        # =================SHIFT====================
        S=["Day Time","Night Time"]
        l6=Label(self.f2,text='Shift:',fg='black', font=("times new roman",20,"bold"),padx=15,pady=15)
        l6.grid(row=13,column=0,padx=10,pady=10)
        self.shift=StringVar()
        self.cmb1=ttk.Combobox(self.f2,text="select3",textvariable=self.shift,value=S,width=32,height=50)
        self.cmb1.grid(row=13,column=1,ipadx=5,ipady=5)
        self.cmb1.current(0)
        #=================POST====================

        # post=["MANAGER","CLEANING"]
        # l7=Label(self.f2,text='POST :',fg='white',bg='black',font=('Times New Roman',15,BOLD))
        # l7.grid(row=15,column=0,padx=10,pady=10)
        # cmb2=ttk.Combobox(self.f2,text="select2",value=post,width=30,)
        # cmb2.grid(row=15,column=1,ipadx=5,ipady=5)
        # cmb2.current(0)



        b1 = Button(self.f2,fg="white",bg="black",text="CLEAR",width=15,font=('Times New Roman',15,BOLD),command=self.clearBox)
        b1.grid(row=17,column=1,padx=1,pady=1,ipadx=1,ipady=1)

        b2= Button(self.f2,command=self.addem,fg="white",bg="black",text="ADD",width=15,font=('Times New Roman',15,BOLD))
        b2.grid(row=17,column=0)

        b3= Button(self.f2,fg="white",bg="black",text="CANCEL",width=15,font=('Times New Roman',15,BOLD), command=self.Exit)
        b3.grid(row=17,column=3)


        self.root.mainloop()

    def clearBox(self):
        self.textbox1.delete('0',END);
        self.textbox2.delete('0',END);
        self.textbox3.delete('0',END);
        self.textbox4.delete('0',END);

        # self.cmb.delete('0',END)
        # self.cmb1.delete('0',END)
        # cmb2.delete('0',END)

    def Exit(self):
        self.root.destroy()
        # root=Tk()
        # obj=hotel.HotelManagementSystem(root)
        # root.mainloop()

    def addem(self):
        if self.textbox1.get()=="" or self.textbox3.get()=="":
            messagebox.showerror("Error","all fields are required")
        else:
            try:
                conn=sql3.connect("hotel_management.db")
                cur=conn.cursor()

                # insertion code here
                query="select id from cleaning union all select id from manager order by id desc;"
                cur.execute(query)
                result=cur.fetchone()
                sid=1
                if (result!=None):
                    sid=result[0] + 1
                query = "insert into cleaning values(?,?,?,?,?,?,?);"
                cur.execute(query,(str(sid),self.textbox2.get(),self.textbox1.get(),self.textbox4.get(),self.shift.get(),self.gender.get(),self.textbox3.get()))

                conn.commit()
                cur.close()
                conn.close()
                messagebox.showinfo(message="Cleaning staff added.")
            except Exception as e:
                # print("Error in adding staff.")
                print(e)