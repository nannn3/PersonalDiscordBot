# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 07:10:24 2022

@author: Tristen
"""


class Stack:

    def __init__(self):
        self.stack = []
        self.__index = -1

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.stack.append(item)
        self.__index += 1

    def pop(self):
        if not self.isEmpty():
            foo = self.stack.pop(self.__index)
            self.__index -= 1
            return foo
        else:
            return None

    def peek(self):
        return None if self.isEmpty() else self.stack[self.__index]

    def size(self):
        return len(self.stack)


def test():
    s = Stack()
    assert s.isEmpty()
    for i in range(10):
        s.push(i)
    assert s.peek() == 9
    foo = s.pop()
    assert foo == 9
    assert s.isEmpty() is False
    while not s.isEmpty():
        s.pop()
    foo = s.pop()
    assert foo is None


if __name__ == '__main__':
    # not a script, but is self testing
    test()
