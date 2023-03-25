import os
import tkinter as tk
from tkinter import ttk

# All the callback functions here


# Function for when a course is selected from the course drop down box
def courseSelect(event):
    sub_box.set("Subject")
    topic_box.set("Topic")
    course_txt = course_box.get()
    file_list = os.listdir(f"Input_Files/{course_txt}")
    sub_box['values'] = file_list


def subSelect(event):
    topic_box.set("Topic")
    course_txt = course_box.get()
    sub_txt = sub_box.get()
    file_list = os.listdir(f"Input_Files/{course_txt}/{sub_txt}")
    topic_box['values'] = file_list


def topicSelect(event):
    # Build the file path
    course_txt = course_box.get()
    sub_txt = sub_box.get()
    topic_txt = topic_box.get()
    mod_name = f"Input_Files.{course_txt}.{sub_txt}.{topic_txt[:-3]}"

    # Import the specified module and get make an object from the class inside
    module = __import__(mod_name, fromlist=['*'])

    class_obj = None
    class_count = 0
    for name, obj in module.__dict__.items():
        if isinstance(obj, type):
            class_count += 1
            if class_count == 2:
                class_obj = obj
                break

    my_obj = class_obj()
    info = my_obj.getInfo()

    # Create the info boxes in the GUI
    


# Create root
root = tk.Tk()
root.geometry('500x500')

# Initialize frames for organization
top_frame = tk.Frame(root)
top_frame.pack(side='top', fill="both", expand=True)

bottom_frame = tk.Frame(root)
bottom_frame.pack(side='bottom', fill="both", expand=True)

file_frame = tk.Frame(top_frame, relief='groove', bg='blue')
file_frame.pack(side='left', fill="both", expand=True)

note_frame = tk.Frame(top_frame, relief='groove', bg='green')
note_frame.pack(side="right", fill="both", expand=True)

input_frame = tk.Frame(bottom_frame, relief='groove', bg='red')
input_frame.pack(fill="both", expand=True)

# create subject drop down boxes
course_box = ttk.Combobox(file_frame)
course_box.set("Course")
sub_box = ttk.Combobox(file_frame)
sub_box.set("Subject")
topic_box = ttk.Combobox(file_frame)
topic_box.set("Topic")

# Populate the course drop down
course_files = os.listdir("Input_Files")
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
