def pf_eval(e):
    stack = []
    for char in e:
        if char.isdigit():
            stack.append(int(char))
        elif char == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif char == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b) 
        elif char == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif char == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b) 
    return stack.pop()

post = ['5','6','2','+','*','12','4','/','-']
print(pf_eval(post)) 
