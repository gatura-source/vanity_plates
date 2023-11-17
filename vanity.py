"""
The Script Checks Vanity Plates validity
"""
import string
import sys

DIGITS = string.digits
ALPHA = string.ascii_uppercase
SPECIAL_CHARS = string.punctuation



def check_len(stack):
    return not (len(stack) > 6 or len(stack) < 2)
def op_check_first_two(stack):
    top_= stack.pop(0)
    next_top = stack.pop(0)
    top_two = top_ + next_top
    for char in top_two:
        if char not in ALPHA:
            return False
    return True
def check_plate(stack):
    f_num = False
    while stack != []:
        #print(stack)
        char = stack.pop(0)
        if char in DIGITS and not f_num and char != '0':
            f_num = True
        elif char in ALPHA and f_num:
            return False
        elif char == '0' and not f_num:
            return False
        elif char in SPECIAL_CHARS:
            return False
        else:
            continue
    return True
stack = []
inp = input('Enter your plate here:: ')
for c in inp:
    if c in string.ascii_lowercase:
        stack.append(c.upper())
    else:
        stack.append(c)
print(f"NOTE: all chars are converted to uppercase\n\nInput:: {stack}")
ops = {1: check_len,
       3: op_check_first_two,
       5: check_plate,
       2: 'len > 6 or len < 2',
       6: 'First 2 chars not alphabet',
       10:'Either contains a special char, or 0 as the first number or char after first number'}
for k, v in ops.items():
    if k in range(1, 6, 2):
        res = v(stack)
        if res == False:
            print(f"Terminated.\nReason:: Plate {ops[k*2]}")
            sys.exit(0)
print("Plate is valid")
