import sys
from expression_functions import evaluate

user_input = sys.argv[1]

while True:
    result = evaluate(user_input)
    print(result)
    break
