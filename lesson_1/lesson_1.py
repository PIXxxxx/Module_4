# def strcount(string): # сложность  O(n ** 2)
#     for symbol in string:
#         counter = 0
#         for sub_symbol in string:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)

# strcount('abcdceeea')

# def strcount(string): # сложность O(n * m)
#     for symbol in sorted(set(string)):
#         counter = 0
#         for sub_symbol in string:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)

# strcount('abcdceeea')

def strcount(string): # сложность O(n * m)
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
    print(syms_counter)
strcount('aaabbcdeee')