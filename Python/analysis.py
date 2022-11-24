#Name:Tanishq Patil
##File: analysis.py
# Student ID:1961827   
# #Date:11/18/2022 
#Sources: Professor Munishkina, Lab info and assignment
from timeit import Timer, timeit
from random import choice
from matplotlib import pyplot as plt
# counting sort for digits 0 - 9
def count_sort(arr, pos, m):
    # count the same digits and put their counts at index = digit
    counts = [0 for i in range(11)] 
    for i in arr:
        i = str(i)
        while len(i) < m: # add 0s in front to small numbers
            i = '0' + i 
        i = int(i[ pos])
        counts[ i] += 1
    # convert counts into ranking: each index value = (number of items <= i) 
    for i in range(10):
        counts[ i] += counts[ i-1]

    output = [0 for i in range(len(arr))]
    # use ranking as index and index as values
    for i in range(len(arr)-1, -1, -1):
        j = str(arr[ i])
        while len(j) < m:
            j = '0' + j
        j = int(j[ pos])
        output[counts[ j]-1] = arr[ i]
        counts[ j] -= 1

    return output

def radix_sort(arr, pos):
    for i in range(pos-1, -1, -1):
        arr = count_sort(arr,i,pos)
    return arr
        
def mergeSort(items):
    if len(items)>1:
        mid = len(items)//2
        l = items[:mid]
        r = items[mid:]
        mergeSort(l)
        mergeSort(r)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[ i] <= r[ j]:
                items[ k] = l[ i]
                i += 1
            else:
                items[ k] = r[ j]
                j += 1
            k += 1
        while i < len(l):
            items[ k] = l[ i]
            i, k = i+1, k+1
        while j < len(r):
            items[ k] = r[ j]
            j, k = j+1, k+1
def bubbleSort(items):
    for i in range(len(items)-1,0,-1): # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[ j] > items[j+1]:
                items[ j], items[j+1] = items[j+1], items[ j] # swap items           
def plot(inputSize,times,fig,ax,type):
    global colors
    
list_ = list(range(0,500))      # list of numbers
data=[]
data.append([choice(list_) for i in range(10)])
data.append([choice(list_) for i in range(20)])

for i in [50,100,200,500]:
    data.append([choice(list_) for i in range(i)])


# you need to add more lists of different sizes: d3, d4, d5, and d6  # your input
times = []       # times required to sort input

for i in data:
    t1 = Timer(f"bubbleSort({i})", "from __main__ import bubbleSort")
    #print("bubblesort ",t1.timeit(number=3), "milliseconds") # for debugging
    times.append(t1.timeit(number=3)) # record the time required to sort the input
type="BubbleSort- O(n^2)"
fig=plt.figure()
ax=plt.axes()
ax.set_title("Algorithm Analysis")
ax.set_ylabel('Times')
ax.set_xlabel('Size of Input')
colors=["red","green","blue"]
ax.plot([10,20,50,100,200,500],times,color=colors[0],label=type)
if len(colors)>1:
    colors=colors[1::]
times=[]
for i in data:
    t1 = Timer(f"mergeSort({i})", "from __main__ import mergeSort")
    #print("mergeSort ",t1.timeit(number=3), "milliseconds") # for debugging
    times.append(t1.timeit(number=3)) # record the time required to sort the input
type="MergeSort-O(nlog(n))"
ax.plot([10,20,50,100,200,500],times,color=colors[0],label=type)
if len(colors)>1:
    colors=colors[1::]
times=[]
for i in data:
    t1 = Timer(f"radix_sort({i},{3})", "from __main__ import radix_sort")
    #print("mergeSort ",t1.timeit(number=3), "milliseconds") # for debugging
    times.append(t1.timeit(number=3)) # record the time required to sort the input
type="RadixSort-O(nk)"
ax.plot([10,20,50,100,200,500],times,color=colors[0],label=type)
if len(colors)>1:
    colors=colors[1::]
plt.legend()
plt.show()




# do not forget to plot your data!!!