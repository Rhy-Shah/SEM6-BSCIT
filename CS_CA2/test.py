from tkinter import *
root = Tk()
root.geometry('180x200')

listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)
listbox.insert(1, "Data Structure")
listbox.insert(2, "Algorithm")
listbox.insert(3, "Data Science")
listbox.insert(4, "Machine Learning")
listbox.insert(5, "Blockchain")

def selected_item():
	for i in listbox.curselection():
		print(listbox.get(i))
  
btn = Button(root, text='Print Selected', command=selected_item)

btn.pack(side='bottom')
listbox.pack()
root.mainloop()
