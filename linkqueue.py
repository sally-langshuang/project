from node import Node
from myiterator import MyIterator

__all__ = ['LinkQueue']

class LinkQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isempty(self):
        return self.head is None

    def enqueue(self, elem):
        node = Node(elem)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
    
    def dequeue(self):
        try:
            rst = self.getnext()
        except IndexError:
            raise IndexError("dequeue from empty queue")
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return rst

    def getnext(self):
        if self.isempty():
            raise IndexError("get element from empty queue")
        return self.head.elem

    def __iter__(self):
        return MyIterator(self)

    def __repr__(self):
        rst = list("LinkQueue()")
        if not self.isempty():
            node = self.head
            while node:
                rst[-1:-1] = list(str(node.elem))
                node = node.next
                if node:
                    rst[-1:-1] = [", "]
        rst = "".join(rst)
        return rst

