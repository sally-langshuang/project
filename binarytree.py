from binarynode import BinaryNode

# tree's degree = 2
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def level_traversal(self):
        pass

    #DLR Degree Left Right
    def preorder_traversal(self, node, handle=print):
        if self.root:
            handle(node.item)
            if node.left:
                self.preorder_traversal(node.left, handle)
            if node.right:
                self.preorder_traversal(node.right, handle)

    # LDR
    def inorder_traversal(self, node, handle=print):
        if node:
            if node.left:
                self.inorder_traversal(node.left, handle)
            handle(node.item)
            if node.right:
                self.inorder_traversal(node.right, handle)

    # LRD
    def postorder_traversal(self, node, handle=print):
        if node:
            if node.left:
                self.postorder_traversal(node.left, handle)
            if node.right:
                self.postorder_traversal(node.right, handle)
            handle(node.item)
    
    def __str__(self):
        rst = []
        def handle(item):
            rst.append(item)
        # LDR 中序遍历显示
        self.inorder_traversal(self.root,handle)
        rst = "binary tree => " + str(rst)
        return str(rst)
    
    def add(self, item):
        if not self.root:
            self.root = BinaryNode(item)
        elif item < self.root.item:
            if not self.root.left:
                self.root.left = BinaryNode(item)
                return
            BinaryTree(self.root.left).add(item)
        else:
            if not self.root.right:
                self.root.right = BinaryNode(item)
                return
            BinaryTree(self.root.right).add(item)
        
if __name__ == '__main__':
    t = BinaryTree()
    t.add(5)
    t.add(3)
    t.add(7)
    t.add(2)
    t.add(4)
    t.add(6)
    t.add(8)
    print(t)
