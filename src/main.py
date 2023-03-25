import os
import tkinter as tk
from tkinter import ttk

# All the callback functions here


# Function for when a course is selected from the course drop down box
def courseSelect(event):
    sub_box.set("Subject")
    topic_box.set("Topic")
    course_txt = course_box.get()
    file_list = os.listdir(f"../Input_Files/{course_txt}")
    sub_box['values'] = file_list


def subSelect(event):
    topic_box.set("Topic")
    course_txt = course_box.get()
    sub_txt = sub_box.get()
    file_list = os.listdir(f"../Input_Files/{course_txt}/{sub_txt}")
    topic_box['values'] = file_list


def topicSelect(event):
    note = "hello"
    note_label['text'] = note


# Create root
root = tk.Tk()
root.geometry('500x500')

# Initialize frames for organization
top_frame = tk.Frame(root)
top_frame.pack(side='top')

bottom_frame = tk.Frame(root)
bottom_frame.pack(side='bottom')

file_frame = tk.Frame(top_frame, relief='groove', bg='blue')
file_frame.pack(side='left')

note_frame = tk.Frame(top_frame, relief='groove', bg='green')
note_frame.pack(side="right")

input_frame = tk.Frame(bottom_frame, relief='groove', bg='red')
input_frame.pack()

# create subject drop down boxes
course_box = ttk.Combobox(file_frame)
course_box.set("Course")
sub_box = ttk.Combobox(file_frame)
sub_box.set("Subject")
topic_box = ttk.Combobox(file_frame)
topic_box.set("Topic")

# Populate the course drop down
course_files = os.listdir("../Input_Files")
course_box['values'] = course_files

# Bind callback functions for the drop-downs
course_box.bind("<<ComboboxSelected>>", courseSelect)
sub_box.bind("<<ComboboxSelected>>", subSelect)
topic_box.bind("<<ComboboxSelected>>", topicSelect)

# Pack all the drop-downs in tight
course_box.grid(row=0, column=0)
sub_box.grid(row=1, column=0)
topic_box.grid(row=2, column=0)

# Create the note and input label
note_label = tk.Label(note_frame, text="Note: ")
note_label.grid(row=0)

input_label = tk.Label(input_frame, text="Inputs")
input_label.grid(row=0)

# run the mainloop to initialize the GUI
tk.mainloop()
