import tkinter
from tkinter import *
from tkinter import messagebox
#**********************MAIN WINDOW***********************
root = Tk()
root.title("To-do-list")
root.geometry("440x350+100+200")

title_lbl = Label(root, text="TO-DO-LIST", font=("Bradley Hand ITC", 30, "bold"),bg="rosybrown", fg="white")
title_lbl.place(x=0, y=0, width=440, height=45)

#********************FUNTION TO ADD TASK*******************
def add_task():
    task=ENTRY.get()
    if task:
        TASKS_LIST.insert(0,task)
        ENTRY.delete(0,END)
        save_tasks()
    else:
        messagebox.showerror("Error","Enter a Task")

#*********************FUNCTION TO DELETE TASK******************
def delete_task():
    selected=TASKS_LIST.curselection()
    if selected:
        TASKS_LIST.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror("Error","Choose a Task to Delete")

def mark_done():
    selected = TASKS_LIST.curselection()
    if selected:
        index = selected[0]
        task = TASKS_LIST.get(index)
        if not task.startswith("DONE: "):
            TASKS_LIST.delete(index)
            TASKS_LIST.insert(index,task+"  ✔")
            save_tasks()
        else:
            messagebox.showerror("Error", "Task is already marked as DONE")
    else:
        messagebox.showerror("Error", "Choose a Task to Mark as DONE")

#****************FUNTION TO SAVE TASK********************
def save_tasks():
    with open("tasks.txt","w")as f:
        tasks=TASKS_LIST.get(0,END)
        for task in tasks:
            f.write(task+"\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks=f.readlines()
            for task in tasks:
                TASKS_LIST.insert(0,task.strip())
    except FileNotFoundError:
        pass

#********LEFT FRAME*******
left_frame=Frame(root)
left_frame.place(x=2, y=48, width=235, height=475)

ADD_TASKS= Label(left_frame, text="ADD TASK", font=("Freestyle Script", 25, "bold"),bg="teal", fg="white")
ADD_TASKS.place(x=10, y=5, width=210, height=45)

ENTRY=Entry(left_frame,highlightthickness=3, highlightbackground="black",font=("times new roman", 18))
ENTRY.place(x=10, y=70, width=210, height=45)

ADD = Button(left_frame, text="ADD",command=add_task , cursor="hand2",font=("Freestyle Script", 20, "bold"), bg="olive", fg="white")
ADD.place(x=10, y=140, width=210, height=40)

DELETE=Button(left_frame, text="DELETE",command=delete_task , cursor="hand2",font=("Freestyle Script", 20, "bold"), bg="olive", fg="white")
DELETE.place(x=10, y=190, width=210, height=40)

DONE=Button(left_frame, text="DONE" , command=mark_done,cursor="hand2",font=("Freestyle Script", 20, "bold"), bg="olive", fg="white")
DONE.place(x=10, y=240, width=210, height=40)

#*******RIGHT FRAME***********
right_frame = Frame(root, highlightthickness=2, highlightbackground="black")
right_frame.place(x=230, y=48, width=200, height=280)
TASKS= Label(right_frame, text="TASKS", font=("Freestyle Script", 25, "bold"),bg="teal", fg="white")
TASKS.place(x=10, y=5, width=175, height=45)

TASKS_LIST=Listbox(right_frame,width=15,highlightthickness=1, highlightbackground="black",font=("times new roman", 18))
TASKS_LIST.place(x=6,y=58,height=214)

load_tasks()
root.mainloop()