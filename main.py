import sys
from expression_functions import output_function

user_input = sys.argv[1]

while True:
    result = output_function(user_input)
    print(result)
    break
