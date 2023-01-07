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


