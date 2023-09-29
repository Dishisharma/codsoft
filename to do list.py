import tkinter
import tkinter.messagebox
root=tkinter.Tk()
root.title("To-Do-List")
root.geometry("300x350")
font1=("Arial",10,"bold")

def add_task():
    task = task_entry.get()
    if task:
       Listbox_tasks.insert(0, task)
       task_entry.delete(0, END)
       save_tasks()
    else:messagebox.showerror("error","enter a task.")
def Remove_task():
    selected =  Listbox_tasks.curselection()
    if selected:
        Listbox_tasks.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('error', 'choose a task to delete')
def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks=Listbox_tasks.get(0,END)
        for task in tasks:
            f.write(task + "\n")
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                Listbox_tasks.insert(0, task.strip())
    except FileNotFoundError:
        pass
Title_label=tkinter.Label(root,font=("Arial",20),text="To-Do-List")
Title_label.place(x=80,y=10) 
add_button=tkinter.Button(root,command=add_task,font=font1,text="Add")
add_button.place(x=80,y=70) 
remove_button=tkinter.Button(root,command=Remove_task,font=font1,text="Remove")
remove_button.place(x=150,y=70) 
Listbox_tasks=tkinter.Listbox(root,height=6 , width= 30)
Listbox_tasks.place(x=50,y=120)
task_entry=tkinter.Entry(root,font=font1)
task_entry.place(x=80,y=100)

load_tasks()
root.mainloop()