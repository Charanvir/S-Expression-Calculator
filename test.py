from expression_functions import output_function

test_cases = [
    ("123", 123),
    ("(add 1 1)", 2),
    ("(multiply 5 5)", 25),
    ("(add (add 3 4) 7)", 14),
    ("(multiply (multiply 3 3) (add 4 9))", 117),
    ("(add (multiply (add 4 6) (multiply 10 5)) (add 5 5))", 510),
    ("(add (multiply (add 5 5) 5) (add 3 4))", 57)
]

if __name__ == "__main__":
    for test in test_cases:
        expression, expected_result = test
        actual_result = output_function(expression)
        if actual_result == expected_result:
            print("Test Passed!!!!")
        else:
            print("Test Failed")
            print(f"The expected result was {expected_result}, but the actual result was {actual_result}")
