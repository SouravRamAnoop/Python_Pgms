# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")

# print(queue)

    #Adding Elements
# class Queue:
#    def __init__(self):
#       self.queue = list()
#
#    def addtoq(self,dataval):
# # Insert method to add element
#     if dataval not in self.queue:
#       self.queue.insert(0,dataval)
#       print(self.queue)
#     return False
#
#    def size(self):
#       return len(self.queue)
#
# TheQueue = Queue()
# x=TheQueue.addtoq("Mon")
# y=TheQueue.addtoq("Tue")
# z=TheQueue.addtoq("Wed")
# print(TheQueue.size())

#removing elements
# class Queue:
#    def __init__(self):
#       self.queue = list()
#
#    def addtoq(self,dataval):
# # Insert method to add element
#     if dataval not in self.queue:
#       self.queue.insert(0,dataval)
#       print(self.queue)
#       return True
#
#     return False
# # Pop method to remove element
#    def removefromq(self):
#       if len(self.queue)>0:
#          return self.queue.pop()
#       return ("No elements in Queue!")
#
# TheQueue = Queue()
# TheQueue.addtoq("Mon")
# TheQueue.addtoq("Tue")
# TheQueue.addtoq("Wed")
# print(TheQueue.removefromq())
# print(TheQueue.removefromq())
# print(TheQueue.removefromq())