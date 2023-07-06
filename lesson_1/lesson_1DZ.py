def palidrom(stroka):
    a = []
    for symbol in stroka:
        a.append(symbol)
    if a == list(reversed(a)):
        return True
    else:
        return False
vvod = str(input())
print(palidrom(vvod))

