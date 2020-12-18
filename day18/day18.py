with open("input.txt") as f:
    data = "+".join(f"({r})" for r in f.readlines())
    expression = [
        t if t in "()+*" else int(t)
        for t in data.strip().replace("(", " ( ").replace(")", " ) ").split()
    ]


def infix_to_postfix(expression, priority):
    stack, postfix = [], []

    for token in expression:
        if isinstance(token, int):
            postfix.append(token)
        elif token == "(":
            stack.append("(")
        elif token == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and priority[token] <= priority[stack[-1]]:
                postfix += stack.pop()
            stack.append(token)

    postfix += stack[::-1]

    return postfix


def eval_postfix(expr):
    stack = []
    while expr:
        token = expr.pop(0)
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(token)

    return stack[0]


print("Part 1", eval_postfix(infix_to_postfix(expression, {"+": 1, "*": 1})))
print("Part 2", eval_postfix(infix_to_postfix(expression, {"+": 2, "*": 1})))
