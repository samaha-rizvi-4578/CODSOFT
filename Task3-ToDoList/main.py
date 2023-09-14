import tkinter as tk
from tkinter import ttk

# Create a function to add a new task to the list.
def add_task():
    # Get the text from the entry field.
    task_text = task_entry.get()
    
    if task_text:  # Check if the entry is not empty
        # Add the task to the listbox.
        tasks_listbox.insert("end", task_text)

        # Clear the entry field.
        task_entry.delete(0, "end")

# Create a function to delete a task from the list.
def delete_task():
    # Get the selected task from the listbox.
    selected_task_index = tasks_listbox.curselection()
    
    if selected_task_index:  # Check if an item is selected
        # Delete the task from the listbox.
        tasks_listbox.delete(selected_task_index)

# Create a function to edit a task.
def edit_task():
    # Get the selected task from the listbox.
    selected_task_index = tasks_listbox.curselection()
    
    if selected_task_index:  # Check if an item is selected
        # Get the new task text from the entry field.
        new_task_text = edit_entry.get()
        
        if new_task_text:  # Check if the entry is not empty
            # Update the selected task with the new text.
            tasks_listbox.delete(selected_task_index[0])
            tasks_listbox.insert(selected_task_index[0], new_task_text)
            
            # Clear the entry field.
            edit_entry.delete(0, "end")

# Create the main window.
root = tk.Tk()
root.title("Task Master")

# Create a style for the frames.
style = ttk.Style()
style.configure('TFrame', background='black')  # Set the background color for frames

# Create a style for buttons.
style.configure('TButton', background='light blue', foreground='blue')  # Set button background and text color

# Create a style for entry field.
style.configure('TEntry', background='light blue', foreground='blue')  # Set entry field background and text color

# Create a frame for the input and action widgets.
input_frame = ttk.Frame(root, padding=10)
input_frame.pack(fill="both", expand=True)

# Create a label for the task entry.
task_label = ttk.Label(input_frame, text="Add Task:")
task_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Create an entry field to input tasks.
task_entry = ttk.Entry(input_frame)
task_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
task_entry.configure(style='TEntry')  # Apply the style to the entry field

# Create a button to add a new task.
add_task_button = ttk.Button(input_frame, text="Add Task", command=add_task)
add_task_button.grid(row=0, column=2, padx=5, pady=5)
add_task_button.configure(style='TButton')  # Apply the style to the button

# Create a button to delete a task.
delete_task_button = ttk.Button(input_frame, text="Delete Task", command=delete_task)
delete_task_button.grid(row=1, column=2, padx=5, pady=5)
delete_task_button.configure(style='TButton')  # Apply the style to the button

# Create a frame for the listbox and edit widgets.
list_frame = ttk.Frame(root, padding=10)
list_frame.pack(fill="both", expand=True)

# Create a listbox to display the tasks.
tasks_listbox = tk.Listbox(list_frame)
tasks_listbox.pack(fill="both", expand=True)
tasks_listbox.configure(bg='light blue')  # Set the listbox background color

# Create a label for the edit entry.
edit_label = ttk.Label(list_frame, text="Edit Task:")
edit_label.pack(pady=5)

# Create an entry field for editing tasks.
edit_entry = ttk.Entry(list_frame)
edit_entry.pack(fill="both", expand=True)
edit_entry.configure(style='TEntry')  # Apply the style to the entry field

# Create a button to edit a task.
edit_task_button = ttk.Button(list_frame, text="Edit Task", command=edit_task)
edit_task_button.pack(pady=5)
edit_task_button.configure(style='TButton')  # Apply the style to the button

# Start the main loop.
root.mainloop()
