class MyQueue:
    # time complexity: O(1)
    # space complexity: O (n)
    #used to stacks to keep the correct order of the stack and to pop the first element of the stack.
    #For push the integers are appended only to stack. If values are present in reverse stack it's shifted back to stack before push. 
    #For pop if reverse stack is empty the values are pushed into reverse stack and then poped to pop the first element. 
    # Peek shows the first/last element depending on the stack.

    def __init__(self):
        self.stack = []
        self.reverse_stack = []

    def push(self, x: int) -> None:
        if len(self.stack) > 0:
            self.stack.append(x)
        else:
            #append only to stack to preserve the order of the elements
            while self.reverse_stack:
                self.stack.append(self.reverse_stack.pop())
            self.stack.append(x)

    def pop(self) -> int:
        if not self.reverse_stack:  # Only transfer if reverse_stack is empty
            while self.stack:  
                self.reverse_stack.append(self.stack.pop())
        return self.reverse_stack.pop()

    def peek(self) -> int:
        if len(self.stack) > 0:
            return self.stack[0]
        return self.reverse_stack[-1]

    def empty(self) -> bool:
        if len(self.stack) > 0 or len(self.reverse_stack) > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()