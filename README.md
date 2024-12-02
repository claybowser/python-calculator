### Scientific Calculator written in Python
### Author: Clay Bowser
### Date: December 2nd 2024
### This repository hosts a scientific calculator written in Python and Tkinter. It includes error handling, and unit tests.
---
# Scientific Calculator

A simple scientific calculator application built with Python and Tkinter, featuring basic arithmetic operations and scientific functions.

## Features

- Basic Operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)

- Scientific Functions:
  - Square (x²)
  - Cube (x³)
  - Square Root (√)
  - Trigonometric Functions (sin, cos, tan)
  - Constants (π, e)

- Additional Features:
  - Clear Display (C, CE)
  - Delete Last Character (DEL)
  - Error Handling
  - Decimal Point Operations

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- Math module (built-in)

## Installation

1. Clone this repository or download the source files:
   - calculator.py
   - test_calculator.py

2. No additional package installation is required as the application uses Python's standard libraries.

## Usage

Run the calculator application:
```bash
python calculator.py
```
![2024-12-02 Screenshot of graphical user interface of calculator.]("./calculator-ui.PNG")

The calculator provides a graphical interface with:
- A display screen for input and results
- Numeric keypad (0-9)
- Operation buttons (+, -, *, /)
- Scientific function buttons
- Clear and delete buttons

## Testing

The application includes a comprehensive test suite. To run the tests:
```bash
python -m unittest test_calculator.py -v
```

![2024-12-02 Screenshot of output of calculator unit test showing no failures.]("./calculator-unit-test-output.PNG")

The test suite covers:
- Basic arithmetic operations
- Scientific functions
- Error handling
- Input validation
- Display clearing and manipulation

## Error Handling

The calculator handles various error cases:
- Division by zero
- Invalid expressions
- Invalid characters
- Negative square roots
- Multiple decimal points
- Incomplete expressions

## Project Structure

- `calculator.py`: Main application file containing the calculator implementation
- `test_calculator.py`: Test suite for the calculator
- `__pycache__/`: Python bytecode cache directory (can be ignored)

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.
