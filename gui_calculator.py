import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Entry field (display screen)
entry = tk.Entry(
    root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)


# Function to add number/operator to display
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))


# Function to clear display
def clear():
    entry.delete(0, tk.END)


# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button in row:
        if button == "=":
            btn = tk.Button(frame, text=button, font=("Arial", 18), command=calculate)
        else:
            btn = tk.Button(
                frame,
                text=button,
                font=("Arial", 18),
                command=lambda b=button: click(b),
            )
        btn.pack(side="left", expand=True, fill="both")


# Clear button at bottom
clear_btn = tk.Button(root, text="C", font=("Arial", 18), command=clear)
clear_btn.pack(fill="both", padx=10, pady=5)

root.mainloop()
