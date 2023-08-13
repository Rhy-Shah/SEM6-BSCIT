import tkinter as tk
from tkinter import *
root = Tk()
root.title('IT Act')
root.geometry('500x375')
import tkinter.messagebox

my_frame = Frame(root)

def update(data):
    my_listbox.delete(0,END)
    for item in data:
        my_listbox.insert(END,item)
        
def fillout(e):
    my_entry.delete(0,END)
    
    my_entry.insert(0,my_listbox.get(ACTIVE))
        
def check(e):
    typed = my_entry.get()
    if typed == '':
        data = sections
    else:
        data = []
        for item in sections:
            if typed.lower() in item.lower():
                data.append(item)   
    update(data)   
    
def delete():
    for i in my_listbox.curselection():
        sections.pop(i)
        punishments.pop(i)
    tk.messagebox.showinfo("","Deleted Successfully")
    my_listbox.delete(ANCHOR)
    
def insert():
    my_listbox.insert(END,entry.get())
    entry.delete(0,END)
    tk.messagebox.showinfo("","Add Successful")
    
def selected_item():
    for i in my_listbox.curselection():
        tk.messagebox.showinfo(sections[i],punishments[i])

global my_label
my_label = Label(my_frame,text = "The Information Technology Act, 2000",font = ("Helvetica",14),fg="black")
my_label.pack(pady=20)

my_entry = Entry(my_frame,font=("Hetletica",20))
my_entry.pack()

my_scrollbar = Scrollbar(my_frame,orient=VERTICAL)

my_listbox=Listbox(my_frame,width=50,yscrollcommand=my_scrollbar.set)
my_listbox.pack(pady=40)

my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT,fill=Y,pady=15)
my_frame.pack()
global sections
sections = ["Tampering with Documents",
            "Hacking",
            "Breach of Privacy",
            "Cyber Terrorism",
            "Publishing Obscene Data",
            "Misrepresentation",
            "Forging Digital Signature",
            "Breaching Protected System",
            "CyberBullying",
            "Downloading Torrent",
            "Uploading Pornography"]
update(sections)

global punishments
punishments = ["This Crime comes under Section 65 and the criminal is liable to pay compensation of the damages and has to serve 3 years of imprisonment or fine of 2,00,000 rupees or both",
               "This Crime comes under Section 66 and the criminal is liable to serve 3 years of imprisonment or fine of 5,00,000 rupees or both",
               "This Crime comes under Section 66 E and the criminal is liable to pay compensation of the damages and has to serve 3 years of imprisonment or fine of 2,00,000 rupees or both",
               "This Crime comes under Section 66F affecting unity, integrity, security, sovereignty of India through digital medium is liable for life imprisonment.",
               "This Crime comes under Section 67 and the criminal is liable to pay compensation of the damages and has to serve 5 years of imprisonment or fine of 10,00,000 rupees or both",
               "This Crime comes under Section 71 and the criminal is liable to pay compensation of the damages and has to serve 2 years of imprisonment or fine of 1,00,000 rupees or both",
               "This Crime comes under Section 73 and the criminal is liable to pay compensation of the damages and has to serve 2 years of imprisonment or fine of 1,00,000 rupees or both",
               "This Crime comes under Section 70 and the criminal is liable to pay compensation of the damages and has to serve 10 years of imprisonment along with the fine",
               "Section 66 E of IT Act and the criminal is liable to be punished with two years in prison",
               "Under this crime the criminal is liable to pay upto 250,000 rupees fine and up to five years in prison.",
               "This crime come under section 67A and the criminal is liable to pay up to 10 lakhs and has to serve upto 5 years in prison"]

my_listbox.bind("<<ListboxSelect>>",fillout)

get_value = Button(root,text="View Punishment",command=selected_item)
get_value.place(x=200,y=340)

del_button = Button(root,text='Delete',command = delete)
del_button.place(x=350,y=340)

entry = tk.Entry(root)
entry.place(x=100,y=315)

insert_button = Button(root,text='Add Law',command= insert)
insert_button.place(x=100,y=340)

my_entry.bind("<KeyRelease>",check)

root.mainloop()