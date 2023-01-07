def output_function(user_input):
    while ')' in user_input:
        right_index = user_input.index(')')
        left_index = user_input[:right_index].rindex('(')
        evaluated_expression = evaluate(user_input[left_index + 1:right_index])
        user_input = user_input[:left_index] + str(evaluated_expression) + user_input[right_index + 1:]
    return int(user_input)


def evaluate(expression):
    parts_of_expression = expression.split()
    operator = parts_of_expression[0]
    exp1 = parts_of_expression[1]
    exp2 = parts_of_expression[2]
    if operator == 'add':
        return int(exp1) + int(exp2)
    elif operator == 'multiply':
        return int(exp1) * int(exp2)
    return int(expression)
