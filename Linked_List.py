# [10] -> [20] -> [30] -> None
# O(n) | O()


class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
        
    
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        pass

    def __contains__(self):
        pass
    
    def __len__(self):
        pass
    
    # create a new node if empty [10] -> [20] -> [5]
    def append(self, value): 
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)
    
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node
    
    def insert(self, value):
        pass
    
    def delete(self, value):
        pass
    
    def pop(self, index):
        pass
    
    def get(self, index):
        pass
    
    def print(self):
        pass
    
    if __name__ == "__main__":
        pass
        