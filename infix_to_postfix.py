def inf_pf(e):
    prec={"+":1, "-":1, "*":2, "/":2, "^":3}
    stack=[]
    post=[]

    for char in e:
        if char.isalnum():
            post.append(char)

        elif char=="(":
            stack.append(char)

        elif char==")":
            while stack and stack[-1]!="(":
                post.append(stack.pop())
            stack.pop()

        elif char in prec:
            while stack and stack[-1]!="(":
                post.append(stack.pop())
            stack.append(char)
    while stack:
        post.append(stack.pop())
    return post

infix="5*(6+2)-12/4"
post=inf_pf(infix)
print(infix)
print(post)
