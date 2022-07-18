from tkinter import *
import login
from PIL import Image,ImageTk

class HotelManagementSystem:
    def __init__(self,root):
     self.root=root
     self.root.title("Hotel Management System")
     self.root.geometry("600x350+430+230")


     i1= Image.open(r"Images\hotel.jpg")
     i1=i1.resize((600,350),Image.ANTIALIAS)
     self.photoi1=ImageTk.PhotoImage(i1)

     lblimg=Label(self.root,image=self.photoi1,bd=4,relief=RIDGE)
     lblimg.place(x=0,y=0,width=600,height=350)

     lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
     lbl_title.place(x=30, y=260,width=530, height=40)

     b1=Button(text="NEXT",font=("Times New Roman",12,"bold"),cursor="hand2",borderwidth=0,bg="white",fg="black",command=lambda: login.start_login(self.root))
     b1.place(x=500,y=310,width=70)






if __name__ =="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()