"""
Queue to stack converter.
"""

import copy
from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    """
    This function converts queue to stack.
    """
    queue_copy = copy.deepcopy(queue)
    convert_stack = ArrayStack()
    stack = ArrayStack()

    for i in range(len(queue_copy)):
        stack.add(queue_copy.pop())

    for i in range(len(stack)):
        convert_stack.add(stack.pop())

    return convert_stack


queue = ArrayQueue()
for i in range(10):
    queue.add(i)
stack = queue_to_stack(queue)
print(queue)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(stack)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(stack.pop())
# 0
print(queue.pop())
# 0
stack.add(11)
queue.add(11)
print(queue)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print(stack)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
