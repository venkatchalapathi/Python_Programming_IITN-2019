# Email validation

def isEmailValid(email):
    pattern = '^([a-z0-9][a-z0-9_.]{4,13}[0-9a-z]+)@([a-zA-Z0-9]{4,16}[a-z0-9]+).([a-zA-Z]{2,4})$'
    if re.match(pattern,email):
        return True
    return False
    

import re

def phoneValidator(number):
    pattern = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    
    if re.match(pattern,str(number)):
        return True
    else:
        return False