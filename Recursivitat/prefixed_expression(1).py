import yogi

def prefixed_expression()-> int:

    for token in yogi.tokens(str):
        a = prefixed_expression()
        b = prefixed_expression()
        if token=="*":
           return a * b
        elif token=="+":
            return a + b
        elif token=="-":
            return a - b
        return(int(str))
    

print(prefixed_expression())