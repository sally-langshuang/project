from linkstack import LinkStack

class Match:
    brackets = {'{', '}', '[', ']', '(', ')'}
    opposite = {'{':'}', '[':']', '(':')'}
    
    def __init__(self, string=None):
        self.str = string
        self.stack = LinkStack()
        self.run()
    
    def generator(self):
        line = 0
        num = 0
        for char in self.str:
            num += 1
            if char in Match.brackets:
                yield (char, line, num)

    def run(self):
        # 括号信息生成器
        g = self.generator()
        for symbol, line, num in g:
            # 读到左括号， 将左括号入栈
            if symbol in Match.opposite:
                self.stack.push((symbol, line, num))
            # 读到右括号，从栈里弹出一个元素
            elif self.stack.is_empty() or Match.opposite[self.stack.pop()[0]] != symbol:
                raise Exception('%d行%d列%c没有匹配的左括号'% (line, num, symbol))
        if not self.stack.is_empty():
            symbol, line, num = self.stack.pop()
            raise Exception('%d行%d列%c没有匹配的右括号'% (line, num, symbol))

