# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Search for a value
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Traverse and print
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("None")

# Usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

print("Traversal:")
ll.traverse()  # 30 -> 20 -> 10 -> None

print("Search 20:", ll.search(40))  # True
print("Search 50:", ll.search(50))  # False
        