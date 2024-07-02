f= open("x.sexp")
a=f.read()
print(a)

def tokenize(s):
    tokens = []
    word = ""
    i = 0
    
    while i < (len(s)-1):
        if s[i] == "(" or s[i] == ")":
            tokens.append(s[i])
            i += 1
        elif s[i] == " ":
            i += 1
        else:
            while i < len(s) and s[i] not in ("(", ")", " "):
                word += s[i]
                i += 1
            tokens.append(word)
            word = ""    
    return tokens


b=tokenize(a)
#print(b)


def parse(tokens):
    token=tokens.pop(0)
    if token=='(':
        L=[]
        while tokens[0] != ')':
            L.append(parse(tokens))
        tokens.pop(0)
        return L
    else:
        try:
            return int(token)
        except ValueError:
            try:
                return float(token)
            except ValueError:
                return token

c=parse(b)
print(c)

def evaluate(s,env):
    if type(s)==int:
        return s
    elif type(s)==list:
        operator = s[0]
        if operator == '+':
            return evaluate(s[1],env) + evaluate(s[2],env)
        elif operator == '-':
            return evaluate(s[1],env) - evaluate(s[2],env)
        elif operator == '*':
            return evaluate(s[1],env) * evaluate(s[2],env)
        elif operator == '/':
            return evaluate(s[1],env) / evaluate(s[2],env)
        elif operator == 'let':
            for exp in s[1]:
                env[exp[0]]=evaluate(exp[1],env)
            return evaluate(s[2],env)
        elif operator == 'lambda':
            return s
        elif operator in env:
            l=env[operator]
            arg=l[1]
            func=l[2]
            for k in range (len(arg)):
                env[arg[k]] = evaluate(s[k+1],env)
            return evaluate(func,env)

        else:
            raise Exception("Expression is wrong")
    else:
            if type(s)==str:
                if s in env:
                    return env[s]
                else:
                    raise Exception("ERROR - not defined variable!!!!")
            elif type(s)==int or type(s)==float:
                return s
            else:
                raise Exception("ERROR!!!!")

env={}
d=evaluate(c,env)
print(d)
