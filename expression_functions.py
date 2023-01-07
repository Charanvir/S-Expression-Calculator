def output_function(user_input):
    try:
        while ')' in user_input:
            right_index = user_input.index(')')
            left_index = user_input[:right_index].rindex('(')
            try:
                evaluated_expression = evaluate(user_input[left_index + 1:right_index])
            except IndexError:
                return "Please ensure that each expression has at least two valid operands"
            user_input = user_input[:left_index] + str(evaluated_expression) + user_input[right_index + 1:]
        return int(user_input)
    except ValueError:
        return "Please enter the expression in the correct format."


def evaluate(expression):
    parts_of_expression = expression.split()
    operator = parts_of_expression[0]
    exp1 = parts_of_expression[1]
    exp2 = parts_of_expression[2]
    if operator == 'add':
        return int(exp1) + int(exp2)
    elif operator == 'multiply':
        return int(exp1) * int(exp2)
    elif operator == "exponent":
        return int(exp1) ** int(exp2)
    elif operator == "subtract":
        return int(exp1) - int(exp2)
    return int(expression)
