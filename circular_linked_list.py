class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class circular_linked_list:
    def __init__(self):
        self.start = None

   
    
    def insert_at_beg(self, item):
        new_node = Node(item)
        if self.start == None:
            self.start = new_node
            new_node.next = self.start
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            new_node.next = self.start
            temp.next = new_node
            self.start = new_node

    def insert_at_last(self, item):
        new_node = Node(item)
        if self.start == None:
            self.start = new_node
            new_node.next = self.start
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.start

    def insert_at_position(self, item, pos):
        if pos == 1:
            self.insert_at_beg(item)
            return
        
        new_node = Node(item)
        temp = self.start
        i = 1
        while temp.next != self.start and i < pos - 1:
            temp = temp.next
            i = i + 1
        
        if i < pos - 1:
            print("Position out of range")
            return
            
        new_node.next = temp.next
        temp.next = new_node

    def insert_after_item(self, item, after_item):
        if self.start == None:
            print("List is Empty")
            return
            
        temp = self.start
        while True:
            if temp.info == after_item:
                new_node = Node(item)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.start:
                break
        print("Item not found")

    
    
    def delete_start_node(self):
        if self.start == None:
            print("List is Empty")
            return
        
        temp = self.start
        if temp.next == self.start:
            self.start = None
            del temp
            return
            
        last = self.start
        while last.next != self.start:
            last = last.next
        self.start = self.start.next
        last.next = self.start
        del temp

    def delete_last_node(self):
        if self.start == None:
            print("List is Empty")
            return
            
        temp = self.start
        if temp.next == self.start:
            self.start = None
            del temp
            return
            
        prev = None
        while temp.next != self.start:
            prev = temp
            temp = temp.next
        prev.next = self.start
        del temp

    def delete_at_position(self, pos):
        if self.start == None:
            print("List is Empty")
            return
        
        if pos == 1:
            self.delete_start_node()
            return
        
        temp = self.start
        prev = None
        i = 1
        while temp.next != self.start and i < pos:
            prev = temp
            temp = temp.next
            i = i + 1
        
        if i < pos:
            print("Position out of range")
            return
        
        prev.next = temp.next
        del temp

    def delete_specific_item(self, item):
        if self.start == None:
            print("List is Empty")
            return
        
        temp = self.start
        prev = None
        
        if temp.info == item:
            self.delete_start_node()
            return
        
        while temp.next != self.start and temp.info != item:
            prev = temp
            temp = temp.next
        
        if temp.info != item:
            print("Item not found")
            return
            
        prev.next = temp.next
        del temp

    def display(self):
        if self.start == None:
            print("List Empty")
            return
        temp = self.start
        while True:
            print(temp.info, end=" ")
            temp = temp.next
            if temp == self.start:
                break


s1 = circular_linked_list()
s1.insert_at_last(20)
s1.insert_at_beg(10)
s1.insert_at_last(40)
s1.insert_at_position(30, 3)  
s1.insert_after_item(25, 20)  
s1.display()
print()
s1.delete_start_node()        
s1.delete_last_node()       
s1.delete_at_position(2)    
s1.delete_specific_item(20) 
s1.display()
