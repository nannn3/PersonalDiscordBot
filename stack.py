# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 07:10:24 2022

@author: Tristen
"""


class Stack:

    def __init__(self):
        self.stack = []
        self.index = -1

    def isEmpty(self):
        return True if self.size() == 0 else False

    def push(self, item):
        self.stack.append(item)
        self.index += 1

    def pop(self):
        foo = self.stack.pop(self.index)
        self.index -= 1
        return foo

    def peek(self):
        return None if self.isEmpty() else self.stack[self.index]

    def size(self):
        return len(self.stack)
