class BinaryNode:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def add_left(self, item):
        if self:
            self.left = BinaryNode(item)

    def add_right(self, item):
        if self:
            self.right = BinaryNode(item)
