import unittest
from calculator import ScientificCalculator
import tkinter as tk
import math
# to execute the test, run the command: python -m unittest test_calculator.py -v
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.calculator = ScientificCalculator(self.root)
    
    def test_addition(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "2+2")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "4")
    
    def test_square(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "5")
        self.calculator.click('x²')
        self.assertEqual(self.calculator.display.get(), "25.0")
    
    def test_square_root(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "16")
        self.calculator.click('√')
        self.assertEqual(self.calculator.display.get(), "4.0")
    
    def test_sin(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "90")
        self.calculator.click('sin')
        self.assertAlmostEqual(float(self.calculator.display.get()), 1.0, places=10)
    
    def test_clear(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "123")
        self.calculator.click('C')
        self.assertEqual(self.calculator.display.get(), "")
    
    def test_multiplication(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "3*4")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "12")
    
    def test_division(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "10/2")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "5.0")
    
    def test_division_by_zero(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "5/0")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "Error: Division by zero")
    
    def test_invalid_input(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "abc")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "Error")
    
    def test_decimal_calculation(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "2.5+2.5")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "5.0")
    
    def test_negative_square_root(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "-16")
        self.calculator.click('√')
        self.assertEqual(self.calculator.display.get(), "Error")
    
    def test_invalid_characters(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "2+@+3")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "Error: Invalid expression")
    
    def test_incomplete_expression(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "2+")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "Error: Invalid expression")
    
    def test_multiple_decimal_points(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "2.5.6")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "Error: Invalid expression")
    
    def test_division_by_zero_message(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "5/0")
        self.calculator.click('=')
        self.assertEqual(self.calculator.display.get(), "Error: Division by zero")
    
    def test_trigonometric_functions(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "30")
        self.calculator.click('sin')
        self.assertAlmostEqual(float(self.calculator.display.get()), 0.5, places=10)
    
    def test_constants(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.click('π')
        self.assertEqual(self.calculator.display.get(), str(math.pi))
    
    def test_delete_character(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "123")
        self.calculator.click('DEL')
        self.assertEqual(self.calculator.display.get(), "12")
    
    def test_cube(self):
        self.calculator.display.delete(0, tk.END)
        self.calculator.display.insert(tk.END, "3")
        self.calculator.click('x³')
        self.assertEqual(self.calculator.display.get(), "27.0")
    
    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main() 