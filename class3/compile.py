import json
import sys

inp = json.load(sys.stdin) #["s-kaleidoscope",["define",["fn-name","n"],["ret","n"]]]
print(inp)

def compile(exp):
    out =[]
    if type(exp)==list:
        if exp[0]=='s-kaleidoscope':
            out.append('brilisp')
            for fn in exp[1:]:
                out.append(gen_fun(fn))
        else:
            raise Exception("Error- Not a s-kaleidoscope code", exp)
    else:
        raise Exception("Error- Input not in JSON")
    return out

def gen_fun(fn):
    assert fn[0] == "define"
    header = fn[1]
    name = header[0]
    args = header[1:]
    body = fn[2]

    out=[]
    out.append('define')
    
    out_header=[]
    out.append(out_header)

    namel = [name, "int"]
    out_header.append(namel)
    
    for arg in args:
        out_header.append([arg, "int"])

    out.extend(gen_body(body))
    return out

def gen_body(body):
    assert body[0] == 'ret'
    expr = body[1]
    if not isinstance(expr, list):
        return [body]
    else:
        out=[]
        operator = body[1][0]
        op1=body[1][1]
        op2=body[1][2]
        out_set=['set',['tmp','int']]
        if operator == '+':
            out_set.append(['add',op1,op2])
        elif operator == '-':
            out_set.append(['sub',op1,op2])
        elif operator == '%':
            out_set.append(['div',op1,op2])
        elif operator == '*':
            out_set.append(['mul',op1,op2])
        else:
            raise Exception("Error- Invalid operation type")
        out.append(out_set)
        out.append(['ret','tmp'])
    return out

print(json.dumps(compile(inp)))