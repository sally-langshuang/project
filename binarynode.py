class BinaryNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add_left(self, data):
        if self:
            self.left = BinaryNode(data)

    def add_right(self, data):
        if self:
            self.right = BinaryNode(data)
