155. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

1. 澄清:


2. 易错点:


3. 思路
   use array to store a list of  data and min value so far

4.1.algorithm: use array method, ---o(1) time

class MinStack:

    def __init__(self):
        self.stack =[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            self.stack.append([val, min(self.stack[-1][1], val)])

    def pop(self) -> None:
        return self.stack.pop()[0] if self.stack else None

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
