# This is a python script to reverse the nodes of a singly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while (current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

        # Function to insert a new node at the beginning of linked list

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def displayList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Driver program to test above functions
obj = LinkedList()
obj.insert(7)
obj.insert(8)
obj.insert(4)
obj.insert(6)

print("Given Linked List")
obj.displayList()
obj.reverse()
print("The reverse order is : ")
obj.displayList()