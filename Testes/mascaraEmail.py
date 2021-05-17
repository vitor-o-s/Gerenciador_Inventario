s = 'matheus@mail.com'

def mask(s):
    lo = s.find('@')
    if checkEmail(s, lo) == 1:
        print("Email valido: email mascarado: " + s[0] + "###" + s[lo:])
        return 1
    else:
        print("email invalido")
        return -1

def checkEmail(s, lo):
    dominio_email = s[lo:]
    if dominio_email == '@hotmail.com' or dominio_email == '@gmail.com' or dominio_email == '@outlook.com' or dominio_email == 'yahoo.com':
        return 1
    else:
        return -1
mask(s)