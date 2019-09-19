import fire


class Node:
    """
    Implement a class to represent a Node, on python we don't have pointers
    but support reference to objects
    """
    def __init__(self, val, next_element=None, prev_element=None):
        self.val, self.next, self.prev = val, next_element, prev_element

    # Override to be able to print the Node value
    def __str__(self):
        return str(self.val)


class LinkedList:
    """
    Implement Linked List Algorithm
    """
    def __init__(self):
        self.head = None
        self.last = None
        self.counter = 0

    def append(self, val):
        node = Node(val)
        if self.head is not None:
            # Not First element
            node.prev = self.last
            self.last.next = node
        else:
            # First element
            self.head = node
        self.last = node
        self.counter += 1

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.last:
            self.last = self.last.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        self.counter -= 1

    def __str__(self):
        curr = self.head
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return str(vals)

    def __len__(self):
        return self.counter

    # Override the linked_list[key] operator
    def __getitem__(self, key):
        curr = self.head
        times = 0
        while curr:
            prev_curr = curr
            curr = curr.next
            times += 1
            if times > key:
                return prev_curr


# Testing ....
linked_list = LinkedList()
linked_list.append(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
print('Linked List:', linked_list, 'len:', len(linked_list))
print('Element key=4 :', linked_list[4])
# Remove element
linked_list.remove(linked_list[4])
print('Linked List:', linked_list, 'len:', len(linked_list))
print('Element key=2 :', linked_list[2])
