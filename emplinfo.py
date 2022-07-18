from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import bgcolor,st 
from tkinter.ttk import Labelframe
from tkinter.font import BOLD
from turtle import width
from PIL import Image,ImageTk
import sqlite3 as sql3


class EmployeeInfo :
    def __init__(self,root):

        self.root=root
        self.root.title("EmployeeInfo")
        self.root.geometry("1240x750+280+100")
        self.root.config(bg="white")

        lbl_title=Label(self.root,text="EMPLOYEE INFORMATION",font=("times new roman",30,"bold"),bg="white",fg="black")
        lbl_title.place(x=0,y=0,width=1240,height=40)

        img1 =Image.open(r"Images\ef2.jpg")
        img1 =img1.resize((600,500),Image.ANTIALIAS)
        self.photoimg1 =ImageTk.PhotoImage(img1)
        lbling=Label(self.root,image=self.photoimg1,bd=1,relief=RIDGE)
        lbling.place(x=750,y=60,width=500,height=600)

        Table_Frame=Labelframe(self.root,text="View Details and Search System",relief=RIDGE)
        Table_Frame.place(x=5,y=60,width=743,height=700)


        lbl_search=Label(Table_Frame,text="SEARCH BY:", font=("times new roman",15),padx=20)
        lbl_search.grid(row=0,column=0,sticky=W)
        self.search_opt=StringVar()
        self.combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_opt,font=("times new roman",15),width=20,state="readonly")
        self.combo_search["value"]=("AADHAR NUMBER","Mobile Number")
        self.combo_search.current(0)
        self.combo_search.grid(row=0,column=1)


        self.txtSearch=ttk.Entry(Table_Frame,font=("times new roman",15),width=22)
        self.txtSearch.grid(row=1,column=1,padx=20)

        search_btn=Button(Table_Frame,text="Search",width = 15,font=("times new roman",13,"bold"),bg="black",fg="white",cursor="hand1",command=self.search_employee)
        search_btn.grid(row=0,column=2,pady=10,padx=10)


        showall_btn=Button(Table_Frame,text="Show All",width = 15,font=("times new roman",13,"bold"),bg="black",fg="white",cursor="hand1",command=self.display_all_employee)
        showall_btn.grid(row=1,column=2,pady=10,padx=10)

        
        #data table
        info_frame=Frame(Table_Frame,bd=2,relief=RIDGE)
        info_frame.place(x=0,y=120,width=735,height=430)

        scroll_x=ttk.Scrollbar(info_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(info_frame,orient=HORIZONTAL)

        self.Show_Cust_Table=ttk.Treeview(info_frame,columns=("NAME","AADHAR NO","Mobile","DOB","GENDER","SHIFT","POST"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=BOTTOM,fill=Y)

        scroll_x.config(command=self.Show_Cust_Table.xview)
        scroll_y.config(command=self.Show_Cust_Table.yview)

        self.Show_Cust_Table.heading("NAME", text="NAME")
        self.Show_Cust_Table.heading("AADHAR NO", text="AADHAR NO")
        self.Show_Cust_Table.heading("Mobile", text="Mobile number")
        # self.Show_Cust_Table.heading("Email", text="Email")
        self.Show_Cust_Table.heading("DOB", text="DOB")
        self.Show_Cust_Table.heading("GENDER", text="GENDER")
        self.Show_Cust_Table.heading("SHIFT", text="SHIFT")
        self.Show_Cust_Table.heading("POST", text="POST")

        self.Show_Cust_Table["show"]="headings"

        self.Show_Cust_Table.column("NAME",width=120)
        self.Show_Cust_Table.column("AADHAR NO",width=120)
        self.Show_Cust_Table.column("Mobile",width=120)
        # self.Show_Cust_Table.column("Email",width=120)
        self.Show_Cust_Table.column("DOB",width=120)
        self.Show_Cust_Table.column("GENDER",width=120)
        self.Show_Cust_Table.column("SHIFT",width=120)
        self.Show_Cust_Table.column("POST",width=120)

        self.Show_Cust_Table.pack(fill=BOTH,expand=1)
        
    def display_all_employee(self):
        try:
            #clearing table
            for x in self.Show_Cust_Table.get_children():
                self.Show_Cust_Table.delete(x)

            #getting data
            conn=sql3.connect('hotel_management.db')
            cur=conn.cursor()
            query="select name,aadhar,phone,dob,gender,shift,'Manager' from manager union all select name,aadhar,phone,dob,gender,shift,'Cleaning' from cleaning;"
            cur.execute(query)
            result=cur.fetchall()
            for x in result:
                self.Show_Cust_Table.insert("",'end',values=x)

            cur.close()
            conn.close()
        except Exception as e:
            print("error occured in displaying employees.")
            # print(e)
    
    def search_employee(self):
        if (self.txtSearch.get()==""):
            messagebox.showinfo(message="Please enter value to search for.")
        else:
            try:
                #clearing table
                for x in self.Show_Cust_Table.get_children():
                    self.Show_Cust_Table.delete(x)

                #getting data
                conn=sql3.connect('hotel_management.db')
                result=[]
                cur=conn.cursor()
                if(self.search_opt=="AADHAR NUMBER"):
                    query="select name,aadhar,phone,dob,gender,shift,'Manager' from manager where aadhar=? union all select name,aadhar,phone,dob,gender,shift,'Cleaning' from cleaning where aadhar=?;"
                    cur.execute(query,(self.txtSearch.get(),self.txtSearch.get()))
                    result=cur.fetchall()
                else:
                    query="select name,aadhar,phone,dob,gender,shift,'Manager' from manager where phone=? union all select name,aadhar,phone,dob,gender,shift,'Cleaning' from cleaning where phone=?;"
                    cur.execute(query,(self.txtSearch.get(),self.txtSearch.get()))
                    result=cur.fetchall()
                for x in result:
                    self.Show_Cust_Table.insert("",'end',values=x)

                cur.close()
                conn.close()
            except Exception as e:
                print("error occured in searching employees.")
                # print(e)




if __name__ =="__main__":
    root=Tk()
    obj=EmployeeInfo(root)
    root.mainloop()



