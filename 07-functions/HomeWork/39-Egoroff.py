print('\nA. Красивый год')


def year(y):
    y += 1
    if len(set(str(y))) != 4:
        return year(y)
    return y


# print(year(int(input())))
print(year(1987))

print('\nA. cAPS lOCK')


def caps_lock(s):
    if len(s) == 1:
        if s.islower():
            print(s.upper())
        else:
            print(s.lower())
    else:
        if s.isupper():
            print(s.lower())
        elif s[0].islower() and s[1:].isupper():
            print(s[0].upper() + s[1:].lower())
        else:
            print(s)


# caps_lock(input())
caps_lock('cAPS')
caps_lock('Lock')
caps_lock('hELLO')
caps_lock('HTTP')
caps_lock('z')
caps_lock('cAPSlOCK')
