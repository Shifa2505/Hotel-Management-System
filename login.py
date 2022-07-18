from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import hotel

from hotel import HotelManagementSystem

def start_login(win):
    win.destroy()
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
     def __init__(self,root):
         self.root=root
         self.root.title("Login")
         self.root.geometry("1540x800+0+0")

         self.var_securityq=StringVar()
         self.var_securityA=StringVar()
         self.var_new_password=StringVar()
         self.bg=ImageTk.PhotoImage(file=r"Images\hotel_i2.png")
         lbl_bg=Label(self.root,image=self.bg)
         lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


         frame=Frame(self.root,bg="black")
         frame.place(x=550,y=150,width=450,height=500)


         i1=Image.open(r"Images\login.jpg")
         i1=i1.resize((100,100),Image.ANTIALIAS)
         self.photoimage1=ImageTk.PhotoImage(i1)
         lblimg1=Label(self.root,image=self.photoimage1,bg="black",borderwidth=0)
         lblimg1.place(x=730,y=180,width=100,height=100)

         get_str=Label(self.root,text="Get Started",font=("Times New Roman",25,"bold"),fg="white",bg="black")
         get_str.place(x=700,y=280)

         username=lbl=Label(self.root,text="Username",font=("Times New Roman",16,"bold"),fg="white",bg="black")
         username.place(x=630,y=330)
         self.txt_username=ttk.Entry(self.root,font=("Times New Roman",15,"bold",))
         self.txt_username.place(x=600,y=360,width=300)

         password=lbl=Label(self.root,text="Password",font=("Times New Roman",15,"bold"),fg="white",bg="black")
         password.place(x=630,y=400)
         self.txt_pass=ttk.Entry(self.root,show="*",font=("Times New Roman",15,"bold"))
         self.txt_pass.place(x=600,y=430,width=300)

         i2=Image.open(r"Images\login.jpg")
         i2=i2.resize((20,20),Image.ANTIALIAS)
         self.photoimage2=ImageTk.PhotoImage(i2)
         lblimg2=Label(self.root,image=self.photoimage2,bg="black",borderwidth=0)
         lblimg2.place(x=600,y=335,width=20,height=20)

         i3=Image.open(r"Images\lock.jpg")
         i3=i3.resize((20,20),Image.ANTIALIAS)
         self.photoimage3=ImageTk.PhotoImage(i3)
         lblimg3=Label(self.root,image=self.photoimage3,bg="black",borderwidth=0)
         lblimg3.place(x=600,y=405,width=20,height=20)

         loginbtn=Button(self.root,command=self.login,text="LOGIN",font=("times new roman",15,"bold"),bg="red",fg="white",bd=3,relief=RIDGE,activeforeground="white",activebackground="red")
         loginbtn.place(x=700,y=480,width=130,height=35)

         registerbtn=Button(self.root,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),bg="black",fg="white",borderwidth=0,activeforeground="white",activebackground="black")
         registerbtn.place(x=600,y=530,height=15)

         forgotpassbtn=Button(self.root,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),bg="black",fg="white",borderwidth=0,activeforeground="white",activebackground="black")
         forgotpassbtn.place(x=600,y=550,height=15)

     def register_window(self):
         for x in self.root.winfo_children():
             x.destroy()
        #  self.root.destroy()
        #  self.root = Tk()
        #  self.new_window=Toplevel(self.root)
         self.app=register(self.root)
    
     


     def login(self):
         print("function called")
         if (self.txt_username.get()=="" or self.txt_pass.get()==""):
             messagebox.showerror("error","All feilds required")
             print("abc")
         else:
             conn= sqlite3.connect('hotel_management.db')
             cursor = conn.cursor()
             query = 'select * from manager where username=? and password=?;'
             cursor.execute(query,[self.txt_username.get(),self.txt_pass.get()])
             result = cursor.fetchone()
            
             if result==None:
                messagebox.showerror("Error","Invalid username and password")
             else:
                 open_main=messagebox.askyesno("YesNo","Access only Admin")
                 if open_main>0:
                     for x in self.root.winfo_children():
                         x.destroy()
                    #  self.new_window=Toplevel(self.root)
                     self.app=HotelManagementSystem(self.root)
                 else:
                     if not open_main:
                         return
             conn.commit()
             conn.close()
     
     def reset_Pass(self):
         if self.combo_securityq.get()=="Select":
             messagebox.showerror("Error","Please select the security question")
             print("self")
         elif self.txt_securityA.get()=="":
             messagebox.showerror("Error","Please enter the security answer")
         elif self.txt_new_password.get()=="":
             messagebox.showerror("Error","Please enter the new password")
         else:
             conn= sqlite3.connect('hotel_management.db')
             cursor = conn.cursor()
             query = 'select * from manager where username=? and securityQ=? and securityA=?;'
             cursor.execute(query,[self.txt_username.get(),self.combo_securityq.get(),self.txt_securityA.get()])
             result = cursor.fetchone()

             if result==None:
                messagebox.showerror("Error","Please enter correct answer")
             else:
                 query=("update manager set password=? where username=?;")
                 cursor.execute(query,[self.txt_new_password.get(),self.txt_username.get()])
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Info","Your password has been reset,please login with new password")



            



     def forgot_password_window(self):
         if self.txt_username.get()=="":
             messagebox.showerror("Error","Please enter the username to reset password")  
         else:
             conn= sqlite3.connect('hotel_management.db')
             cursor = conn.cursor()
             print("cursor")
             query = 'select * from manager where username=?;'
             cursor.execute(query,[self.txt_username.get()])
             result = cursor.fetchone()

             if result==None:
                messagebox.showerror("Error","Please enter valid username")
             else:
                conn.close()
                self.root2=Toplevel(bg="black")
                self.root2.title("Forget Password")
                self.root2.geometry("450x500+550+150")
                l=Label(self.root2,text="Forget Password?!",font=("Times New Roman",25,"bold"),fg="Red",bg="black")
                l.place(x=0,y=0,relwidth=1)

                securityq=Label(self.root2,text="Select Security Question",font=("Times New Roman",16,"bold"),fg="white",bg="black")
                securityq.place(x=50,y=80)
                self.combo_securityq=ttk.Combobox(self.root2,textvariable=self.var_securityq,font=("Times New Roman",15,"bold",),state="readonly")
                self.combo_securityq["values"]=("select","Your birth place","Your pet name","your favourite food dish")
                self.combo_securityq.place(x=50,y=130,width=250)
                self.combo_securityq.current(0)

                securityA=Label(self.root2,text="Security Answer",font=("Times New Roman",16,"bold"),fg="white",bg="black")
                securityA.place(x=50,y=200)
                self.txt_securityA=ttk.Entry(self.root2,textvariable=self.var_securityA,font=("Times New Roman",15,"bold",))
                self.txt_securityA.place(x=50,y=250,width=250)

                new_password=Label(self.root2,text="New Password",font=("Times New Roman",16,"bold"),fg="white",bg="black")
                new_password.place(x=50,y=310)
                self.txt_new_password=ttk.Entry(self.root2,textvariable=self.var_new_password,font=("Times New Roman",15,"bold",))
                self.txt_new_password.place(x=50,y=360,width=250)

                btn=Button(self.root2,text="Reset Password",command=self.reset_Pass,font=("Times New Roman",16,"bold"),fg="Yellow",bg="red")
                btn.place(x=140,y=410)

                
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
         frame.place(x=400,y=30,width=700,height=750)

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
         b1=Button(image=self.photoimage2,bg="black",command=self.register_data,borderwidth=0,cursor="hand2",font=("Times New Roman",50,"bold"))
         b1.place(x=480,y=710,width=130)

         i3=Image.open(r"Images\login.png")
         i3=i3.resize((130,45),Image.ANTIALIAS)
         self.photoimage3=ImageTk.PhotoImage(i3)
         b2=Button(image=self.photoimage3,bg="black",borderwidth=0,cursor="hand2",font=("Times New Roman",45,"bold"),command=lambda: start_login(self.root))
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
                #  elif:
                #      query="select username from manager;"
                #      cursor.execute(query)
                #      result=cursor.fetchall()
                #      if result==[]:
                #          messagebox.showerror("Error","User already exist, Please try another email")

                 else:
                     print("entered else")
                     query="select id from cleaning union all select id from manager order by id desc;"
                     cursor.execute(query)
                     result=cursor.fetchone()
                     print(result)
                     sid=1
                     if (result!=None):
                         sid=result[0] + 1
                     cursor.execute("insert into manager(id,name,gender,phone,email,aadhar,DOB,shift,securityQ,securityA,username,password)"+
                                    " values(?,?,?,?,?,?,?,?,?,?,?,?);",(str(sid),self.var_name.get(),
                     self.var_gender.get(),self.var_mobile.get(),self.var_email.get(),self.var_aadhar.get(),self.var_DOB.get(),
                     self.var_shift.get(),self.var_securityq.get(),self.var_securityA.get(),self.var_username.get(),
                     self.var_password.get()))
                     messagebox.showinfo("Success","Register Successfully")
                 conn.commit()
                 conn.close()
             except Exception as e:
                 print(e)



                



# if __name__ =="__main__":
#     start_login()
