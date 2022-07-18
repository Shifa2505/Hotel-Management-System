from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

class register:
     def __init__(self,root):
         self.root=root
         self.root.title("Register")
         self.root.geometry("1540x800+0+0")

         self.var_name=StringVar()
         self.var_gender=StringVar()
         self.var_mobile=StringVar()
         self.var_email=StringVar()
         self.var_aadhar=StringVar()
         self.var_DOB=StringVar()
         self.var_shift=StringVar()
         self.var_securityq=StringVar()
         self.var_securityA=StringVar()
         self.var_username=StringVar()
         self.var_password=StringVar()
         self.var_conf_password=StringVar()

         self.bg=ImageTk.PhotoImage(file=r"Images\hotel_i2.jpg")
         lbl_bg=Label(self.root,image=self.bg)
         lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

         frame=Frame(self.root,bg="black")
         frame.place(x=420,y=30,width=700,height=750)

         register_lbl=Label(text="!!! REGISTER HERE !!!",font=("Times New Roman",20,"bold"),fg="red",bg="black")
         register_lbl.place(x=620,y=60)

         i1=Image.open(r"Images\register-removebg-preview.png")
         i1=i1.resize((300,450),Image.ANTIALIAS)
         self.photoimage1=ImageTk.PhotoImage(i1)
         lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
         lblimg1.place(x=800,y=130,width=300,height=550)

         name=Label(text="Name",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         name.place(x=450,y=110)
         name_entry=ttk.Entry(textvariable=self.var_name,font=("Times New Roman",15,"bold",))
         name_entry.place(x=650,y=110,width=200)

         gender=Label(text="Gender",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         gender.place(x=450,y=160)
         self.combo_gender=ttk.Combobox(textvariable=self.var_gender,font=("Times New Roman",15,"bold",),state="readonly")
         self.combo_gender["values"]=("select","Male","Female")
         self.combo_gender.place(x=650,y=160,width=200)
         self.combo_gender.current(0)

         mobile=Label(text="Mobile No",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         mobile.place(x=450,y=210)
         self.txt_contact=ttk.Entry(textvariable=self.var_mobile,font=("Times New Roman",15,"bold",))
         self.txt_contact.place(x=650,y=210,width=200)

         email=Label(text="Email",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         email.place(x=450,y=260)
         self.txt_email=ttk.Entry(textvariable=self.var_email,font=("Times New Roman",15,"bold",))
         self.txt_email.place(x=650,y=260,width=200)

         aadhar=Label(text="Aadhar No",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         aadhar.place(x=450,y=310)
         self.txt_aadhar=ttk.Entry(textvariable=self.var_aadhar,font=("Times New Roman",15,"bold",))
         self.txt_aadhar.place(x=650,y=310,width=200)

         DOB=Label(text="Date Of Birth",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         DOB.place(x=450,y=360)
         DOB_entry=ttk.Entry(textvariable=self.var_DOB,font=("Times New Roman",15,"bold",))
         DOB_entry.place(x=650,y=360,width=200)

         shift=Label(text="Shift",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         shift.place(x=450,y=410)
         self.combo_shift=ttk.Combobox(textvariable=self.var_shift,font=("Times New Roman",15,"bold",),state="readonly")
         self.combo_shift["values"]=("select","Day Time","Night Time")
         self.combo_shift.place(x=650,y=410,width=200)
         self.combo_shift.current(0)

         securityq=Label(text="Security Question",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         securityq.place(x=450,y=460)
         self.combo_securityq=ttk.Combobox(textvariable=self.var_securityq,font=("Times New Roman",15,"bold",),state="readonly")
         self.combo_securityq["values"]=("select","Your birth place","Your pet name","your favourite food dish")
         self.combo_securityq.place(x=650,y=460,width=200)
         self.combo_securityq.current(0)

         securityA=Label(text="Security Answer",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         securityA.place(x=450,y=510)
         self.txt_securityA=ttk.Entry(textvariable=self.var_securityA,font=("Times New Roman",15,"bold",))
         self.txt_securityA.place(x=650,y=510,width=200)

         username=Label(text="Username",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         username.place(x=450,y=560)
         self.txt_username=ttk.Entry(textvariable=self.var_username,font=("Times New Roman",15,"bold",))
         self.txt_username.place(x=650,y=560,width=200)

         password=Label(text="Password",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         password.place(x=450,y=610)
         self.txt_password=ttk.Entry(textvariable=self.var_password,font=("Times New Roman",15,"bold",))
         self.txt_password.place(x=650,y=610,width=200)

         conf_password=Label(text="Confirm Password",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         conf_password.place(x=450,y=660)
         self.txt_conf_password=ttk.Entry(textvariable=self.var_conf_password,font=("Times New Roman",15,"bold",))
         self.txt_conf_password.place(x=650,y=660,width=200)

         i2=Image.open(r"Images\register_now.png")
         i2=i2.resize((130,50),Image.ANTIALIAS)
         self.photoimage2=ImageTk.PhotoImage(i2)
         b1=Button(image=self.photoimage2,bg="black",command=self.register_data(),borderwidth=0,cursor="hand2",font=("Times New Roman",50,"bold"))
         b1.place(x=480,y=710,width=130)

         i3=Image.open(r"Images\login.png")
         i3=i3.resize((130,45),Image.ANTIALIAS)
         self.photoimage3=ImageTk.PhotoImage(i3)
         b2=Button(image=self.photoimage3,bg="black",command=self.login_window,borderwidth=0,cursor="hand2",font=("Times New Roman",45,"bold"))
         b2.place(x=700,y=710,width=130)

     def register_data(self):
         if self.var_name.get()=="" or self.var_aadhar.get()=="" or self.var_password.get()=="":
             messagebox.showerror("Error","All Fields Are Required")
         elif self.var_password.get()!=self.var_conf_password.get():
             messagebox.showerror("Error","Password and Confirm Password must be same") 
         else:
             try:
        
                 conn= sqlite3.connect('hotel_management.db')
                 cursor = conn.cursor()
                 query = 'select * from manager where email=?;'
                 print(self.var_email.get())
                 cursor.execute(query,[self.var_email.get()])
                 print("executed")
                 result = cursor.fetchone()
                 print("abc")
                 if result!=None:
                   messagebox.showerror("Error","User already exist, Please try another email")
                 else:
                     print("entered else")
                     cursor.execute("insert into manager(name,gender,phone,email,aadhar,DOB,shift,sec_Q,sec_A,username,password) values(?,?,?,?,?,?,?,?,?,?,?);",(self.var_name.get(),
                     self.var_gender.get(),self.var_mobile.get(),self.var_email.get(),self.var_aadhar.get(),self.var_DOB.get(),
                     self.var_shift.get(),self.var_securityq.get(),self.var_securityA.get(),self.var_username.get(),
                     self.var_password.get()))
                     messagebox.showinfo("Success","Register Successfully")
                 conn.commit()
                 conn.close()
             except Exception as e:
                 print(e)











      
      
      

  



if __name__ =="__main__":
    root=Tk()
    app=register(root)
    root.mainloop()  
