class StackIterator:
    def __init__(self, stack):
        self.stack = stack

    def __next__(self):
        return self.stack.gettop()
