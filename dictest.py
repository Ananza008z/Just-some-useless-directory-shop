import string

a = list(input().strip().split(','))
ditt = {a[0]:'Man', a[1]:'Non', a[2]:'Miv'}

def pas(password):
    upper = any([1 if n in string.ascii_uppercase else 0 for n in password])
    lower = any([1 if n in string.ascii_lowercase else 0 for n in password])
    special = any([1 if n in string.punctuation else 0 for n in password])
    digit = any([1 if n in string.digits else 0 for n in password])
    if 6 <= len(password) <= 12:
        if upper == True and lower == True and special == True and digit == True:
            print(ditt[password])

for i in range(len(a)):
    pas(a[i])