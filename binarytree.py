from binarynode import BinaryNode
from linkqueue import LinkQueue
from printtree import PrintTree

# tree's degree = 2
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    

    #DLR Data Left Right
    @staticmethod
    def preorder_traversal(tree, handle, end=id):
        if tree.root:
            handle(tree)
            if tree.root.left:
                BinaryTree.preorder_traversal(BinaryTree(tree.root.left), handle, end)
            if tree.root.right:
                BinaryTree.preorder_traversal(BinaryTree(tree.root.right), handle, end)
            end(tree)

    # LDR
    @staticmethod
    def inorder_traversal(tree, handle, end=id):
        if tree.root:
            if tree.root.left:
                BinaryTree.inorder_traversal(BinaryTree(tree.root.left), handle, end)
            handle(tree)
            if tree.root.right:
                BinaryTree.inorder_traversal(BinaryTree(tree.root.right), handle, end)
            end(tree)

    # LRD
    @staticmethod
    def postorder_traversal(tree, handle, end=id):
        if tree.root:
            if tree.root.left:
                BinaryTree.postorder_traversal(BinaryTree(tree.root.left), handle, end)
            if tree.root.right:
                BinaryTree.postorder_traversal(BinaryTree(tree.root.right), handle, end)
            handle(tree)
            end(tree)
    
    def print_line(self):
        rst = []
        def handle(tree):
            rst.append(tree.root.data)
        # LDR 中序遍历显示
        self.inorder_traversal(self, handle)
        rst = "binary tree => " + str(rst)
        return rst

    def print_tree(self):
        rst = PrintTree(list_=self.level_traversal()).rst
        return rst[:-1]

    def level_traversal(self):
        level = -1
        list_ = []
        def handle(tree):
            nonlocal level
            level += 1
            # list_ = [(data,level),...]
            list_.append((tree.root.data, level))
        def end(tree):
            nonlocal level
            level -= 1
        self.preorder_traversal(self, handle, end)
        return list_

    def __str__(self):
        #return self.print_line()
        return self.print_tree()
    
    def add(self, data):
        if not self.root:
            self.root = BinaryNode(data)
        elif data < self.root.data:
            if not self.root.left:
                self.root.left = BinaryNode(data)
                return
            BinaryTree(self.root.left).add(data)
        else:
            if not self.root.right:
                self.root.right = BinaryNode(data)
                return
            BinaryTree(self.root.right).add(data)
        
if __name__ == '__main__':
    t = BinaryTree()
    t.add(5)
    t.add(3)
    t.add(7)
    t.add(2)
    t.add(1)
    t.add(3.5)
    t.add(4)
    t.add(6)
    t.add(8)
    t.add(7)
    t.add(9)
    t.add(0)
    print(t)
