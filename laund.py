
import customtkinter as ctk 
import tkinter as tk 
import pyglet as pg 
import random, datetime
from PIL import Image, ImageTk


pg.font.add_file("Inter-Black.ttf")
count = 0
nrow = 1
c = 3
row_con = 2
class GUI:
    
    def __init__(self):
        
        self.colors = ["060047", "B3005E", "E90064", "FF5F9E"]
        self.btns = [{"name":"shirt", "num" : 0},{"name":"pants", "num" : 0},{"name":"uniform", "num" : 0}]
        self.ref = []
        self.root = ctk.CTk()
        



        self.root.title("Laundry App V.1")
        self.row = 0
        self.root.geometry("700x500")

        
        
        self.root.columnconfigure(0, weight =1 )
        self.root.columnconfigure(1, weight = 1)
        self.root.columnconfigure(2, weight = 1)

        self.root.rowconfigure(0, weight = 1)
        self.root.rowconfigure(1, weight = 3)

        self.frame = ctk.CTkScrollableFrame(self.root, fg_color="#FFECD6")
        self.frame.grid(row = 1, columnspan= 3, sticky="nswe")

        self.frame.columnconfigure(0, weight = 1)
        self.frame.columnconfigure(1, weight = 1)

        self.frame.rowconfigure(0, weight = 1)
        self.frame.rowconfigure(1, weight = 1)

        self.entry = ctk.CTkEntry(self.root, 
                    width = 250,
                    placeholder_text= "Enter new item",
                    placeholder_text_color= "grey",
                    )
        self.entry.grid(row = 0, columnspan = 2)
        self.entry.bind("<KeyPress>", self.check)

        self.donebtn = ctk.CTkButton(self.root, 
                                     text = "Done",
                                     command=self.save)
        self.donebtn.grid(row = 0, column = 2)
        self.add_new()

        self.root.mainloop()

    def add_new(self):
        global count
        count = 0
        row = 0
        for i in range(len(self.btns)):
            if count %2 == 0 and count != 0:
                row +=1
                
            col= self.get_pos(i)    
            
            self.ref.append(ctk.CTkButton(self.frame, 
            text= f"{self.btns[i]['name'].upper()} : {self.btns[i]['num']}", 
            font = ("inter black", 30), command = lambda i =i : self.add_quant(i, self.btns),
            width = 250, height = 30, fg_color = "#0F2167", corner_radius=20
            ))
            self.ref[i].grid(row = row, column = col)
            count += 1
            
            
    
    def get_pos(self, i):
        
        
        if i == 0 or i%2 == 0:
            col = 0
        else:
            col = 1 
        
        return col
    
    def check(self, event):
        global c
        
        if event.keycode == 13:
            self.new = self.entry.get()
            self.add_btn(self.new, c, self.btns)
            self.entry.delete(0, tk.END)
            c += 1
            
            

    def add_btn(self, n, i, d):
        global count
        global nrow
        global row_con

        if count %2 == 0 and count != 0:
            nrow +=1
        

        d.append({"name":str(n), "num":0})
        col = self.get_pos(i)

        if col == 1:
            self.frame.rowconfigure(row_con, weight = 1)
            row_con += 1

        self.ref.append(ctk.CTkButton(self.frame, 
                    text= f"{self.btns[i]['name'].upper()} : {self.btns[i]['num']}", 
                    font = ("inter black", 30),
                    width = 250,
                    fg_color= "#0F2167",
                    height= 30, 
                    corner_radius=20, 
                    command = lambda i =i : self.add_quant(i, self.btns)))
        self.ref[c].grid(row = nrow, column = col)
        count += 1
        
    def add_quant(self, n, d):
        d[n]["num"] += 1
        self.ref[n].configure(text =f"{self.btns[n]['name'].upper()} : {self.btns[n]['num']}" )

    def color(self):
        return "#" + random.choice(self.colors)
    
    def save(self):
        with open("laundry.txt", "w") as file:
            file.write(datetime.date.today().strftime("%B %d, %Y\n"))
            for item in self.btns:
                if item["num"] == 0:
                    continue
                file.write(f"{item['name']}:{item['num']}\n")
            
        self.root.destroy()
            
        

GUI()