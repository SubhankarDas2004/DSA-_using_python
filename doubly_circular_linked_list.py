class Node:
    def __init__(self, info):
        self.info = info
        self.next = None
        self.prev = None

class doubly_circular_linked_list:
    def __init__(self):
        self.start = None

    
    
    def insert_at_beg(self, item):
        new_node = Node(item)
        if self.start == None:
            self.start = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.start.prev
            new_node.next = self.start
            new_node.prev = last
            self.start.prev = new_node
            last.next = new_node
            self.start = new_node

    def insert_at_last(self, item):
        new_node = Node(item)
        if self.start == None:
            self.start = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.start.prev
            new_node.next = self.start
            new_node.prev = last
            last.next = new_node
            self.start.prev = new_node

    def insert_at_position(self, item, pos):
        if pos == 1:
            self.insert_at_beg(item)
            return
        
        new_node = Node(item)
        temp = self.start
        i = 1
        while i < pos - 1:
            temp = temp.next
            i = i + 1
            if temp == self.start:
                print("Position out of range")
                return
            
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
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
                new_node.prev = temp
                temp.next.prev = new_node
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
            
        last = self.start.prev
        self.start = self.start.next
        self.start.prev = last
        last.next = self.start
        del temp

    def delete_last_node(self):
        if self.start == None:
            print("List is Empty")
            return
            
        if self.start.next == self.start:
            temp = self.start
            self.start = None
            del temp
            return
            
        last = self.start.prev
        last.prev.next = self.start
        self.start.prev = last.prev
        del last

    def delete_at_position(self, pos):
        if self.start == None:
            print("List is Empty")
            return
        
        if pos == 1:
            self.delete_start_node()
            return
        
        temp = self.start
        i = 1
        while i < pos:
            temp = temp.next
            i = i + 1
            if temp == self.start:
                print("Position out of range")
                return
        
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        del temp

    def delete_specific_item(self, item):
        if self.start == None:
            print("List is Empty")
            return
        
        temp = self.start
        while True:
            if temp.info == item:
                if temp == self.start:
                    self.delete_start_node()
                    return
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                del temp
                return
            temp = temp.next
            if temp == self.start:
                break
        print("Item not found")

    def display_forward(self):
        if self.start == None:
            print("List Empty")
            return
        temp = self.start
        while True:
            print(temp.info, end=" ")
            temp = temp.next
            if temp == self.start:
                break
        

    def display_backward(self):
        if self.start == None:
            print("List Empty")
            return
        temp = self.start.prev
        last = temp
        while True:
            print(temp.info, end=" ")
            temp = temp.prev
            if temp == last:
                break
        


s1 = doubly_circular_linked_list()
s1.insert_at_last(20)
s1.insert_at_beg(10)
s1.insert_at_last(40)
s1.insert_at_position(30, 3)   
s1.insert_after_item(25, 20)
node=s1.start
print(node.prev.info)
s1.display_forward()
print()
s1.display_backward()
print()
s1.delete_start_node()         
s1.delete_last_node()       
s1.delete_at_position(2)       
s1.delete_specific_item(20)    
s1.display_forward()
print()

