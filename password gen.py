import random
import pyperclip
from tkinter import *
from tkinter.ttk import*


def low():
          entry.delete(0, END)
          length = varl.get()
          lower="abcdefghijklmnopqrstuvwxys"
          upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 
          digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabodefghijklmnopqrstuvwxyz123456789@#$%^&O"
          password=""
          if var.get()==1:
               for i in range(0, length):
                    password=password + random.choice(lower)
               return password
          elif var.get()==0:
                for i in range(0, length):
                     password = password + random.choice(upper)
                return password
          elif var.get() == 3:
                for i in range(0, length):
                     password=password + random.choice(digits)
                return password 
          else:
               print("Please choose an option")
def generate():
    password1 = low()
    entry.insert(10, password1)
def copy1(): 
    random_password = entry.get()
    Pyperclip.copy(random_password)
root = Tk()
root.geometry("500x200")
font1=("Arial",10,"bold")
var = IntVar()
varl = IntVar()
root.title("Random Pamword Generator")
Random_password =Label(root, text="Password")
Random_password.grid(row=0)
entry=Entry(root)
entry.grid(row=0, column=1)
c_label = Label(root, text="Length")
c_label.grid(row=1)
copy_button=Button(root, text="Copy", command=copy1) 
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)
combo = Combobox(root, textvariable=varl)
combo['value']=(8, 9, 10, 11, 12, 13, 14, 15, 16,
                17, 18, 19, 20, 21, 22, 23, 24, 25, 
                26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0) 
combo.bind("<<ComboboxSelected>>")
combo.grid(column=1, row=1)
root.mainloop()
