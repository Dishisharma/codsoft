import tkinter
import tkinter.messagebox
root=tkinter.Tk()
root.title("Calculator")
root.geometry("250x350")

equation = ""
def show(value):
    global equation 
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        
        try:
            result= eval(equation)
        except:
            result ="error"
            equation =""
            print(result)
        label_result.config(text=result)


label_result=tkinter.Label(root,bg="black",fg="white")
label_result.place(x=20,y=20,height="50",width="200")

b9=tkinter.Button(root,text=("9"),height="2",width="4",command=lambda : show("9"))
b9.place(x=30,y=80)
b8=tkinter.Button(root,text=("8"),height="2",width="4",command=lambda : show("8"))
b8.place(x=70,y=80)
b7=tkinter.Button(root,text=("7"),height="2",width="4",command=lambda : show("7"))
b7.place(x=110,y=80)
b6=tkinter.Button(root,text=("6"),height="2",width="4",command=lambda : show("6"))
b6.place(x=30,y=130)
b5=tkinter.Button(root,text=("5"),height="2",width="4",command=lambda : show("5"))
b5.place(x=70,y=130)
b4=tkinter.Button(root,text=("4"),height="2",width="4",command=lambda : show("4"))
b4.place(x=110,y=130)
b3=tkinter.Button(root,text=("3"),height="2",width="4",command=lambda : show("3"))
b3.place(x=30,y=180)
b2=tkinter.Button(root,text=("2"),height="2",width="4",command=lambda : show("2"))
b2.place(x=70,y=180)
b1=tkinter.Button(root,text=("1"),height="2",width="4",command=lambda : show("1"))
b1.place(x=110,y=180)
b0=tkinter.Button(root,text=("0"),height="2",width="4",command=lambda : show("0"))
b0.place(x=70,y=230)

b=tkinter.Button(root,text=("."),height="2",width="4",command=lambda : show("."))
b.place(x=30,y=230)
b10=tkinter.Button(root,text=("%"),height="2",width="4",command=lambda : show("%"))
b10.place(x=110,y=230)

b11=tkinter.Button(root,text=("/"),height="2",width="6",command=lambda : show("/"))
b11.place(x=160,y=80)
b12=tkinter.Button(root,text=("*"),height="2",width="6",command=lambda : show("*"))
b12.place(x=160,y=130)
b13=tkinter.Button(root,text=("-"),height="2",width="6",command=lambda : show("-"))
b13.place(x=160,y=180)
b14=tkinter.Button(root,text=("+"),height="2",width="6",command=lambda : show("+"))
b14.place(x=160,y=230)

b15=tkinter.Button(root,text=("="),height="2",width="9",command=lambda : calculate())
b15.place(x=30,y=280)

b15=tkinter.Button(root,text=("AC"),height="2",width="13",command=lambda : clear())
b15.place(x=110,y=280)


root.mainloop()