from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from AddCustomer import AddCustmer
import Room_Status
from ShowCustomer import ShowCustmer
import addrooms, addempl, emplinfo, Checkout

class HotelManagementSystem:
    def __init__(self,root): 
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1520x900+0+0")

        self.left_frame = Frame(self.root,bg='white')
        self.left_frame.pack(fill=Y,side=LEFT)
        self.right_frame = Frame(self.root,bg='white')
        self.right_frame.pack(fill=BOTH)

        lbl_title=Label(self.right_frame,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",42,"bold"),bg="white",fg="black")
        lbl_title.pack()

        img1 = Image.open(r"Images\one.jpg")
        img1 = img1.resize((1230,750),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.interaction_frame = Frame(self.right_frame,bg='white')
        self.interaction_frame.pack(fill=BOTH)

        lblimg=Label(self.interaction_frame,image=self.photoimg1,bd=1,relief=RIDGE,bg='white')
        lblimg.pack()


        img2 = Image.open(r"Images\two.jpg")
        img2 = img2.resize((280,100),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg=Label(self.left_frame,image=self.photoimg2,bg='white')
        lblimg.pack()


        lbl_menu=Label(self.left_frame,text="MENU",font=("times new roman",20),bg="white",fg="black",bd=1)
        lbl_menu.pack()

        btn_frame=Frame(self.left_frame,bd=3,relief=RIDGE,bg='white')
        btn_frame.pack(fill=X)

        cust_btn=Button(btn_frame,text="ADD CUSTOMER",command=lambda: self.cust_details(),font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1")
        cust_btn.pack(fill=X)

        room_btn=Button(btn_frame,text="ADD ROOM",font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1",command=self.add_rooms)
        room_btn.pack(fill=X)

        employee_btn=Button(btn_frame,text="ADD EMPLOYEE",font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1",command=self.add_employee)
        employee_btn.pack(fill=X)

        showcustmr_btn=Button(btn_frame,text="CUSTOMER INFO",command=self.cust_info,font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1")
        showcustmr_btn.pack(fill=X)

        showemployee_btn=Button(btn_frame,text="EMPLOYEE INFO",font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1",command=self.empl_info)
        showemployee_btn.pack(fill=X)

        roomstatus_btn=Button(btn_frame,text="ROOM STATUS",font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1",command=lambda: self.room_info(self.interaction_frame))
        roomstatus_btn.pack(fill=X)

        checkout_btn=Button(btn_frame,text="CHECKOUT",font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1",command=self.checkout)
        checkout_btn.pack(fill=X)

        receipt_btn=Button(btn_frame,text="PRINT RECEIPT",font=("times new roman",18,"bold"),bg="black",fg="white",cursor="hand1")
        receipt_btn.pack(fill=X)
        

        
        img3 = Image.open(r"Images\three.jpg")
        img3 = img3.resize((250,210),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg=Label(self.left_frame,image=self.photoimg3,bg='white')
        lblimg.pack()

    def cust_details(self):
        # for x in win.winfo_children():
            # x.destroy()
        self.new_window=Toplevel(self.root)
        self.app=AddCustmer(self.new_window)

    def cust_info(self):
        self.window=Toplevel(self.root)
        self.app=ShowCustmer(self.window)
    
    def room_info(self,win):
        self.window=Toplevel(self.root)
        self.app=Room_Status.room_status(self.window)
    
    def add_rooms(self):
        self.window=Toplevel(self.root)
        self.app=addrooms.add_rooms(self.window)
    
    def add_employee(self):
        self.window=Toplevel(self.root)
        self.app=addempl.add_employee(self.window)
    
    def empl_info(self):
        self.window=Toplevel(self.root)
        self.app=emplinfo.EmployeeInfo(self.window)
    
    def checkout(self):
        self.window=Toplevel(self.root)
        self.app=Checkout.checkout(self.window)



if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()        

        
