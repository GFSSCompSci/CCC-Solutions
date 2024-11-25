#Written By Arghya Vyas
breaker = 0
solutions = []

while breaker == False:
    expression = input().strip()
    if expression == '0':
        breaker = 1
    else:
        expression = expression.split()[::-1]
        stack = []

        for token in expression:
            if token.isdigit():
                stack.append(token)
            elif token in '+-':
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = operand1 + ' ' + operand2 + ' ' + token
                stack.append(result)

        solutions.append(stack.pop())

for solution in solutions:
    print(solution)
