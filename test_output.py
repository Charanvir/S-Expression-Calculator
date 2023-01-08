from expression_functions import output_function

correct_test_cases = [
    ("123", 123),
    ("(add 1 1)", 2),
    ("(multiply 5 5)", 25),
    ("(add (add 3 4) 7)", 14),
    ("(multiply (multiply 3 3) (add 4 9))", 117),
    ("(add (multiply (add 4 6) (multiply 10 5)) (add 5 5))", 510),
    ("(add (multiply (add 5 5) 5) (add 3 4))", 57),
    ("(add (multiply 2 4 6) (add 2 4 6) (multiply 3 3 3))", 87),
    ("(multiply (add (add 1 2 3) 5) (exponent 2 2 2) (subtract 6 4))", 352)
]

error_message = "Please enter the expression in the correct format, with at least two valid operands per expression)"
error_handling_test_cases = [
    ("abc", error_message),
    ("add 1 1", error_message),
    ("(add 1 (add 1 1)", error_message),
    ("(add 1)", error_message),
    ("(add (add 1 1))", error_message),
    ("(multiply (add 1 1) (multiply 1)", error_message),
    ("(add (multiply 1)", error_message)
]


def test_correct_output():
    for test in correct_test_cases:
        expression, result = test
        assert output_function(expression) == result


def test_potential_error():
    for test in error_handling_test_cases:
        expression, message = test
        assert output_function(expression) == message
