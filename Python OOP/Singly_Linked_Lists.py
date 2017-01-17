class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def addFront(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new
        if not self.tail:
            self.tail = new
        return self

    def addBack(self, val):
        new = Node(val)
        if self.tail:
            self.tail.next = new
            self.tail = new
        else:
            self.head = self.tail = new
        return self

    def insertBefore(self, nextVal, val):
        new = Node(val)
        if self.head.value == nextVal:
            new.next = self.head
            self.head = new
            return self
        curr = self.head
        while curr.next:
            if curr.next.value == nextVal:
                new.next = curr.next
                curr.next = new
                return self
            curr = curr.next
        print "Couldn't insert!"
        return self

    def insertAfter(self, preVal, val):
        new = Node(val)
        if self.tail.value == preVal:
            self.tail.next = new
            self.tail = new
            return self
        curr = self.head
        while curr:
            if curr.value == preVal:
                new.next = curr.next
                curr.next = new
                return self
            curr = curr.next
        print "Couldn't insert!"
        return self

    def removeNode(self, val):
        if self.head.value == val:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = self.tail = None
        curr = self.head
        while curr.next:
            if curr.next.value == val:
                if self.tail == curr.next:
                    curr.next = None
                    self.tail = curr
                else:
                    curr.next = curr.next.next
                return self
            curr = curr.next
        print "Couldn't remove!"
        return self

    def reverseList(self):
        

    def printAllVals(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(str(curr.value))
            curr = curr.next
        print " ==> ".join(vals)


list = SinglyLinkedList()
# list.addFront(1).addFront(2).addBack(3).addBack(4).printAllVals()
list.addFront(1).addFront(3).addBack(2).addBack(3).printAllVals()
list.removeNode(1).printAllVals()
