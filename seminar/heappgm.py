"""A heap is created by using python’s inbuilt library named heapq.
 This library has the relevant functions to carry out various operations on heap data structure"""

#creating heap
import heapq

H = [21,1,45,78,3,5]
#transform list in to heap
heapq.heapify(H)
print(H)

#Inserting into heap
# import heapq
#
# H = [21,1,45,78,3,5]
# # Covert to a heap
# heapq.heapify(H)
# print(H)

# Add element
# heapq.heappush(H,8)
# print(H)