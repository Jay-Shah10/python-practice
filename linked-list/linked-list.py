class Node: 
    def __init__(self, value) -> None:
        self.data = value
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        """
        Have a pointer at the head. While the pointer is not None print all the values. 
        """
        temp = self.head
        while temp is not None: 
            print(temp.data)
            temp = temp.next





def main(): 
    n = LinkedList()
    n.head = Node("mon")
    n2 = Node("tue")
    n3 = Node("wed")

    n.head.next = n2 # linking head to e2
    n2.next = n3 # linking n2 to n3
    n3.next = None # making n3  tail.

    n.printList() 

    

if __name__ == "__main__":
    main()