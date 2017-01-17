class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    # def __str__(self):
    #     return str(self.value)

class Doubly_Linked_List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            current = Node(value)
            self.tail.next = current
            current.prev = self.tail
            self.tail = current
        return self

    def insert(self, value, ins_val):
        node = self.head
        current = Node(value)
        while node:
            if node.value == ins_val:
                node.prev.next = current
                current.prev = node.prev
                current.next = node
                node.prev = current
                return self
            node = node.next
        print "Cannot insert!"
        return self

    def delete(self, del_val):
        node = self.head
        while node:
            if node.value == del_val:
                if node.prev and node.next:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                elif node.prev:
                    self.tail = node.prev
                    node.prev.next = None
                elif node.next:
                    self.head = node.next
                    node.next.prev = None
                else:
                    self.head = None
                    self.tail = None
                return self
            node = node.next
        print "Cannot delete!"
        return self

    def list_print(self):
        vals = []
        node = self.head
        while node:
            vals.append(str(node.value))
            node = node.next
        print " ==> ".join(vals)

dll = Doubly_Linked_List()
dll.append(1).append(2).append(3).append(4).insert(5,4).insert(6,5).delete(3).list_print()
