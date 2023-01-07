from expression_functions import output_function
import pytest

correct_test_cases = [
    ("123", 123),
    ("(add 1 1)", 2),
    ("(multiply 5 5)", 25),
    ("(add (add 3 4) 7)", 14),
    ("(multiply (multiply 3 3) (add 4 9))", 117),
    ("(add (multiply (add 4 6) (multiply 10 5)) (add 5 5))", 510),
    ("(add (multiply (add 5 5) 5) (add 3 4))", 57)
]

error_handling_test_cases = [
    ("abc", "Please enter the expression in the correct format."),
    ("add 1 1", "Please enter the expression in the correct format."),
    ("(add 1 (add 1 1)", "Please enter the expression in the correct format."),
    ("(add 1)", "Please ensure that each expression has at least two operands"),
    ("(add (add 1 1))", "Please ensure that each expression has at least two operands"),
    ("(multiply (add 1 1) (multiply 1)", "Please ensure that each expression has at least two operands")
]


def test_correct_output():
    for test in correct_test_cases:
        expression, result = test
        assert output_function(expression) == result


def test_potential_error():
    for test in error_handling_test_cases:
        expression, error_message = test
        assert output_function(expression) == error_message
