from linkstack import LinkStack

class PrintTree:

    symbols = ['───','─┬─', ' ├─', ' └─', ' │ ', '   ']
    
    class Item:
        def __init__(self, data=None, level=None, head=None, tail=None ):
            self.data = data
            self.level = level
            self.head = head
            self.tail = tail

        def choose_symbol(self):
            if self.level == 0:
                symbol = ""
            else:
                if self.neighbour == [0,0]:
                    symbol = PrintTree.symbols[0]
                elif self.neighbour == [0,1]:
                    symbol = PrintTree.symbols[1]
                elif self.neighbour == [1,1]:
                    symbol = PrintTree.symbols[2]
                elif self.neighbour == [1,0]:
                    symbol = PrintTree.symbols[3]
            return symbol

    def __init__(self, file_=None, str_=None, list_=None):
        self.list = []
        self.rst = ""
        self.run(file_, str_, list_)

    def run(self, file_, str_, list_):
        self.in_file(file_)
        self.in_str(str_)
        self.in_list(list_)
        self.handle_list()
        self.list_str()


    def get_level(self, line):
        ''' "    hello" --> level '''
        count = 0
        for char in line:
            if ord(char) == 32:
                count += 1
            else:
                break
        # 4个空格为一个级别缩进
        return count // 4

    def line(self, line):
        level = self.get_level(line)
        data = line.strip(' \n')
        if data:
            self.list.append(PrintTree.Item(data, level))

    def in_file(self, filename):
        if not filename:
            return
        fd = open(filename, 'rt')
        for line in fd:
            self.line(line)
        fd.close()

    def in_str(self, str_):
        if not str_:
            return 
        list_ = str_.split("\n")
        for line in list_:
            self.line(line)

    def in_list(self, list_):
        if not list_:
            return
        for x in list_:
            data = x[0]
            level = x[1]
            self.list.append(PrintTree.Item(data=data, level=level))

    def handle_list(self):
        stack = LinkStack()
        stack.max_level = -1
        
        # 需要遍历两遍
        # step 1 stack 创建临时变量lenth neighbour family 完成tail 和不缩进的head""
        # step 2 list  删除临时变量lenth neighbour family 完成head
        
        def push_stack(stack, item):
            # neighbour lenth 初始化临时变量
            item.neighbour = [0,0] 
            item.lenth = len(str(item.data))
            item.family = []
            if not stack.is_empty():
                if stack.getnext().tail is None:
                    # 设置紧临前节点尾部不回车
                    stack.getnext().tail = ""
                    # 插入节点无哥哥节点
                    # 插入节点紧挨着父亲节点
                    item.head = ""
                else:
                    # 插入节点有哥哥节点front = 1
                    item.neighbour[0] |= 1
            # 更新stack.max_level
            stack.max_level = item.level
            #family
            for parent in stack:
                item.family.append(parent)
            item.family = item.family
            # 压栈
            stack.push(item)
            return item
        
        def pop_stack(stack):
            # 弹栈
            pop_item = stack.pop()
            if pop_item.tail is None:
                pop_item.tail = "\n"
            # 更新stack.max_level
            try:
                stack.max_level = stack.getnext().level
            except IndexError:
                stack.max_level = -1
            return pop_item

        # step1
        for item in self.list:
            # 弹栈
            while stack.max_level >= item.level:
                pop_item = pop_stack(stack)
                if pop_item.level == item.level:
                    # 弹出节点有弟弟节点
                    pop_item.neighbour[1] |= 1
            
            # 压栈
            push_stack(stack, item)
        while not stack.is_empty():
            pop_item = pop_stack(stack)
        #step2
        for item in self.list:
            if item.head is None:
                item.head = ""
                for parent in item.family:
                    item.head = " " * parent.lenth + item.head
                    if parent == item.family[-1]:
                        continue
                    if parent.neighbour[1]:
                        item.head = PrintTree.symbols[4] + item.head
                    else:
                        item.head = PrintTree.symbols[5] + item.head
            item.head = item.head + item.choose_symbol()
            # 删除临时变量
            #del item.family
            #del item.neighbour
            #del item.lenth

    def list_str(self):
        for item in self.list:
            # 创建 item.rst
            item.rst =  item.head + str(item.data) + item.tail
            self.rst += item.rst

    def __repr__(self):
        return self.rst

if __name__ == '__main__':
    print(PrintTree(file_='test2.txt').__repr__())
    
