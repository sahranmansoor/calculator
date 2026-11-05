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
            while i < l and (s[i].isdigit() or s[i] == "."):
                n_str += s[i]
                i += 1
            n = float(n_str) if "." in n_str else int(n_str)
            tokens.append(("NUMBER", n))
        elif cc == "+" or cc == "-" or cc == "/" or cc == "*":
            tokens.append(("OPERATION", cc))
            i += 1
        elif cc == "(" or cc == ")":
            tokens.append(("SYMBOL", cc))
            i += 1
        else:
            raise SyntaxError(f"unknown symbol: {cc}")
            
    tokens.append(("EOF", None))
    return tokens

def presedence(op):
    if op in ('+', '-'): return 1
    if op in ('*', '/'): return 2
    return 0

def infix_to_postfix(tokens):
    pf = []
    ops = []

    for tt, tv in tokens:
        if tt == "EOF":
            break

        elif tt == "NUMBER":
            pf.append(tv)

        elif tt == "SYMBOL":
            if tv == "(":
                ops.append(tv)

            elif tv == ")":
                while ops and ops[-1] != "(":
                    pf.append(ops.pop())

                if not ops:
                    raise SyntaxError("mismatched parentheses")

                ops.pop()

        elif tt == "OPERATION":
            while ops and ops[-1] != "(" and presedence(ops[-1]) >= presedence(tv):
                pf.append(ops.pop())

            ops.append(tv)

    while ops:
        if ops[-1] == "(":
            raise SyntaxError("mismatched parentheses")
        pf.append(ops.pop())

    return pf

def evalvate_postfix(pf):
    res = []

    for t in pf:
        if isinstance(t, (int, float)):
            res.append(t)
        else:
            if len(res) < 2:
                raise SyntaxError("invalid expression")

            r = res.pop()
            l = res.pop()

            if t == "+":
                res.append(add(r, l))
            elif t == "-":
                res.append(sub(l, r))
            elif t == "*":
                res.append(mul(r, l))
            elif t == "/":
                res.append(div(l, r))
                
    if len(res) != 1:
        raise SyntaxError("invalid expression")
        
    return res[0]

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y):
    if y == 0:
        raise ZeroDivisionError("can not divide by zero")
    return x / y

def main():
    print("Type 'exit' to quit.\n")
    
    while True:
        try:
            s = input('calc > ')
        except (EOFError, KeyboardInterrupt):
            break

        s = s.strip()
        if not s:
            continue

        if s.lower() == 'exit':
            print("Exiting...")
            break

        try:
            ts = tokenize(s)
            pf = infix_to_postfix(ts)
            res = evalvate_postfix(pf)

            if isinstance(res, float) and res.is_integer():
                res = int(res)
            print(res)

        except SyntaxError as e:
            print(f"SYNTAX ERROR: {e}")
        except ZeroDivisionError as e:
            print(f"MATH ERROR: {e}")

if __name__ == '__main__':
    main()
