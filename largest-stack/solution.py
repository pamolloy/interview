#!/usr/bin/env python
#
#   largest-stack/solution.py
#

class Stack:
    """A class that represents a stack and is given in the problem"""

    def __init__(self):
        """Initialize an empty list"""
        self.items = []

    def push(self, item):
        """Push a new item to the last index"""
        self.items.append(item)

    def pop(self):
        """Remove the last item"""

        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""

        # If the stack is empty, return None
        if not self.items:
            return None

        return self.items[-1]

class MaxStackBrute(Stack):
    """Without modifying the original methods create a new method with O(n)
       running time that loops through each element to find the largest"""

    def get_max(self):
        """Get the maximum value in the stack of integers"""

        largest_element = self.items[0]
        for element in self.items[1:]:
            if element > largest_element:
                larest_element = element

        return largest_element

# I could add a variable called `self.largest_element`, which could be updated
# with every push(), but what if the largest element is removed with a pop()?

class MaxStack(Stack):
    """Since the values are stored in a stack it is not possible to remove a
       arbitrary element. Therefore removing the max means the new maximum must
       have been added earlier. Because of that a second stack can be used
       to store the largest element"""

    def __init__(self):
        super().__init__()
        self.largest_items = Stack()

    def push(self, item):
        if not self.peek():
            self.largest_items.push(item)
        elif item > self.largest_items.peek():
            self.largest_items.push(item)

        self.items.append(item)

    def pop(self):
        if self.items.peek() == self.largest_items.peek():
            self.largest_items.pop()

        return self.items.pop()

    def get_max(self):
        return self.largest_items.peek()

examples = [
    ([("push", 4), ("push", 5), ("push", 8)], 8)
]

if __name__ == "__main__":
    stack = MaxStack()
    for actions, maximum in examples:
        for function, argument in actions:
            getattr(stack, function)(argument)
        assert maximum == stack.get_max()
