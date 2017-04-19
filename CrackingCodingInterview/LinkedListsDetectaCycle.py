"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    traveled_list = {}
    current = head
    while (current != None):
        if current in traveled_list:
            traveled_list[current]+=1
        else:
            traveled_list[current]=1
        if traveled_list[current] > 1:
            return True
        current = current.next
    return False



