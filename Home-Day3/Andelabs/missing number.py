a = [2, 5, 7, 8, 4]
b = [2, 5, 7, 8, 4, 9, 10, 10]

if len(a) == 0 and len(b) == 0:
    print('Lists are empty')
elif len(a) == len(b):
    print('The lists are similar')
elif len(a) > len(b):
    print('List a is larger')
elif len(a) < len(b):
    pos = [item for item in b if item not in a]
    print(pos)
