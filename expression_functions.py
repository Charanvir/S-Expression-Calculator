error_message = "Please enter the expression in the correct format, with at least two valid operands per expression)"


def output_function(user_input):
    try:
        while ')' in user_input:
            right_index = user_input.index(')')
            left_index = user_input[:right_index].rindex('(')
            try:
                evaluated_expression = evaluate(user_input[left_index + 1:right_index])
            except IndexError:
                return error_message
            user_input = user_input[:left_index] + str(evaluated_expression) + user_input[right_index + 1:]
        return int(user_input)
    except ValueError:
        return error_message


def evaluate(expression):
    parts_of_expression = expression.split()
    if len(parts_of_expression) <=2:
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
    return int(exp1)
