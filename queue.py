class queue():
    def __init__(self):
        self.que=[0]*10
        self.front=-1
        self.rear=-1
        self.size=len(self.que)

    def insert(self,item):
        if self.front==self.size-1:
            print("queue is full!!!")
            return
        else:
            self.front=self.front+1
            self.que[self.front]=item
            if self.rear==-1:
                self.rear=0
            '''print("inserted",item)'''
    def delete(self):
        if self.rear==-1:
            print("undeflow!!!")
            return
        else:
            item=self.que[self.rear]
            if self.front==self.rear:
                self.front=-1
                self.rear=-1
            else:
                self.rear=self.rear+1
            '''print("deleted",item)'''
    def display(self):
        for i in range(self.front,0,-1):
            print(self.que[i],end=",")

q1=queue()
q1.insert(20)
q1.insert(30)
q1.delete()
q1.display()
            
