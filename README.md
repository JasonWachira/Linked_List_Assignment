# Linked List Implementation
## Group Members:
* Arnold Richard - 172340
* Jason  Wachira - 172995
* Mitchelle Chitsaka - 190012
---
## Created Node Class
We created a node class and defined a constructor with data passed as an argument and a reference of the next node initialized to none because if we are to instantiate the Node it will only be itself with no reference to the next one. 
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```
---
## Created a linked list class
Set `self.head` to `None` as the linked list is empty when created.
```python
class LinkedList:
    def __init__(self):
        self.head = None
```
### Defined a method for adding a node to the linked list
Used a for loop to check if the linked list is empty. If it is, we se the new node as the head, else we set `self.next` as the new node.
```python
    def Insert_Node_At_Start(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
```

### Defined a method for inserting a node at an index
If the provided index is `0`, call `Insert_Node_At_Start()`
```python
    def Insert_Node_At_Index(self, data, index):
        if index == 0:
            self.Insert_Node_At_Start(data)
```
Otherwise, we initialize two new variables, one for the current node and another for the index position.
```python
current_node = self.head
position = 0
```

We then used a while loop to iterate through the whole linked list while not going out of bounds of our current linked list.<br>
We have to stop just before the previous index so as to insert the data as the previous node will be pointing to the next node.
```python
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
```
### Defined a method for adding the node at the end
We first check if the linked list is empty. If it is we throw the error.
```python
    def Insert_Node_At_End(self, data):
        if self.head is None:
            print("Linked List empty")
            return
```
Else we iterate through the linked list and stop at the last node. as the next node for the last node will be `Null`<br>
```python
current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        new_node = Node(data)
        current_node.next = new_node
```

### Defined a methode for deleting the head
We check if list is empty, if not we have a temporary node(`current_node`) and assign it to `self.head` <br>
We then have the head(`self.head`) as `current_node.next`<br>

```python
    def delete_head(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current_node = self.head
        self.head = current_node.next
```

### Defined a method for deleting at index
We terminate the function if the linked list is empty.<br>
```python
    if self.head is None:
        print("Linked List is empty")
        return
```
We then call the function that deletes the head if index is zero.
```python
    if index == 0:
        self.delete_head()
        return
```
We iterate the linked list and stop right before the index we want to delete as that node will point to the node we want to delete.<br>
We also return list is empty if the current node we want to delete is empty or if it points to an empty node since we stoped right before the node we want to delete, and we can't delete an empty node.<br>
Other wise we just delete by skipping it `current_node.next = current_node.next.next`
```python
        while current_node is not None and position < index - 1:
            position += 1
            current_node = current_node.next

        if current_node is None or current_node.next is None:
            print("List empty at index")
            return
        current_node.next = current_node.next.next
```

### Defining a method to delete the last node
We do the obvious, check if the list is empty.<br>
We then use a while loop to iterate through 