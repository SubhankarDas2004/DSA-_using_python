class node:
    def __init__(self, item):
        self.info= item
        self.next=None

class linked_list:
    def __init__(self):
        self.start=None

    def insert_at_last(self, item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            return
        temp=self.start
        while temp.next!=None:
            temp=temp.next
        temp.next=nd

    def insert_at_begin(self, item):
        nd=node(item)
        nd.next=self.start
        self.start=nd

    def insert_at_position(self, item, pos):
        if pos==1:
            self.insert_at_begin(item)
        else:
            nd=node(item)
            i=1
            temp=self.start
            while temp.next!=None and i<pos:
                prev=temp
                temp=temp.next
                i=i+1
            if temp.next==None:
                temp.next=nd
                return
            nd.next=temp
            prev.next=nd

    def insert_after_specific_item(self, item, specific_item):
        nd=node(item)
        temp=self.start
        while temp.next!=None and temp.info!=specific_item:
            temp=temp.next
        nd.next=temp.next
        temp.next=nd

    def delete_start_node(self):
        temp=self.start
        self.start=temp.next
        del temp

    def delete_last_node(self):
        temp=self.start
        while temp.next!=None:
            prev=temp
            temp=temp.next
        prev.next=None
        del temp

    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.info)
            temp=temp.next

s1=linked_list()
s1.insert_at_last(10)
s1.insert_at_last(20)
s1.insert_at_begin(30)
s1.insert_at_position(15,2)
s1.insert_after_specific_item(25, 30)
s1.delete_start_node()
s1.delete_last_node()
s1.display()
        
