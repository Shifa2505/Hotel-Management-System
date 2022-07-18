# This frame is used to display the Occupied/Empty/All rooms.

import tkinter as tk
import Manav_func as func
class room_status:
    def __init__(self,win):
        self.root=win
        self.root.title("Room Status")
        # Creating a Tkinter frame to hold everything to be displayed by room_status
        self.frm_room_status = tk.Frame(self.root,bg="#01030e") # do not forget to place the correct master window
        self.frm_room_status.pack(fill=tk.BOTH)

        # Label to indicate we are on Room Status page
        self.lbl_room_status=tk.Label(self.frm_room_status, text="Room Status", font=("Helvetica",20), bg="#01030e", fg="#e31d16")
        self.lbl_room_status.pack(fill=tk.X)

        # Checkboxes to select display category
        self.selected_option = tk.StringVar()
        self.selected_option.set("All")
        # Frame to hold selection options
        self.frm_select_room = tk.Frame(self.frm_room_status, bg="#01030e")
        self.frm_select_room.pack(fill=tk.X)
        self.chb_occupied=tk.Radiobutton(self.frm_select_room, text="Occupied", variable=self.selected_option, value="Occupied", bg="#01030e", fg="#0099ff", font=(14),command=lambda : func.create_room_table(frm_table,self.selected_option))
        self.chb_empty=tk.Radiobutton(self.frm_select_room, text="Empty", variable=self.selected_option, value="Empty", bg="#01030e", fg="#0099ff", font=(14),command=lambda : func.create_room_table(frm_table,self.selected_option))
        self.chb_all=tk.Radiobutton(self.frm_select_room, text="All", variable=self.selected_option, value="All", bg="#01030e", fg="#0099ff", font=(14),command=lambda : func.create_room_table(frm_table,self.selected_option))
        self.chb_occupied.pack(side=tk.LEFT)
        self.chb_empty.pack(side=tk.LEFT)
        self.chb_all.pack(side=tk.LEFT)

        # Creating a Frame to display the Table within a canvas within outer frame
        outerframe = tk.Frame(self.root,bg='#01030e')
        outerframe.pack(fill=tk.X)
        outerframe.columnconfigure(0,weight=1)
        canvas = tk.Canvas(outerframe,background="#01030e",scrollregion=(0,0,500,500),highlightthickness=0,width=450)
        frm_table = tk.Frame(canvas, bg="#01030e")
        func.create_room_table(frm_table,self.selected_option)
        # frm_table.pack(fill=tk.X)
        sb=tk.Scrollbar(outerframe)
        sb.pack(side=tk.RIGHT,fill=tk.Y)
        canvas.pack(side=tk.LEFT,expand=True)
        canvas.create_window(0,0,anchor=tk.NW,window=frm_table)
        sb.config(command=canvas.yview)
        canvas.config(yscrollcommand=sb.set)
        self.root.mainloop()
