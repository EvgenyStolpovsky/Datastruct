class Node:
    def __init__(self, data, next_node=None):
        """Класс активации узла"""
        self.data = data
        self.next_node = next_node

class Stack:

    def __init__(self):
        '''Инициализация пустого стэка'''
        self.top = None

    def push(self, data):
        '''Добавляет элемент в стэк'''
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data) #5
print(n2.data) #a
print(n1)
print(n2.next_node)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)

