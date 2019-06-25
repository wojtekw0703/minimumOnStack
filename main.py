def minimumOnStack(operations):
    stack = []
    ans = []
    for op in operations:
        if op == 'min':
            ans.append(stack[-1])
        elif op == "pop":
            stack.pop()
        else:
            n = int(op.split()[1])
            if stack:
                stack.append(min(stack[-1], n))
            else:
                stack.append(n)
    return ans

operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"]
print(minimumOnStack(operations))
