import tkinter as tk
import tkinter.messagebox

def IT():
    root = tk.Tk()
    root.title('IT ACT 2000')
    root.geometry("350x210")

    def act1():
        tk.messagebox.showinfo("Tampering with source code documents","This Crime comes under Section 65 and the criminal is liable to pay compensation of the damages and has to serve 3 years of imprisonment or fine of 2,00,000rupees or both")
        
    def act2():
        tk.messagebox.showinfo("Hacking for malicious purposes","This Crime comes under Section 66 and the criminal is liable to serve 3 years of imprisonment or fine of 5,00,000rupees or both")
        
    def act3():
        tk.messagebox.showinfo("Breach of confidentiality and privacy","This Crime comes under Section 66 E and the criminal is liable to pay compensation of the damages and has to serve 3 years of imprisonment or fine of 2,00,000rupees or both")

    def act4():
        tk.messagebox.showinfo("Publication for fraud purposes","This Crime comes under Section 66 B,C,D and the criminal is liable to pay compensation of the damages and has to serve 3 years of imprisonment or fine of 1,00,000rupees or both")

    def act5():
        tk.messagebox.showinfo("Cyber Terrorism","This Crime comes under Section 66F affecting unity, integrity, security, sovereignty of India through digital medium is liable for life imprisonment.")

    def act6():
        tk.messagebox.showinfo("Publishing Obscene Information electronic form","This Crime comes under Section 67 and the criminal is liable to pay compensation of the damages and has to serve 5 years of imprisonment or fine of 10,00,000rupees or both")

    def act7():
        tk.messagebox.showinfo("Penalty for misrepresentation","This Crime comes under Section 71 and the criminal is liable to pay compensation of the damages and has to serve 2 years of imprisonment or fine of 1,00,000rupees or both")

    def act8():
        tk.messagebox.showinfo("Forging Digital Signature in certain particulars","This Crime comes under Section 73 and the criminal is liable to pay compensation of the damages and has to serve 2 years of imprisonment or fine of 1,00,000rupees or both")

    def act9():
        tk.messagebox.showinfo("Protected system","This Crime comes under Section 70 and the criminal is liable to pay compensation of the damages and has to serve 10 years of imprisonment along with the fine")


    tk.Button(root,text='Tampering with source code documents',width=40,command=act1).pack()
    tk.Button(root,text='Hacking for malicious purposes',width=40,command=act2).pack()
    tk.Button(root,text='Breach of confidentiality and privacy',width=40,command=act3).pack()
    tk.Button(root,text='Publication for fraud purposes',width=40,command=act4).pack()
    tk.Button(root,text='Cyber Terrorism',width=40,command=act5).pack()
    tk.Button(root,text='Publishing Obscene Information electronic form',width=40,command=act6).pack()
    tk.Button(root,text='Penalty for misrepresentation',width=40,command=act7).pack()
    tk.Button(root,text='Forging Digital Signature in certain particulars',width=40,command=act8).pack()
    tk.Button(root,text='Protected system',width=40,command=act9).pack()

    root.mainloop()
