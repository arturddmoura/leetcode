#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.in_queue = []
        self.out_queue = []

    def push(self, x: int) -> None:
        self.in_queue.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_queue.pop()

    def peek(self) -> int:
        if not self.out_queue:
            while self.in_queue:
                self.out_queue.append(self.in_queue.pop())
        return self.out_queue[-1]

    def empty(self) -> bool:
        return not self.out_queue and not self.in_queue


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
