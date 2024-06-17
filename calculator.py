# Importing libraries
import tkinter as tk
import threading
import math

# Class representing the calculator
class CalculatorApp:
    
    # Initializes the calculator GUI
    def __init__(self, master):
        self.master = master
        # Window title
        master.title("Calculator")
        master.config(bg="#333333")

        # Variable to hold the result
        self.result_var = tk.StringVar()
        # Sets the result to an empty string
        self.result_var.set("")
        # Variable to hold the expression
        self.expression_var = tk.StringVar()
        
        # Creates a label widget to display the expression
        self.expression_label = tk.Label(master, textvariable=self.expression_var, font=("Calibri", 15), anchor="e", padx=5, bg="#333333", fg="white")
        # Places the label widget within the grid of the main window
        self.expression_label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        # Creates a label widget to display result
        self.result_label = tk.Label(master, textvariable=self.result_var, font=("Calibri", 40), anchor="e", padx=5, bg="#333333", fg="white")
        # Places the label widget within the grid of the main window
        self.result_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Defines the position of the buttons
        self.buttons = [
            ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2), ('/', 2, 3),
            ('^', 3, 0), ('x²', 3, 1), ('√', 3, 2), ('*', 3, 3),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('-', 4, 3),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('+', 5, 3),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('.', 6, 3),
            ('C', 7, 0), ('0', 7, 1), ('←', 7, 2), ('=', 7, 3)
        ]

        # Creates a button widget for each tuple in self.buttons
        for (text, row, column) in self.buttons:
            '''
            Command parameter is set to a lambda function to call on_button_click by passing text as an argument
            Creates a button widget with specified text and colors
            '''
            button = tk.Button(master, text=text, command=lambda t=text: self.on_button_click(t), font=("Calibri", 20), bg="#555555", fg="white")
            # Places the button widget within the grid of the main window
            button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

        # Setting the window size
        master.geometry("500x500")
        
        # Ensures consistent layout if window is resized
        for i in range(8):
            master.grid_rowconfigure(i, weight=1, minsize=60)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1, minsize=60)


        # Empty string for user input
        self.expression = ""

    # Method called when a button is clicked
    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.expression)
                # Updates the result label
                self.result_var.set(result)
                # Updates the expression label
                self.expression_var.set(self.expression)
                self.expression = str(result)
            except Exception:
                self.result_var.set("Error")
                self.expression_var.set("")
                self.expression = ""
                
        elif char == 'C':
            self.expression = ""
            # Updates the result label
            self.result_var.set("")
            # Updates the expression label
            self.expression_var.set("")
            
        elif char == '←':
            self.expression = self.expression[:-1]
            # Updates the result label
            self.result_var.set(self.expression)

        elif char == '.':
            # Checks if there is already a decimal point in the expression
            if '.' not in self.expression:
                self.expression += char
            
        elif char == '^':
            self.expression += '**'
            
        elif char == '√':
            try:
                result = math.sqrt(float(self.expression))
                # Updates the result label
                self.result_var.set(result)
                # Updates the expression label
                self.expression_var.set("sqrt(" + self.expression + ")")
                self.expression = str(result)
            except Exception:
                self.result_var.set("Error")
                self.expression_var.set("")
                self.expression = ""
                
        elif char == 'x²':
            try:
                result = eval(self.expression)**2
                # Updates the result label
                self.result_var.set(result)
                # Updates the expression label
                self.expression_var.set("(" + self.expression + ")²")
                self.expression = str(result)
            except Exception:
                self.result_var.set("Error")
                self.expression_var.set("")
                self.expression = ""

        elif char in ['sin', 'cos', 'tan']:
            try:
                # Evaluate the trigonometric function
                result = eval(f"math.{char}({self.expression})")
                # Update the result label
                self.result_var.set(result)
                # Update the expression label
                self.expression_var.set(f"{char}({self.expression})")
                self.expression = str(result)
            except Exception:
                self.result_var.set("Error")
                self.expression_var.set("")
                self.expression = ""

        else:
            self.expression += char
            self.result_var.set(self.expression)

# Starts the GUI
def start_gui():
    # Creates main window
    root = tk.Tk()
    # Creates an instance of the CalculatorApp class
    app = CalculatorApp(root)
    # Starts event loop of tkinter app
    root.mainloop()

# Function to a create a thread
def start_thread():
    # Starts a thread using threading.Thread constructor
    calculator_thread = threading.Thread(target=start_gui)
    calculator_thread.start()

# Calls start_thread function
start_thread()
