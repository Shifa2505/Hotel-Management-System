from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image,ImageTk
import sqlite3 as sql3
from tkinter import messagebox
import hotel
class add_rooms:
    def __init__(self,root):
        self.root=root
        # root.title("ADD_ROOMS")
        self.root.geometry("500x500")
        self.root.configure(background='black')

        f1=Frame(self.root,bg='white',height=40, width=1)

        f1.place(anchor='center')
        f1.grid(row=0,column=0,padx=0,pady=0,ipadx=500,ipady=500)

        self.img1=Image.open(r"Images\r1.jpg")
        self.img1=self.img1.resize((500,500),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(self.img1)

        self.l4=Label(f1,image=self.photoimg1,bd=4,relief=RIDGE)
        # l4.image=photoimg1
        self.l4.place(x=0,y=0,width=500,height=500)


        #labelPryProt = Label(f1, text='Add Room',bg='white',fg='Black', font='Bold')
        #labelPryProt.config(font=("Bell Gothic Std Black", 22))
        #labelPryProt.pack()
        #label2 = Label(f1, text='',bg='#0d3c59',fg='Black', font='Bold')
        #label2.config(font=("Bell Gothic Std Black", 12))
        #label2.pack()

        #label3 = Label(f1, text='Floor NO',bg='white',fg='Black', font='Bold')
        #label3.config(font=("Bell Gothic Std Black", 12))
        #label3.pack()



        l2=Label(f1,text='ROOM NO:',bg='black',fg='white', font=('Times New Roman',15,BOLD))
        l2.grid(row=0,column=0,padx=20,pady=20)
        self.textbox2=Entry(f1,fg='black',font=(16))
        self.textbox2.grid(row=0,column=1)

        l1=Label(f1,text='Price:',bg='black',fg='white', font=('Times New Roman',15,BOLD))
        l1.grid(row=1,column=0,padx=20,pady=20)
        self.textbox=Entry(f1,fg='black',font=(16))
        self.textbox.grid(row=1,column=1)

        roomtype=["Single","Double","Master"]

        l3=Label(f1,text='ROOM TYPE:',bg='black',fg='white',font=('Times New Roman',15,BOLD))
        self.rtype=StringVar()
        l3.grid(row=2,column=0,padx=10,pady=10)
        cmb=ttk.Combobox(f1,text="select",value=roomtype,width=30,height=50,textvariable=self.rtype)
        cmb.grid(row=2,column=1,padx=10,pady=10,ipadx=5,ipady=5)

        cmb.current(0)
        #textbox=Entry(f1,fg='red',font=(16))
        #textbox.grid(row=2,column=1)
        b1 = Button(f1,fg="black",text="clear",width=15,command=self.clearBox,font=('Times New Roman',15,BOLD))
        b1.grid(row=3,column=1,padx=10,pady=10,ipadx=2,ipady=2)

        b2= Button(f1,fg="black",text="ADD",width=15,font=('Times New Roman',15,BOLD),command=lambda: self.add_room(self.textbox2.get(),self.rtype.get(),self.textbox.get()))
        b2.grid(row=3,column=0,padx=30,pady=30,ipadx=2,ipady=2)

        b3= Button(f1,fg="black",text="Exit",width=15,font=('Times New Roman',15,BOLD), command=self.Exit)
        b3.grid(row=4,column=0)
        self.root.mainloop()

    def clearBox(self):
        # textbox.delete('0',END)
        self.textbox2.delete('0',END)
        # cmb.delete('0',END)

    def Exit(self):
        self.root.destroy()
        # root=Tk()
        # obj=hotel.HotelManagementSystem(root)
        # root.mainloop()




    def add_room(self,no,type,price):
        try:
            conn=sql3.connect('hotel_management.db')
            cur=conn.cursor()
            query="insert into rooms (room_no,occupancy,category,price) values(?,NULL,?,?);"
            cur.execute(query,(int(no),str(type),float(price)))
            conn.commit()
            cur.close()
            conn.close()
            messagebox.showinfo(message="Room added.")
        except Exception as e:
            # print("Error in adding rooms")
            print(e)

        #ttk.Button(f1,text="cancel",command=clearBox(self)).grid(row=4,column=3)

