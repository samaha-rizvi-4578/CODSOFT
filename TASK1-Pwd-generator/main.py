# Import necessary modules
import random  # For generating random passwords
import tkinter as tk  # For creating the graphical user interface (GUI)
from tkinter import messagebox  # For displaying error messages

# Define character sets for password generation
lower = "abcdefghijklmnopqrstuvwxyz"  # Lowercase letters
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Uppercase letters
symbols = "[]{}()@!#$%^&*-+_=;:.,/?\\|"  # Special symbols
numbers = "0123456789"  # Numbers

# Combine all character sets into one for password generation
all_ch = lower + upper + numbers + symbols

# Function to generate a random password of a given length
def generate_password(length):
    password = "".join(random.sample(all_ch, length))
    return password

# Function to handle the "Generate Password" button click event
def generate_button_clicked():
    length = length_entry.get()
    
    try:
        length = int(length)  # Convert user input to an integer
        if length <= 0:
            raise ValueError("Enter Correct length > 0")
        
        password = generate_password(length)  # Generate the password
        password_label.config(text="Your Password Is: " + password)  # Update the label with the generated password
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))  # Display an error message for invalid input

# Create the main window
root = tk.Tk()
root.title("Password Generator")  # Set the window title

# Create widgets (GUI elements)
instruction_label = tk.Label(root, text="Enter The Desired Length:")  # Label for instruction
length_entry = tk.Entry(root)  # Entry field for user input
generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked)  # Button to trigger password generation
password_label = tk.Label(root, text="Your Password Is:")  # Label to display the generated password

# Place widgets using grid layout
instruction_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))  # Grid layout for labels
length_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)  # Grid layout for input field
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  # Grid layout for button
password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)  # Grid layout for displaying the generated password

# Start the GUI event loop
root.mainloop()  # This starts the GUI application and keeps it running until the user closes the window
