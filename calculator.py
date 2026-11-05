def tokenize(s):
    tokens = []

    i = 0
    l = len(s)

    while i < l:
        cc = s[i]

        if cc.isspace():
            i += 1
        elif cc.isdigit() or cc == ".":
            n_str = ""
            while i < l and ( s[i].isdigit() or s[i] == "."):
                n_str += s[i]
                i += 1
            n = float(n_str) if "." in n_str else int(n_str)
            tokens.append(("NUMBER", n))
        elif cc == "+" or cc == "-" or cc == "/" or cc == "*":
            tokens.append(("OPERATION", cc))
            i += 1
        elif cc == "(" or cc == ")":
            tokens.append(("SYMBOL", cc))
        else:
            raise SyntaxError(f"unknown symbol: {cc}")
    tokens.append(("EOF", None))
    return tokens

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

def main():
    print("Type 'exit' to quit.\n")
    
    while True:
        try:
            text = input('calc > ')
        except (EOFError, KeyboardInterrupt):
            break

        text = text.strip()

        if not text:
            continue

        if text.lower() == 'exit':
            print("Exiting...")
            break

        ans = parse(text)
        print(f"= {ans}")

if __name__ == '__main__':
    main()
