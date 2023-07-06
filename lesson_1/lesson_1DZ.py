def palidrom(stroka): 
    a = []
    for symbol in stroka:
        a.append(symbol)
    if a == list(reversed(a)):
        return True
    else:
        return False
input = str(input())
print(palidrom(input))

