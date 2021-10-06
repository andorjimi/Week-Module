import tkinter as tk
from tkinter import Tk, Text, ttk
from tkmacosx import Button


root = Tk()
root.geometry("600x300")
root.title("Week Moudule")
root.configure(background='#3DB2FF')

# variables
week_number = ""
week_number = tk.StringVar()

# Functions
def CourseConverer(week_number):
    course = {
        "Module 1" :f'''
    Week {week_number} is in Module 1

    Module 1:

    Week 1
    Week 2
    Week 3
    Week 4
    Week 5
            ''',
        "Module 2" : f'''
    Week {week_number} is in Module 2

    Module 2

    Week 6
    Week 7
    Week 8
    Week 9
    Week 10
            ''',
        "Module 3" : f'''
    Week {week_number} is in Module 3

    Module 3

    Week 11
    Week 12
    Week 13
    Week 14
    Week 15
            ''',
        "Module 4" : f'''
    Week {week_number} is in Module 4

    Module 4

    Week 16
    Week 17
    Week 18
    Week 19
    Week 20
    Week 21
            ''',
        "Module 5" : f'''
    Week {week_number} is in Module 5

    Module 5

    Week 22
    Week 23
    Week 24
    Week 25
    Week 26
            ''',
        "Module 6" : f'''
    Week {week_number} is in Module 6

    Module 6

    Week 27
    Week 28
    Week 29
    Week 30
    Week 31
            ''',
        "Module 7" : f'''
    Week {week_number} is in Module 7

    Module 7

    Week 32
    Week 33
    Week 34
    Week 35
    Week 36
            ''',
        "Module 8" : f'''
    Week {week_number} is in Module 8

    Module 8

    Week 37
    Week 38
    Week 39
    Week 40
    Week 41
    Week 42
            ''',}


    if week_number <= 5:
        print(course.get("Module 1"))
        answer_box.insert(1.0, course.get("Module 1"))
        answer_box.tag_add("center", "1.0", "end")
    elif week_number == 6  or week_number <= 10:
        print(course.get("Module 2"))
        answer_box.insert(1.0, course.get("Module 2"))
        answer_box.tag_add("center", "1.0", "end")
    elif week_number == 11  or week_number <= 15:
        print(course.get("Module 3"))
        answer_box.insert(1.0, course.get("Module 3"))
        answer_box.tag_add("center", "1.0", "end")
    elif week_number == 16  or week_number <= 21:
        print(course.get("Module 4"))
        answer_box.insert(1.0, course.get("Module 4"))
        answer_box.tag_add("center", "1.0", "end")
    elif week_number == 22  or week_number <= 26:
        print(course.get("Module 5"))
        answer_box.insert(1.0, course.get("Module 5"))
        answer_box.tag_add("center", "1.0", "end")
    elif week_number == 27  or week_number <= 31:
        print(course.get("Module 6"))
        answer_box.insert(1.0, course.get("Module 6"))
        answer_box.tag_add("center", "1.0", "end")
    elif week_number == 32  or week_number <= 36:
        print(course.get("Module 7"))
        answer_box.insert(1.0, course.get("Module 7"))
        answer_box.tag_add("center", "1.0", "end")
    elif week_number == 37  or week_number <= 42:
        print(course.get("Module 8"))
        answer_box.insert(1.0, course.get("Module 8"))
        answer_box.tag_add("center", "1.0", "end")
    else:
        print("Not in range")

def clear_box():
    answer_box.delete(1.0, tk.END)
    entry.delete(0, "end")

def go(event=None):
    error_1 = "*** Please enter a number from 1 - 42 ***"

    week_number = entry.get()
    clear_box()

    try:
        week_number = int(week_number)
    except Exception as ValueError:
        pass

    if week_number in range(1, 43):
        CourseConverer(week_number)
    else:
        answer_box.insert(1.0, error_1)
        answer_box.tag_add("center", "1.0", "end")

root.bind('<Return>', go)

# Add a Frame for the Text box
text_frame = tk.Frame(root, width=200, height=200)
text_frame.pack(fill="x", padx=50, pady=20)


answer_box = Text(text_frame, height=11, width=10, bg="#FFEDDA",font=("Helvitca", 16), fg="black")
answer_box.tag_configure("center", justify='center')
answer_box.pack(fill="both")

# Add a frame for the Button and imput box.
control_frame = tk.Frame(root, height=80, bg="#3DB2FF")
control_frame.pack(fill="both", padx=50)

week_lable = tk.Label(control_frame, text="Week Number", bg="#FFEDDA", font=("Helvitca", 14), fg="black")
week_lable.pack(side="left",fill="y")

entry = tk.Entry(control_frame,textvariable=week_number,width=10,bg="#FFEDDA",font=("Helvitca", 25), fg="black")
entry.pack(side="left")

go_button = Button(control_frame, text="Go", height=30, width=100, command=go, bg="#FFEDDA", activebackground="#FFB830")
go_button.pack(side="right",padx=10)


root.mainloop()
