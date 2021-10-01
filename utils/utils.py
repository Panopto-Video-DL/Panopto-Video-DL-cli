
def input_yesno(*args) -> bool:
    r = None
    while r not in ['Y', 'N']:
        r = input(*args).upper()
        if r == 'Y':
            return True
        elif r == 'N':
            return False
        else:
            print('Invalid input. Use Y or N', end='\n\n')
