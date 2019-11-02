from liststack import ListStack
__all__ = ['ListQueue']

class ListQueue():
    def __init__(self):
        self.list = list()

    # 入队
    def enqueue(self, elem):
        self.list.append(elem)
    
    # 出队
    def dequeue(self):
        try:
            rst = self.list.pop(0)
        except IndexError:
            raise IndexError("dequeue from empty queue")
        return rst
    
    def gethead(self):
        try:
            rst = self.list[0]
        except IndexError:
            raise IndexError("dequeue from empty queue")
        return rst

    def isempty(self):
        return bool(self.list)

    def reverse(self):
        stack = ListStack()
        while not isempty(self):
            stack.push(self.dequeue())
        while not isempyt(stack):
            self.enqueue(stack.pop())

    def __iter__(self):
        return self

    def __next__(self):
        try:
            rst = self.gethead()
        except IndexError:
            raise StopIteration()
        return rst



