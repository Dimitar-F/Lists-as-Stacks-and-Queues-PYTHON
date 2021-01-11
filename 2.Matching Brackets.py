expression = input()

s = []

for i in range(len(expression)):
    char = expression[i]
    if char == '(':
        s.append(i)
    elif char == ')':
        j = s.pop()
        print(expression[j:i + 1])
