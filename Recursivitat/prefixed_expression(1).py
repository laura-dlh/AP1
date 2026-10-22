from yogi import read

def prefixed_expression () -> int:

    token = read(str)

    if token == "+":
        return prefixed_expression() + prefixed_expression()
    elif token == "-":
        return prefixed_expression() - prefixed_expression()
    elif token == "*":
        return prefixed_expression() * prefixed_expression()
    else:
        return int(token)

print(prefixed_expression())
