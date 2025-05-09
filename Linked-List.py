
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Insert_Node_At_Start(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def Insert_Node_At_Index(self, data, index):
        if index == 0:
            self.Insert_Node_At_Start(data)

        current_node = self.head
        position = 0







