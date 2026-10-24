import yogi

def prefixed_expression2():
    for token in yogi.tokens(str):
        if token == "+":
            return prefixed_expression2() + prefixed_expression2()  
        elif token == "-":
           return - prefixed_expression2()
        elif token == "m":
            return max(prefixed_expression2(),prefixed_expression2(),prefixed_expression2())
        return int(token)


print(prefixed_expression2())