# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution: 
def mergeTwoLists(list1, list2) -> list: 
    if list1 is None: return list2
    if list2 is None: return list1
    
    head = ListNode()
    
    if list1.val <= list2.val: 
        head = list1
        list1 = list1.next
    else: 
        head = list2
        list2 = list2.next
    
    head.next = self.mergeTwoLists(list1, list2)
    return head
    
# space O(m+n)
# Time O(m+n)


# -------------------------------

# Solution two with itertion: 

def mergeTwoLists(list1, list2) -> list: 

    # two pointers. both at head and tail to keep track of the last item. 
    head = ListNode()
    tail = head 

    # iterate until we reach end of one list. 
    while list1 is not None and list2 is not None: 
        #compare the two heads of the list. 
        if list1.val  <  list2.val: 
            tail.next = list1 
            list1 = list1.next
        else: 
            tail.next = list2
            list2  = list2.next
        
        tail = tail.next # to get to the last value. 

        tail.next  = list1 if list1 is not None else list2 
        return head.next 
"""
space: O(1)
time: O(m+n)
"""