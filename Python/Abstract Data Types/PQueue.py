# # Python3 code to implement priority-queue
# # using array implementation of
# # binary heap
 
# H = [0]*50
# size = -1
   
# # Function to return the index of the
# # parent node of a given node
# def parent(i) :
 
#     return (i - 1) // 2
   
# # Function to return the index of the
# # left child of the given node
# def leftChild(i) :
 
#     return ((2 * i) + 1)
   
# # Function to return the index of the
# # right child of the given node
# def rightChild(i) :
 
#     return ((2 * i) + 2)
     
# # Function to shift up the 
# # node in order to maintain 
# # the heap property
# def shiftUp(i) :
 
#     while (i > 0 and H[parent(i)] < H[i]) :
           
#         # Swap parent and current node
#         swap(parent(i), i)
       
#         # Update i to parent of i
#         i = parent(i)
         
# # Function to shift down the node in
# # order to maintain the heap property
# def shiftDown(i) :
 
#     maxIndex = i
       
#     # Left Child
#     l = leftChild(i)
       
#     if (l <= size and H[l] > H[maxIndex]) :
     
#         maxIndex = l
       
#     # Right Child
#     r = rightChild(i)
       
#     if (r <= size and H[r] > H[maxIndex]) :
     
#         maxIndex = r
       
#     # If i not same as maxIndex
#     if (i != maxIndex) :
     
#         swap(i, maxIndex)
#         shiftDown(maxIndex)
         
# # Function to insert a 
# # new element in 
# # the Binary Heap
# def insert(p) :
     
#     global size
#     size = size + 1
#     H[size] = p
       
#     # Shift Up to maintain 
#     # heap property
#     shiftUp(size)
   
# # Function to extract 
# # the element with
# # maximum priority
# def extractMax() :
     
#     global size
#     result = H[0]
       
#     # Replace the value 
#     # at the root with 
#     # the last leaf
#     H[0] = H[size]
#     size = size - 1
       
#     # Shift down the replaced 
#     # element to maintain the 
#     # heap property
#     shiftDown(0)
#     return result
   
# # Function to change the priority
# # of an element
# def changePriority(i,p) :
 
#     oldp = H[i]
#     H[i] = p
       
#     if (p > oldp) :
     
#         shiftUp(i)
  
#     else :
     
#         shiftDown(i)
   
# # Function to get value of 
# # the current maximum element
# def getMax() :
  
#     return H[0]
   
# # Function to remove the element
# # located at given index
# def Remove(i) :
 
#     H[i] = getMax() + 1
       
#     # Shift the node to the root
#     # of the heap
#     shiftUp(i)
       
#     # Extract the node
#     extractMax()
   
# def swap(i, j) :
     
#     temp = H[i]
#     H[i] = H[j]
#     H[j] = temp
     
# # Insert the element to the
# # priority queue
# insert(45)
# insert(20)
# insert(14)
# insert(12)
# insert(31)
# insert(7)
# insert(11)
# insert(13)
# insert(7)
   
# i = 0
   
# # Priority queue before extracting max
# print("Priority Queue : ", end = "")
# while (i <= size) :
 
#     print(H[i], end = " ")
#     i += 1
   
# print()
   
# # Node with maximum priority
# print("Node with maximum priority :" ,  extractMax())
   
# # Priority queue after extracting max
# print("Priority queue after extracting maximum : ", end = "")
# j = 0
# while (j <= size) :
 
#     print(H[j], end = " ")
#     j += 1
   
# print()
   
# # Change the priority of element
# # present at index 2 to 49
# changePriority(2, 49)
# print("Priority queue after priority change : ", end = "")
# k = 0
# while (k <= size) :
 
#     print(H[k], end = " ")
#     k += 1
   
# print()
   
# # Remove element at index 3
# Remove(3)
# print("Priority queue after removing the element : ", end = "")
# l = 0
# while (l <= size) :
 
#     print(H[l], end = " ")
#     l += 1
from heap import BinHeap as Heap
class PriorityQueue():
    def __init__(self):
        self.queue=Heap() 

    def insert(item):
            
        pass
    def extract_min():
        pass
    def minimum():
        pass
    def decrease_key():
        pass
    def isEmpty():
        pass
    def size():
        pass
