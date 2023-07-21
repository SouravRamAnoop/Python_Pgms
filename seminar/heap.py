"""Creating a simple heap
The heapify(iterable):- This function is used to convert the iterable into a heap data structure.
 i.e. in heap order.
"""

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", (list(li)))