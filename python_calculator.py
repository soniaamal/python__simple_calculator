import tkinter as tk

#Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

#Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)

#Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

#Create the main window
root = tk.Tk()
root.title("simple calculator")

#Entry field
entry = tk.Entry(root, width=28, borderwidth=5, font=("Arial", 18))
entry.grid(row=0, column=0 ,columnspan=4, padx= 10, pady=10)

#button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

#add button to the window
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, padx=25, pady=20, command=button_clear, font=("Arial", 14))

    elif text == '=':
        button = tk.Button(root, text=text, padx=25, pady=20, command=button_equal, font=("Arial", 14))
    else:
        button = tk.Button(root, text=text, padx=25, pady=20, command=lambda  t=text: button_click(t), font=("Arial", 14))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# configure row and column weights for resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)
        
# run the application
root.mainloop()


