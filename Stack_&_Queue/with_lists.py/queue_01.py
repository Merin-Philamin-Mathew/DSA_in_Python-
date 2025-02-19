queue = []

arr = [3,4,5,7,8]
# enqueue
for i in arr:
    queue.append(i)

# display
print(queue)

# dequeue
queue.pop(0)
print(queue)