class stack():
    def __init__(self):
        self.stk=[0]*10
        self.top=-1
        self.size=len(self.stk)

    def push(self,element):
        if self.top==self.size-1:
            print("Stack overflow!!!")
            return
        else:
            self.top=self.top+1
            self.stk[self.top]=element
            '''print(element,"pushed")'''
    def pop(self):
        if self.top==-1:
            print("stack underflow!!!")
            return
        else:
            element=self.stk[self.top]
            self.top=self.top-1
            '''print(element,"poped")'''

    def display(self):
        for i in range(0,self.top+1):
            print(self.stk[i],end=" ")


s1=stack()
s1.push(10)
s1.push(20)
s1.pop()
s1.display()
