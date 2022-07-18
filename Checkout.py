import tkinter as tk
import Manav_func as func

class checkout:
    def __init__(self,win):
        # Temporarily creating a window
        self.root=win

        # now the header
        lbl_checkout=tk.Label(self.root, text="Checkout", font=("Segoe Script",20), bg="#01030e", fg="#e31d16")
        lbl_checkout.pack(fill=tk.X)
        # checkoutImg = tk.PhotoImage(file="checkoutImg.png")
        # lbl_img = tk.Label(root,image=checkoutImg,bg="#01030e")
        # lbl_img.pack(fill=tk.X)

        # Starting with the frame
        self.frm_checkout = tk.Frame(self.root, bg="#01030e")
        self.frm_checkout.pack(fill="both",expand=True,side=tk.LEFT)

        img_lbl = tk.PhotoImage(file="Images\checkout_image.png")
        lbl_img = tk.Label(self.root,image=img_lbl,bg="#01030e")
        lbl_img.pack(side=tk.RIGHT,fill=tk.BOTH)

        #creating the labels to be displayed and dropdown list to be selected from
        lbl_1 = tk.Label(self.frm_checkout,text="Customer ID", bg="#01030e",fg="#79c0ec",font=("Helvetica",15,"bold"))
        lbl_1.grid(row=0,column=0)
        lbl_2 = tk.Label(self.frm_checkout,text="Name", bg="#01030e",fg="#79c0ec",font=("Helvetica",15,"bold"))
        lbl_2.grid(row=1,column=0)
        lbl_3 = tk.Label(self.frm_checkout,text="Phone", bg="#01030e",fg="#79c0ec",font=("Helvetica",15,"bold"))
        lbl_3.grid(row=2,column=0)
        lbl_4 = tk.Label(self.frm_checkout,text="Aadhar", bg="#01030e",fg="#79c0ec",font=("Helvetica",15,"bold"))
        lbl_4.grid(row=3,column=0)
        lbl_5 = tk.Label(self.frm_checkout,text="Gender", bg="#01030e",fg="#79c0ec",font=("Helvetica",15,"bold"))
        lbl_5.grid(row=4,column=0)
        lbl_6 = tk.Label(self.frm_checkout,text="Check-In Date & Time", bg="#01030e",fg="#79c0ec",font=("Helvetica",15,"bold"))
        lbl_6.grid(row=5,column=0)
        selected_customer=tk.StringVar()
        selected_customer.set("Select a customer ID")
        lbl_7 = tk.Label(self.frm_checkout,text="-", bg="#01030e",fg="yellow",font=(15))
        lbl_7.grid(row=1,column=1)
        lbl_8 = tk.Label(self.frm_checkout,text="-", bg="#01030e",fg="yellow",font=(15))
        lbl_8.grid(row=2,column=1)
        lbl_9 = tk.Label(self.frm_checkout,text="-", bg="#01030e",fg="yellow",font=(15))
        lbl_9.grid(row=3,column=1)
        lbl_10 = tk.Label(self.frm_checkout,text="-", bg="#01030e",fg="yellow",font=(15))
        lbl_10.grid(row=4,column=1)
        lbl_11 = tk.Label(self.frm_checkout,text="-", bg="#01030e",fg="yellow",font=(15))
        lbl_11.grid(row=5,column=1)
        optn_1 = tk.OptionMenu(self.frm_checkout,selected_customer,*func.list_customers(), command=lambda x: func.fetch_customer_details(selected_customer,lbl_7,lbl_8,lbl_9,lbl_10,lbl_11))
        optn_1.config(bg="#0a1e8f",fg="yellow")
        optn_1.grid(row=0,column=1,sticky="nsew")
        # img_btn = tk.PhotoImage(file="checkButton.png")
        # btn_chk = tk.Button(self.frm_checkout,text="",image=img_btn,command=lambda : func.fetch_customer_details(selected_customer,lbl_7,lbl_8,lbl_9,lbl_10,lbl_11))
        # btn_chk.grid(row=0,column=2)

        # Adding the next button
        # img_btn = tk.PhotoImage(file="nextButton.png")
        btn_next = tk.Button(self.frm_checkout,text="Next",bg="#01030e", fg="yellow",command=lambda: func.perform_checkout(self.frm_checkout,selected_customer.get()),font=(15))
        btn_next.grid(row=6,column=1,sticky="nsew")
        btn_next.bind("<Enter>", lambda x:btn_next.config(bg="#030b34"))
        btn_next.bind("<Leave>", lambda x:btn_next.config(bg="#01030e"))

        for i in range(6):
            self.frm_checkout.rowconfigure(i,weight=1)
        self.frm_checkout.columnconfigure(0,weight=1)
        self.frm_checkout.columnconfigure(1,weight=1)


        self.root.mainloop()