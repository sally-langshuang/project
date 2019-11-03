class MyIterator:
    def __init__(self, stack):
        self.stack = stack
        self.traversal = self.stack._head

    def __next__(self):
        if not self.traversal:
            raise StopIteration
        rst = self.traversal.elem
        self.traversal = self.traversal.next
        return rst
        
