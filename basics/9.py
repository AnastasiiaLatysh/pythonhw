def brackets_are_balanced(brackets):
    #remove spaces
    while brackets[0] == ' ':
        brackets = brackets[1:]

    stack = []
    unused = 0
    amount = len(brackets)
    for i in range(amount):
        if brackets[i] == '[':
           stack.append(brackets[i])
        elif brackets[i] == ']':
            if len(stack) > 0:
                stack.pop()
            else:
                unused += 1
        print(stack)

    if (len(stack) == 0) & (unused == 0):
        print(brackets, 'OK')
    else:
        print(brackets, 'NOT OK')


brackets = input('Enter brackets in arbitrary order :\n')
brackets_are_balanced(brackets)