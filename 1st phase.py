print("\nDSA - Learning Task 2 (DS List)")

class Node(): # creating a node with user input as data
    
    def __init__(self, data = None):
        self.data = data
        self.next = None
class ArrayStack():# creating a blank array stack
    def __init__(self):
        self.head = None
    
    def __len__ (self, data = None):
        self.data = data
        return len(self.data)
    def is_empty(self, data = None):
        self.data = data
        return len(self.data) == 0
    
    #defining the insert/push method
    def push (self, e):
        self.data.append(e)
    #defining the delete/pop method
    def pop (self):
         ptr = self.head
        # CASE 0 : EMPTY LIST
         if ptr is None:
            print("\nCANNOT DELETE. ARRAY IS EMPTY.")
            return self.data.pop()
    
    def top(self):
        ptr = self.head
        if ptr is None:
            print("\nCANNOT DELETE. ARRAY IS EMPTY.")
            return self.data[-1]
    