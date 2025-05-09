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

        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def Insert_Node_At_End(self, data):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        new_node = Node(data)
        current_node.next = new_node

    def delete_head(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current_node = self.head
        self.head = current_node.next

    def delete_at_index(self, index):
        if self.head is None:
            print("Linked List is empty")
            return

        if index == 0:
            self.delete_head()
            return

        current_node = self.head
        position = 0

        while current_node is not None and position < index - 1:
            position += 1
            current_node = current_node.next

        if current_node is None or current_node.next is None:
            print("List empty at index")
            return
        current_node.next = current_node.next.next

    def delete_last_node(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current_node = self.head
        while current_node.next is not None and current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def search(self, data):
        current_node = self.head

        while current_node.next is not None:
            if current_node.data == data:
                return current_node
            else:
                current_node = current_node.next

        print("Item not found")



