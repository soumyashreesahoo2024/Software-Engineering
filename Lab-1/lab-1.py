# The program reads a mathematical expression from the user.
# It iterates through each character of the expression, handling numbers, parentheses, and arithmetic operators.
# Negative numbers are handled, and numbers and symbols are pushed onto their respective stacks (NumStorage and SymbolStorage).
# The program follows the rules of operator precedence and performs the necessary calculations using the stacks.
# The final result is printed.



# composition: A owns B : B has no meaning or purpose in system without A
# Aggregation: A uses B : B exists independently from A
# Inheritance: A,B inherited from C: A,B are inherited from C


## NumStorage and SymbolStorage are two classes representing stacks to store numbers and symbols, respectively.
class NumStorage:
    def __init__(self):
        self.number = [0] * 100             # array for numbers 
        self.top = -1

class SymbolStorage:
    def __init__(self):
        self.symbol = [''] * 100            # array for symbols 
        self.top = -1

##  Stack Initialization Functions
def init_operate_num(stack_num):
    stack_num.top = -1

def init_operate_symbol(stack_symbol):
    stack_symbol.top = -1


## Stack Operations
def in_num_storage(stack_num, num):        # store numbers
    stack_num.top += 1
    stack_num.number[stack_num.top] = num

def in_symbol_storage(stack_symbol, ch):    # store symbols
    stack_symbol.top += 1
    stack_symbol.symbol[stack_symbol.top] = ch

def read_num_storage(stack_num):  # read numbers
    return stack_num.number[stack_num.top]

def read_symbol_storage(stack_symbol):  # read symbols
    return stack_symbol.symbol[stack_symbol.top]

def get_num_data(stack_num):   # pop number
    num = stack_num.number[stack_num.top]
    stack_num.top -= 1
    return num

def get_symbol(stack_symbol):       # pop symbol
    symbol = stack_symbol.symbol[stack_symbol.top]
    stack_symbol.top -= 1
    return symbol



## Symbol Priority and Math Operations:
def judge_symbol_priority(ch):            #  (determines priority of arithmetic operators)
    if ch == '(':
        return 1
    elif ch == '+' or ch == '-':
        return 2
    elif ch == '*' or ch == '/':
        return 3
    elif ch == ')':
        return 4

def math(v1, v2, c):           ## performs basic arithmetic operations)
    if c == '+':
        return v1 + v2
    elif c == '-':
        return v1 - v2
    elif c == '*':
        return v1 * v2
    elif c == '/':
        return v1 / v2

def main():
    
    ##  # ... (initializations)
    print("Enter the expression (no blank, no decimals): ")
    data = NumStorage()             # stack   to store numbers
    symbol = SymbolStorage()        # stack to store numbers
    init_operate_num(data)
    init_operate_symbol(symbol)
    i = t = sum_val = 0
    v1 = v2 = 0
    c = ''
    i = t = sum_val = 0
    v = [''] * 100
    user_input = input()
    
    
    for i in range(len(user_input)):
        # Handle negative numbers enclosed in parentheses
        if i == 0 and user_input[i] == '-':
            v[t] = user_input[i]
            t += 1
        elif user_input[i] == '(' and i + 1 < len(user_input) and user_input[i + 1] == '-':
            i += 1
            v[t] = user_input[i]
            t += 1
            while i < len(user_input) and user_input[i] >= '0' and user_input[i] <= '9':
                v[t] = user_input[i]
                t += 1
                i += 1
            # Convert the negative number to integer and store in the NumStorage stack
            in_num_storage(data, int(''.join(v)))
            while t > 0:
                v[t] = ''
                t -= 1
             # If the expression doesn't end with a closing parenthesis, push an opening parenthesis to the SymbolStorage stack
            if i < len(user_input) and user_input[i] != ')':
                i -= 1
                in_symbol_storage(symbol, '(')
                
        # Handle positive numbers        
        elif i < len(user_input) and user_input[i] >= '0' and user_input[i] <= '9':
            while i < len(user_input) and user_input[i] >= '0' and user_input[i] <= '9':
                v[t] = user_input[i]
                t += 1
                i += 1
            # Convert the positive number to integer and store in the NumStorage stack
            in_num_storage(data, int(''.join(v)))
            while t > 0:
                v[t] = ''
                t -= 1
            i -= 1     # Adjust the index to account for the last processed character
            
            
            
        else:
            if symbol.top == -1:
                # If the SymbolStorage stack is empty, push the current operator onto the stack
                in_symbol_storage(symbol, user_input[i])
            # Handle operators based on their priority
            elif judge_symbol_priority(user_input[i]) == 1:
                in_symbol_storage(symbol, user_input[i])
            elif judge_symbol_priority(user_input[i]) == 2:
                # Handle operators with priority 2
                if judge_symbol_priority(read_symbol_storage(symbol)) == 1:
                    in_symbol_storage(symbol, user_input[i])
                elif judge_symbol_priority(read_symbol_storage(symbol)) == 2:
                    # Perform calculations until the SymbolStorage and NumStorage stacks meet the conditions
                    while symbol.top >= 0 and data.top >= 1:
                        v2 = get_num_data(data)
                        v1 = get_num_data(data)
                        sum_val = math(v1, v2, get_symbol(symbol))
                        in_num_storage(data, sum_val)
                    in_symbol_storage(symbol, user_input[i])
                elif judge_symbol_priority(read_symbol_storage(symbol)) == 3:
                    # Similar to the case above, but with a different condition
                    while symbol.top >= 0 and data.top >= 1:
                        v2 = get_num_data(data)
                        v1 = get_num_data(data)
                        sum_val = math(v1, v2, get_symbol(symbol))
                        in_num_storage(data, sum_val)
                    in_symbol_storage(symbol, user_input[i])
                    
            # Handle operators with priority 3, 4 (similar logic to priority 2)
            elif judge_symbol_priority(user_input[i]) == 3:
                if judge_symbol_priority(read_symbol_storage(symbol)) == 1:
                    in_symbol_storage(symbol, user_input[i])
                elif judge_symbol_priority(read_symbol_storage(symbol)) == 2:
                    in_symbol_storage(symbol, user_input[i])
                elif judge_symbol_priority(read_symbol_storage(symbol)) == 3:
                    while symbol.top >= 0 and data.top >= 1:
                        v2 = get_num_data(data)
                        v1 = get_num_data(data)
                        sum_val = math(v1, v2, get_symbol(symbol))
                        in_num_storage(data, sum_val)
                    in_symbol_storage(symbol, user_input[i])
            elif judge_symbol_priority(user_input[i]) == 4:
                while symbol.top >= 0 and judge_symbol_priority(read_symbol_storage(symbol)) != 1:
                    v2 = get_num_data(data)
                    v1 = get_num_data(data)
                    sum_val = math(v1, v2, get_symbol(symbol))
                    in_num_storage(data, sum_val)
                get_symbol(symbol)
    while symbol.top != -1:           # final calculations
        v2 = get_num_data(data)
        v1 = get_num_data(data)
        sum_val = math(v1, v2, get_symbol(symbol))
        in_num_storage(data, sum_val)
    print("The result is: ", data.number[0])

main()
