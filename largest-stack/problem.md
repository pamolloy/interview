You've implemented a Stack class, but you want to be able to access the largest element in a stack.

Here's the Stack class you have:

```
  class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        return self.items.pop()

    # see what the last item is
    def peek(self):
        # if the stack is empty, return None
        if not self.items: return None

        return self.items[len(self.items)-1]
```

Use your Stack class to implement a new class MaxStack with a function `get_max()` that returns the largest element in the stack. `get_max()` should not remove the item.

Your stacks will contain only integers.

Problem from [Interview Cake](https://www.interviewcake.com/).
