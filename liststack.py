class ListStack():
    def __init__(self):
        self.list = list()
   
    def isempty(self):
        return not bool(self.list)

    def gettop(self):
        try:
            rst = self.list[-1]
        except IndexError:
            raise IndexError("get top from empty ListStack")
        else:
            return rst
    # 压栈 / 入栈
    def pop(self):
        try:
            rst = self.list.pop()
        except IndexError:
            raise IndexError("pop from empty ListStack")
            #print("pop from empty ListStack")
        else:
            return rst
    # 弹栈 / 出栈
    def push(self, item):
        self.list.append(item)
    
    def __repr__(self):
        return repr(self.list)
