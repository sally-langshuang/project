'''链表模块'''
'''linkstack module'''
from node import Node
from collections import Iterable
from myiterator import MyIterator

__all__ = ['LinkStack']

class LinkStack:
    def __init__(self,*args, reverse=False):
        # Overriding __init__. Parameters can be iterable, None,elems
        self._head = None
        if args:
            # one iterable
            if len(args) == 1 and isinstance(args[0], Iterable):
                args = args[0]
            if reverse:
                args = args[::-1]
            for item in args:
                self.push(item)
                
    def is_empty(self):
        '''判断是否是空链表'''
        return self._head is None

    def clean(self):
        self._head = None

    def push(self, elem):
        '''Add element at head'''
        self._head = Node(elem, self._head)
        
    def pop(self):
        '''Pop element from head'''
        if self._head is None:
            raise IndexError("pop from empty stack")
        rst = self._head.elem
        self._head = self._head.next
        return rst

    def getnext(self):
        if not self._head:
            raise IndexError("get element from empty stack")
        return self._head.elem

    def __repr__(self):
        '''Return a valid Python expression that could be used to recreate object'''
        node = self._head
        rst = "LinkStack()"
        list_ = list(rst)
        while node:
            list_[-1:-1] += [repr(node.elem)]
            node = node.next
            if node:
                list_[-1:-1] += ", "
        rst = "".join(list_)
        return rst

    def __str__(self):
        '''Return string that is human-readable'''
        rst = ""
        node = self._head
        while node:
            rst += str(node.elem)
            node = node.next
            if node:
                rst += "->"
        return rst

    def __iter__(self):
        return MyIterator(self)

if __name__ == '__main__':
    l = LinkStack([2,3,4])
    for item in l:
        print(item)
