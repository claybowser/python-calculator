import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator by @claybowser")
        
        # Create display
        self.display = tk.Entry(root, width=50, justify="right", font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=8, padx=5, pady=5)
        
        # Basic buttons layout - now more horizontal with 8 columns
        buttons = [
            # Row 1 - Numbers and basic operations
            ['7', '8', '9', '/', 'sin', 'cos', 'tan', 'π'],
            ['4', '5', '6', '*', '√', 'x²', 'x³', 'x^y'],
            ['1', '2', '3', '-', '(', ')', 'log', 'ln'],
            ['0', '.', '=', '+', 'C', 'CE', 'DEL', 'e']
        ]
        
        # Create buttons using nested loops
        for row_idx, row in enumerate(buttons, 1):
            for col_idx, button in enumerate(row):
                cmd = lambda x=button: self.click(x)
                btn = ttk.Button(root, text=button, command=cmd)
                btn.grid(row=row_idx, column=col_idx, padx=2, pady=2, sticky='nsew')
        
        # Configure grid columns to expand equally
        for i in range(8):
            root.grid_columnconfigure(i, weight=1)
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
    
    def click(self, key):
        if key == '=':
            try:
                # Validate the expression before evaluation
                expression = self.display.get()
                
                # First try to evaluate - if this fails with NameError, it means invalid input
                try:
                    result = eval(expression)
                except NameError:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Error")  # For invalid input like "abc"
                    return
                
                # Check for invalid characters
                if any(c not in '0123456789+-*/.() ' for c in expression):
                    raise ValueError("Invalid characters in expression")
                
                # Check if result is a valid number
                if not isinstance(result, (int, float)):
                    raise ValueError("Invalid result type")
                
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ZeroDivisionError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Division by zero")
            except (SyntaxError, ValueError):
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Invalid expression")
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Invalid expression")
        
        elif key == 'C' or key == 'CE':
            self.display.delete(0, tk.END)
        
        elif key in ['sin', 'cos', 'tan']:
            try:
                value = float(self.display.get())
                if key == 'sin':
                    result = math.sin(math.radians(value))
                elif key == 'cos':
                    result = math.cos(math.radians(value))
                else:  # tan
                    result = math.tan(math.radians(value))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        
        elif key == '√':
            try:
                value = float(self.display.get())
                if value < 0:
                    raise ValueError()
                result = math.sqrt(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        
        elif key == 'π':
            self.display.insert(tk.END, str(math.pi))
        
        elif key == 'e':
            self.display.insert(tk.END, str(math.e))
        
        elif key == 'DEL':
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
        
        elif key == 'x³':
            try:
                value = float(self.display.get())
                result = value ** 3
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        
        elif key == 'x²':
            try:
                result = float(self.display.get()) ** 2
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        
        else:
            self.display.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop() 