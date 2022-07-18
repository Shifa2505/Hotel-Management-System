from tkinter import*
from tkinter.ttk import Labelframe
from turtle import bgcolor, st
# from winreg import REG_DWORD_LITTLE_ENDIAN
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import sqlite3 as sql3
from tkinter import messagebox

class ShowCustmer:
    def __init__(self,root): 
        self.root=root
        self.root.title("Show Customer Info")
        self.root.geometry("1240x750+280+100")
        self.root.config(bg="white")

        lbl_title=Label(self.root,text="CUSTOMER INFORMATION",font=("times new roman",30,"bold"),bg="white",fg="black")
        lbl_title.place(x=0,y=0,width=1240,height=40)

        img1 = Image.open(r"Images\five.jpg")
        img1 = img1.resize((600,500),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=1,relief=RIDGE)
        lblimg.place(x=750,y=60,width=500,height=600)

        Table_Frame=Labelframe(self.root,text="View Details and Search System",relief=RIDGE)
        Table_Frame.place(x=5,y=60,width=743,height=700)

        lbl_search=Label(Table_Frame,text="SEARCH BY:", font=("times new roman",15),padx=20)
        lbl_search.grid(row=0,column=0,sticky=W)
        self.search_opt=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_opt,font=("times new roman",15),width=20,state="readonly")
        combo_search["value"]=("Customer ID","Mobile Number")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)

        self.txtSearch=ttk.Entry(Table_Frame,font=("times new roman",15),width=22)
        self.txtSearch.grid(row=1,column=1,padx=20)

        search_btn=Button(Table_Frame,text="Search",width = 15,font=("times new roman",13,"bold"),bg="black",fg="white",cursor="hand1",command=self.search)
        search_btn.grid(row=0,column=2,pady=10,padx=10)

        showall_btn=Button(Table_Frame,text="Show All",width = 15,font=("times new roman",13,"bold"),bg="black",fg="white",cursor="hand1",command=self.show_all)
        showall_btn.grid(row=1,column=2,pady=10,padx=10)

        #data table
        info_frame=Frame(Table_Frame,bd=2,relief=RIDGE)
        info_frame.place(x=0,y=120,width=735,height=430)

        scroll_x=ttk.Scrollbar(info_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(info_frame,orient=HORIZONTAL)

        self.Show_Cust_Table=ttk.Treeview(info_frame,columns=("lbl_cust_id","name","gender","mobile","email","aadhar","check-in-date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=BOTTOM,fill=Y)

        scroll_x.config(command=self.Show_Cust_Table.xview)
        scroll_y.config(command=self.Show_Cust_Table.yview)

        self.Show_Cust_Table.heading("lbl_cust_id", text="Customer ID")
        self.Show_Cust_Table.heading("name", text="Customer Name")
        self.Show_Cust_Table.heading("gender", text="Gender")
        self.Show_Cust_Table.heading("mobile", text="Mobile Number")
        self.Show_Cust_Table.heading("email", text="Email")
        self.Show_Cust_Table.heading("aadhar", text="Aadhar")
        self.Show_Cust_Table.heading("check-in-date", text="Check-In-Date")

        self.Show_Cust_Table["show"]="headings"

        self.Show_Cust_Table.column("lbl_cust_id",width=120)
        self.Show_Cust_Table.column("name",width=120)
        self.Show_Cust_Table.column("gender",width=120)
        self.Show_Cust_Table.column("mobile",width=120)
        self.Show_Cust_Table.column("email",width=120)
        self.Show_Cust_Table.column("aadhar",width=120)
        self.Show_Cust_Table.column("check-in-date",width=120)

        self.Show_Cust_Table.pack(fill=BOTH,expand=1)

    def show_all(self):
        try:
            #clearing table
            for x in self.Show_Cust_Table.get_children():
                self.Show_Cust_Table.delete(x)

            #getting data
            conn=sql3.connect('hotel_management.db')
            cur=conn.cursor()
            query="select id,name,gender,phone_no,email,aadhar,entry_time from customer;"
            cur.execute(query)
            result=cur.fetchall()
            for x in result:
                self.Show_Cust_Table.insert("",'end',values=x)

            cur.close()
            conn.close()
        except Exception as e:
            print("error occured in displaying customres.")
            # print(e)
    
    def search(self):
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
                if(self.search_opt.get()=="Customer ID"):
                    # print("searching by cust_id")
                    query="select id,name,gender,phone_no,email,aadhar,entry_time from customer where id=?;"
                    cur.execute(query,(self.txtSearch.get(),))
                    result=cur.fetchall()
                else:
                    # print("searching by phone_no")
                    query="select id,name,gender,phone_no,email,aadhar,entry_time from customer where phone_no=?;"
                    cur.execute(query,(self.txtSearch.get(),))
                    result=cur.fetchall()
                for x in result:
                    self.Show_Cust_Table.insert("",'end',values=x)

                cur.close()
                conn.close()
            except Exception as e:
                # print("error occured in searching employees.")
                print(e)

if __name__ == "__main__":
    root=Tk()
    obj=ShowCustmer(root)
    root.mainloop()        
