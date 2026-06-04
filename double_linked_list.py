class Node:
    def __init__(self, info):
        self.info = info
        self.next = None
        self.prev = None

class double_linked_list:
    def __init__(self):
        self.start = None

    
    
    def insert_at_beg(self, item):
        new_node = Node(item)
        if self.start == None:
            self.start = new_node
        else:
            new_node.next = self.start
            self.start.prev = new_node
            self.start = new_node

    def insert_at_last(self, item):
        new_node = Node(item)
        if self.start == None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_at_position(self, item, pos):
        if pos == 1:
            self.insert_at_beg(item)
            return
        
        new_node = Node(item)
        temp = self.start
        i = 1
        while temp != None and i < pos - 1:
            temp = temp.next
            i = i + 1
        
        if temp == None:
            print("Position out of range")
            return
            
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next != None:
            temp.next.prev = new_node
        temp.next = new_node

    def insert_after_item(self, item, after_item):
        if self.start == None:
            print("List is Empty")
            return
            
        temp = self.start
        while temp != None and temp.info != after_item:
            temp = temp.next
        
        if temp == None:
            print("Item not found")
            return
            
        new_node = Node(item)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next != None:
            temp.next.prev = new_node
        temp.next = new_node

    
    
    def delete_start_node(self):
        if self.start == None:
            print("List is Empty")
            return
        
        temp = self.start
        self.start = self.start.next
        if self.start != None:
            self.start.prev = None
        del temp

    def delete_last_node(self):
        if self.start == None:
            print("List is Empty")
            return
            
        temp = self.start
        if temp.next == None:
            self.start = None
            del temp
            return
            
        while temp.next != None:
            temp = temp.next
        temp.prev.next = None
        del temp

    def delete_at_position(self, pos):
        if self.start == None:
            print("List is Empty")
            return
        
        if pos == 1:
            self.delete_start_node()
            return
        
        temp = self.start
        i = 1
        while temp != None and i < pos:
            temp = temp.next
            i = i + 1
        
        if temp == None:
            print("Position out of range")
            return
        
        if temp.next != None:
            temp.next.prev = temp.prev
        temp.prev.next = temp.next
        del temp

    def delete_specific_item(self, item):
        if self.start == None:
            print("List is Empty")
            return
        
        temp = self.start
        
        
        if temp.info == item:
            self.delete_start_node()
            return
        
        while temp != None and temp.info != item:
            temp = temp.next
        
        if temp == None:
            print("Item not found")
            return
            
        if temp.next != None:
            temp.next.prev = temp.prev
        temp.prev.next = temp.next
        del temp

    def display_forward(self):
        if self.start == None:
            print("List Empty")
            return
        temp = self.start
        while temp != None:
            print(temp.info, end=" ")
            temp = temp.next
        

    def display_backward(self):
        if self.start == None:
            print("List Empty")
            return
        temp = self.start
        while temp.next != None:
            temp = temp.next
        while temp != None:
            print(temp.info, end=" ")
            temp = temp.prev
        

s1 = double_linked_list()
s1.insert_at_last(20)
s1.insert_at_beg(10)
s1.insert_at_last(40)
s1.insert_at_position(30, 3)  
s1.insert_after_item(25, 20)  
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
s1.display_backward()
