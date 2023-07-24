def infix_to_postfix(infix):
    stack = []
    postfix = ''
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for char in infix:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(char)
    while stack:
        postfix += stack.pop()
    return postfix

print(infix_to_postfix("a*(b+c)/(d-e)"))        # "a*(b+c)/(d-e)" is the infix/expresion here.