from linkstack import LinkStack
import sys

class MyDC:
    operator_list = ["+", "-", "*", "/", "%", "p", "q"]
    def __init__(self):
        # stack = [4, 8.9, 2,...]
        self.stack = LinkStack()

    def run(self):
        while True:
            # step 1: "3 4.1 p q"
            line = input()
            # step2 : ["(3)", "(4.1)", "p"]
            line = MyDC.__read(line)
            # step3: stack = [3, 4.1] print("4.1")
            if MyDC.__handle(line, self.stack):
                break

    @staticmethod
    def __read(line):
        ''' 分割 "3 4.1 + p q 8" --> ['(3)', '(4.1)', 'p', 'q'] '''
        line = line + " "
        list_ = list()
        # 用于累加成一个数值的临时变量
        temp = str()
        for item in line:
            # 0 ~ 9 or . 如， item = "4.1"
            if item >= '0' and item <= '9' or item == '.':
                temp += item
                continue
            else:
                # 停止上一步累计
                if temp:
                    # "6" --> "(6)"
                    list_.append(MyDC.format(temp))
                    # 清空累计变量
                    temp = str()
                # 合法输入
                if item in MyDC.operator_list:
                    list_.append(item)
                    # 'q'不再录入后续命令
                    if item == 'q':
                        break
                # 输入空格
                elif item == ' ':
                    continue
                # 非法输入
                else:
                    raise Exception()
        return list_

    @staticmethod
    def __handle(command_line, stack):
        #打印处理的命令列表
        #print(command_line)
        for command in command_line:
            if command == 'p':
                print(stack.gettop())
            elif command == 'q':
                print("My Desk calculator of linkstack quit.")
                return 1
            # '+' '-' '*' '/' pop2 push1
            elif command in MyDC.operator_list:

                try:
                    num1 = str(stack.pop())
                    num2 = str(stack.pop())
                except IndexError:
                    raise IndexError("pop from empty stack")
                else:
                    rst = eval(num2 + command + num1)
                    stack.push(rst)
            else:
                # 0 ~ 9 command "(6)" --> rst 6 --> stack.push
                rst = MyDC.format(command, reverse = True)
                stack.push(rst)
            # 打印处理完命令后的栈结果
            #print("stack.list:", stack.list)

    @classmethod
    def format(cls, item, reverse=False):
        if reverse:
            return eval(item.strip("()"))
        else:
            return "(" + str(item) + ")"
            

if __name__ == "__main__":
    dc = MyDC()
    dc.run()

