string = input()
chars = []

for el in string:
    chars.append(el)

result = ''

while chars:
    result += chars.pop()

print(result)