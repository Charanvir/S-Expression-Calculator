def evaluate(expression):
    operator = expression.split()[0]
    operands = expression.split()[1:]
    print(f"the following is the operator: {operator}")
    print(f"the following is the operand: {operands}")

