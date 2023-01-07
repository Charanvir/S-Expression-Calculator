# The evaluate function will work as intended when there are integer gives for each expression. It will be called
# multiple times by another function, which breaks apart the user input into separate expressions,
# such as nested expression
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
