def parse(x):
    tokens = x.split()
    
    i = 0
    l = len(tokens)

    ans = None
    op = None

    while i < l:
        if tokens[i] == "+":
            op = "+"
        elif tokens[i] == "-":
            op = "-"
        elif tokens[i] == "/":
            op = "/"
        elif tokens[i] == "*":
            op = "*"
        else:
            if op == None:
                ans = float(tokens[i])
            else:
                ans = eval(op, ans, float(tokens[i]))
        i += 1
    return ans

def eval(op, x, y):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y != 0:
            return x / y
        else:
            return "divide by zero not allowed"




x = input("write an expression to evalvate or exit to exit")

ans = parse(x)

print(ans)
