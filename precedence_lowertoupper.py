inputString = input('Enter a string')
words = inputString.split()
lower = []
upper = []
for char in inputString:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print("\n arranging characters giving precedence to lowercase letters:")
print(sortedString)
