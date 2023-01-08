error_message = "Please enter the expression in the correct format, with at least two valid operands per expression)"


def output_function(user_input):
    """
    output_function() processes a string by evaluating the individual expressions within the overall string. It extracts
    these individual expressions and gets the expression result from the evaluate function. When every individual expression
    within the string is evaluated, it returns the final result as an integer. If the input is not in the correct format,
    the function handles the error by returns an error message to the user.

    Input:
    user_input (str)

    The correct format for the user_input is as followed:
    "(operator operand operand)"
    The operator can be one of the following: add, multiply, exponent, subtract
    The operand is formatted the same as the original user_input string.
    The user_input string must contain the operator, and at least two operands.

    *** Special case: The user_input can also simply be an integer, which will immediately be returned to the user.
    output_function will receive this integer as a string, and return it back to the user as an int

    Output:
    int: The final evaluation of the user_string expression

    Example:
        output_function("(add 1 1)") => 2
        output_function("(multiply (multiply 3 3) (add 4 9))") => 117
        output_function(123) => 123
    """
    try:
        while ')' in user_input:
            right_index = user_input.index(')')
            left_index = user_input[:right_index].rindex('(')
            try:
                evaluated_expression = evaluate(user_input[left_index + 1:right_index])
                if evaluated_expression == "Incorrect Operator":
                    return "Please only use an operator from the following list [add, multiply, exponent, subtract]"
            except IndexError:
                return error_message
            user_input = user_input[:left_index] + str(evaluated_expression) + user_input[right_index + 1:]
        return int(user_input)
    except ValueError:
        return error_message


def evaluate(expression):
    """
    The evaluate function takes an expression and returns the resulting int. This functions takes the input as a string
    and splits it to get its corresponding parts. These parts are saved into a variable called parts_of_expression.
    If parts_of_expression has a length of 2 or less, an error message it returned. Each expression must include an
    operator, and at least 2 operands. The first index of the parts_of_expression List is extracted as the operator,
    while the first operand is saved to a variable called exp1.
    Once these variable are created, the operator is checked to be one of the following: add multiply exponent or
    subtract. If one of these operators are found, a for loop will loop over the remaining parts of the
    parts_of_expression List and execute the operation accordingly. If an operator is entered that does not meet the
    criteria, an error message is returned

    Input:
    expression: str which includes an operator and at least two operands
    expression is in the following format: "operator operand operand"

    Output:
    int: the evaluated result of the inputted expression

    Example:
        evaluate("add 1 1") => 2
        evaluate("multiply 2 2") => 4
        evaluated("divide 2 2") => "Incorrect Operator
    """
    parts_of_expression = expression.split()
    if len(parts_of_expression) <= 2:
        return error_message
    operator = parts_of_expression[0]
    exp1 = int(parts_of_expression[1])
    if operator == "add":
        for operand in parts_of_expression[2:]:
            exp1 = exp1 + int(operand)
    elif operator == "multiply":
        for operand in parts_of_expression[2:]:
            exp1 = exp1 * int(operand)
    elif operator == "exponent":
        for operand in parts_of_expression[2:]:
            exp1 = exp1 ** int(operand)
    elif operator == "subtract":
        for operand in parts_of_expression[2:]:
            exp1 = exp1 - int(operand)
    else:
        return "Incorrect Operator"
    return int(exp1)
