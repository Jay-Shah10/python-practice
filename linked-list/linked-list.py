class Node: 
    def __init__(self, value) -> None:
        self.data = value
        self.next = None
    
class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    

    def append(self, value): 
        """
        Adding in a new value to the single linked list. 
        """
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        """
        Adding a new node at the front of the single linked list. 
        """

        new_node = Node(value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True

    def pop(self):
        """
        Removing the last item from the linked list.
        """
        if self.length == 0: 
            return None
        # two pointers that are needed.
        temp = self.head
        pre = self.head

        while temp.next is not None: 
            pre  = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0: 
            self.head = None
            self.tail = None
        
        return temp
    
    def popfirst(self):
        """
        used to remove the first item in the list. 
        """

        if self.length == 0: 
            return None
        
        # pointer temp points to the head. 
        # move head over to the next node (head.next)
        # temp.next is now none - it is now detached. 
        # decrease lenght.
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1 

        if self.length == 0: 
            self.tail = None
        
        return temp
    
    def get(self, index): 
        if index < 0 or index > self.length: 
            return None

        # pointer to the head. 
        # iterate the linked list to the index.
        # pointer is now the value of next. 
        # return temp
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert (self, index, value):
        if index < 0 or index > self.length: 
            return None
        if index == 0: 
            self.prepend(value)
        if index == self.length: 
            self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1) # temp is pointing to the node before the index value. 
        new_node.next = temp.next # replace new node's next with the previous node's next. 
        temp.next = new_node # previous node's next value is now pointed to the new node.  
        self.length += 1
        return True







    def printList(self):
        """
        Have a pointer at the head. While the pointer is not None print all the values. 
        """
        temp = self.head
        while temp is not None: 
            print(temp.data)
            temp = temp.next





def main(): 
    n = LinkedList("mon")
    n.append("tue")
    n.append("wed")

    n.printList()

    n.pop()
    n.printList()
    

    

if __name__ == "__main__":
    main()