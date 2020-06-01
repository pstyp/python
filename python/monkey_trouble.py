
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling.
#  Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True 
    else: 
        return False

monkey1=bool(input("Is the first monkey smiling? (True if True leave blank if False) "))
monkey2=bool(input("Is the second monkey smiling? (True if True leave blank if False) "))

monkey_result=monkey_trouble(monkey1,monkey2)

print("Are we in trouble?", monkey_result)


# This doesn't actually work properly because non-empty strings will always convert to 'True'. Leave blank if false