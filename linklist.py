'''链表模块'''
'''linklist module'''
from node import Node
from collections import Iterable

__all__ = ['LinkList']

class LinkList:
    class Iterator:
        '''迭代器类（嵌套子类）'''
        # Class for iterator of link list for traversal
        def __init__(self, llist):
            # 有效节点为第二节点
            self.node = llist._head.next
    
        # for next(), for...
        def __next__(self):
            while self.node:
                rst = self.node.elem
                self.node = self.node.next
                return rst
            raise StopIteration
    
    def __init__(self,*args, reverse=False):
        '''初始化可以不穿参、传入单元素、多元素或一个可迭代对象。'''
        # Overriding __init__. Parameters can be iterable, None,elems
        # 头结点记录个数
        self._head = Node(0)
        if args:
            if len(args) == 1 and isinstance(args[0], Iterable):
                args = args[0]
            if reverse:
                args = [::-1]
            self._head.elem  = len(args)
            node = self._head.next
            for item in args:
                node = Node(item)
                node = node.next
                
    def is_empty(self):
        '''判断是否是空链表'''
        return self._head.elem == 0

    def insert(self, index, value):
        '''根据索引加入元素'''
        if type(index) is not int:
            err = "integer argument expected, got %s"% type(index).__name__ 
            raise TypeError(err)
        front = self._head
        #???
        index = index if index >= 0 else index + self._head.elem



    def clean(self):
        self._head = None

    def remove(self, value):
        pass


    
    def prepend(self, elem):
        '''Add element at head'''
        self._head = Node(elem, self._head)
        
    def append(self, elem):
        '''Add element at tail'''
        if self._head is None:
            self._head = Node(elem)
        else:
            i = self._head
            while i.next:
                i = i.next
            i.next = Node(elem)

    def pop_head(self):
        '''Pop element from head'''
        if self._head is None:
            raise LinkList.exception(IndexError,"pop")
        # delet head node
        rst = self._head.elem
        self._head = self._head.next
        return rst

    def pop_tail(self):
        '''Pop element from tail'''
        if self._head is None:
            raise LinkList.exception(IndexError, "pop")
        elif self._head.next is None:
            rst = self._head.elem
            self._head = None
        else:
            front_node = self._head
            while front_node.next.next:
                front_node = front_node.next
            rst = front_node.next.elem
            front_node.next = None
        return rst

    def __repr__(self):
        '''Return a valid Python expression that could be used to recreate object'''
        node = self._head
        rst = "LinkList()"
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
        # super()-->  "<%s.LinkList object at %s>" % (__name__, hex(id(self)))
        return rst

    @staticmethod
    def exception(err_cls, *args):
        err_info = ""
        if err_cls is IndexError:
            err_info =  "LinkList index out of range"

        if err_cls is TypeError:
            err_type = type(args[0]).__name__
            if args[1] == '__getitem__' or "__setitem__":
                type_err = "LinkList indices must be intergers or slices, not %s" % err_type
            elif args[1] == 'insert':
                type_err = "integer argument expected, got %s" % err_type
        return err_cls(err_info)

    def __getitem__(self, key):
        '''Return value of item'''
        if isinstance(key, slice):
            start = key.start
            stop = key.stop
            step = key.step
            return LinkList(start, stop, step)
        if type(key) is not int:
            raise LinkList.exception(TypeError, key, 'indices')
        if not self._head:
            raise LinkList.exception(IndexError)
        if key >= 0:
            node = self._head
            count = 0
            while count < key:
                node = node.next
                count += 1
                if not node:
                    raise LinkList.exception(IndexError)
            return node.elem
        else:
            size = len(self)
            if -(item) > size:
                raise LinkList.exception(IndexError)
            key = size + key
            return self.__getitem__(key)

    def __len__(self):
        count = 0
        node = self._head
        while node:
            node = node.next
            count += 1
        return count

    def __setitem__(self, index, value):
        '''Assign value of index'''
        if type(index) is not int:
            raise LinkList.exception(TypeError, index, 'indices')
        if not self._head:
            raise LinkList.exception(IndexError)
        if item >= 0:
            node = self._head
            count = 0
            while count < item:
                node = node.next
                count += 1
                if not node:
                    raise LinkList.exception(IndexError)
            node.elem = value
        else:
            item = len(self) + item
            self.__setitem__(item, value)

    def __iter__(self):
        '''Be iterable __getitem__ also, return a iterator, for iter() ,for...'''
        # so that traversal temporary variable doesn't waste memory
        return LinkList.Iterator(self)

