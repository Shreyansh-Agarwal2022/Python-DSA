from collections import deque

stack = deque()

# Adding elements to the stack
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack:")
print(stack)

# Removing elements from the stack
print("\nElements popped from the stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after elements are popped:")
print(stack)