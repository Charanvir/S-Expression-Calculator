# S-Expression Calculator

## A command line calculator created using Python 3.10

![badmath](https://img.shields.io/badge/Version-1.0-lightblue)

1. [Description](#Description)
2. [Installation](#Installation)
3. [Usage](#Usage)

## Description

S-Expression Calculator is a command line application which takes an expression from the user and returns an integer.
The integer is the evaluated expression.

S-Expression Calculator takes user input as a string in the following format: "(operator operand operand)"
The user input can include multiple operands, which themselves can be expressions. These nested expressions will also be
calculated by the application. The user input must include at least two operands per each expression to function.

This application currently supports the following operations:

- addition via the "add" operator
- multiplication via the "multiply" operator
- exponential via the "exponent" operator
- subtraction via the "subtract" operator

### Dependencies

S-Expression Calculator uses two libraries to achieve its functionality.

```sys```

- The sys package is used to allow the user the expression to the output_function.

```pytest```

- This third party package is used to test the code, which is done in the test_output.py file.

### Installation

To run this application on your local machine, run the following command:
```git clone <GitHub repository URL above>```
This will install all the necessary files onto your local machine. Note that this application is built using
Python3.10, so Python must be installed on your local machine as well.

You can also choose to run the test file, by first installing the pytest third party package for this project.

### Usage

To use this application, navigate to the root directory of this project via your terminal and run the following command:

```commandline
python3 main.py "(operator operand operand)"
```

This will pass everything in the "" as an expression to be evaluated.
The application will return an integer, which is the result of the expression passed above

The application will return error_message if the expression is inputted correctly. Please refer to the format above.
