from email import message
from gettext import Catalog
import sqlite3
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Labelframe
from turtle import bgcolor, st
# from winreg import REG_DWORD_LITTLE_ENDIAN
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import sqlite3


class AddCustmer:
    def __init__(self,root): 
        # root=Tk()
        self.root=root
        self.root.title("Add Customer")
        self.root.geometry("1240x750+280+100")
        self.root.config(bg="white")

        lbl_title=Label(self.root,text="ADD CUSTOMER",font=("times new roman",30,"bold"),bg="white",fg="black")
        lbl_title.place(x=0,y=0,width=1240,height=40)
        
        img1 = Image.open(r"Images\custmr.jpg")
        img1 = img1.resize((600,600),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=1,relief=RIDGE)
        lblimg.place(x=630,y=59,width=600,height=600)

        labelframeleft=Labelframe(self.root,text="Customer Details",relief=RIDGE)
        labelframeleft.place(x=5,y=60,width=620,height=700)
        

        # #customer ID
        # lbl_cust_id=Label(labelframeleft,text="Customer ID:", font=("times new roman",20,"bold"),padx=15,pady=15)
        # lbl_cust_id.grid(row=0,column=0,sticky=W)
        

        #customer name
        cname=Label(labelframeleft,text="Customer Name:", font=("times new roman",20,"bold"),padx=15,pady=15)
        cname.grid(row=0,column=0,sticky=W)
        self.entry_name=ttk.Entry(labelframeleft,font=("times new roman",20),width=25)
        self.entry_name.grid(row=0,column=1)

        #gender Combobox
        lbl_gender=Label(labelframeleft,text="Gender:", font=("times new roman",20,"bold"),padx=15,pady=15)
        lbl_gender.grid(row=1,column=0,sticky=W)
        self.gender_opt=StringVar()
        self.combo_gender=ttk.Combobox(labelframeleft,font=("times new roman",20),width=24,state="readonly",textvariable=self.gender_opt)
        self.combo_gender["value"]=("M","F","O")
        self.combo_gender.current(0)
        self.combo_gender.grid(row=1,column=1)

        #Mobile Number
        mobile=Label(labelframeleft,text="Mobile Number:", font=("times new roman",20,"bold"),padx=15,pady=15)
        mobile.grid(row=2,column=0,sticky=W)
        self.entry_mobile=ttk.Entry(labelframeleft,font=("times new roman",20),width=25)
        self.entry_mobile.grid(row=2,column=1)

        #email
        mail=Label(labelframeleft,text="Email:", font=("times new roman",20,"bold"),padx=15,pady=15)
        mail.grid(row=3,column=0,sticky=W)
        self.entry_mail=ttk.Entry(labelframeleft,font=("times new roman",20),width=25)
        self.entry_mail.grid(row=3,column=1)

        #aadhar
        aadhar=Label(labelframeleft,text="Aadhar Number:", font=("times new roman",20,"bold"),padx=15,pady=15)
        aadhar.grid(row=4,column=0,sticky=W)
        self.entry_aadhar=ttk.Entry(labelframeleft,font=("times new roman",20),width=25)
        self.entry_aadhar.grid(row=4,column=1)

        #check-in-date
        check_in=Label(labelframeleft,text="Check-In-Date:", font=("times new roman",20,"bold"),padx=15,pady=15)
        check_in.grid(row=5,column=0,sticky=W)

        #room type
        cat=StringVar()
        lbl_room=Label(labelframeleft,text="Room Type:", font=("times new roman",20,"bold"),padx=15,pady=15)
        lbl_room.grid(row=6,column=0,sticky=W)
        self.combo_room=ttk.Combobox(labelframeleft,font=("times new roman",20),textvariable=cat,width=24,state="readonly")
        self.combo_room["value"]=("Single","Double","Master")
        self.combo_room.current(0)
        self.combo_room.grid(row=6,column=1)
        


        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=460,width=610,height=60)

        add_btn=Button(btn_frame,text="ADD",command=lambda: self.find_room(cat.get()),width = 20,font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1")
        add_btn.grid(row=0,column=0,pady=1,padx=10)

        cancel_btn=Button(btn_frame,text="CANCEL",width = 20,font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1",command=lambda:self.root.destroy())
        cancel_btn.grid(row=0,column=1,pady=5)


    def find_room(self,category):
        query='select room_no from rooms where occupancy is NULL and category=?;'
        try:
            #okayss
            conn=sqlite3.connect("hotel_management.db")
            cur=conn.cursor()
            cur.execute(query,(category,))
            print("query done")

            result=cur.fetchone()
            room_no=None
            if(result!=None):
                print(result)
                room_no=result[0]
                cid=1
                query="select id from customer order by id desc;"
                cur.execute(query)
                result=cur.fetchone()
                if(result!=None):
                    cid=result[0]+1
                query="insert into customer(id,name,gender,phone_no,email,aadhar,entry_time) values(?,?,?,?,?,?,datetime('now','localtime'));"
                cur.execute(query,(str(cid),self.entry_name.get(),self.gender_opt.get(),self.entry_mobile.get(),self.entry_mail.get(),self.entry_aadhar.get()))
                query="update rooms set occupancy=? where room_no=?;"
                cur.execute(query,(str(cid),str(room_no)))
                conn.commit()
                messagebox.showinfo(message="New Customer Added.")
                self.root.destroy()

            else:
                messagebox.showinfo(title=None,message="No rooms available")
                # print("No rooms available")
            cur.close()
            conn.close()
            # messagebox.showinfo(message="New Customer Added.")
           
    
        except Exception as e:
            print(e)



if __name__ == "__main__":
    root=Tk()
    obj=AddCustmer(root)
    root.mainloop()        
