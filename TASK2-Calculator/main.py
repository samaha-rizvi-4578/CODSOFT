import tkinter as tk

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("NumWiz")

# Set the window icon
root.iconbitmap('calc.ico') 

# Create an entry field for input
entry = tk.Entry(root, font="Helvetica 20 bold")
entry.pack(fill=tk.X, padx=10, pady=10, ipadx=8, ipady=8)

# Define colors for buttons
button_bg = "#77E080"  # Light gray
button_fg = "#023F08"  # Black

# Create buttons for numbers and operators
button_frame = tk.Frame(root)
button_frame.pack()

button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 0, 0

for button_text in button_texts:
    button = tk.Button(button_frame, text=button_text, font="Helvetica 15 bold", width=3, height=1,
                       bg=button_bg, fg=button_fg)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
