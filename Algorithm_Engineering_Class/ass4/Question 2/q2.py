import time
import random
import matplotlib.pyplot as plt
import copy

# QUICKSORT taken from geeksforgeeks (https://www.geeksforgeeks.org/python-program-for-quicksort/)
# Partition function
def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower

def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p-1)
    _quicksort(xs, p+1, end)
   
def quicksort(xs):
    _quicksort(xs, 0, len(xs)-1)
   
def qsort(arr):
    return arr if len(arr) <= 1 else qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x >= arr[0]])
               
# INSERTION SORT taken from geeksforgeeks (https://www.geeksforgeeks.org/python-program-for-insertion-sort/)
# Function to do insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def _hyrbid(arr, start, end):
    if len(arr) < 40:
        insertionSort(arr)
    elif start < end:
        p = partition(arr, start, end)
        _hyrbid(arr, start, p-1)
        _hyrbid(arr, p+1, end)

def hybrid(arr):
    if len(arr) < 40:
        insertionSort(arr)
    else:
        _hyrbid(arr, 0, len(arr) - 1)
   
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res

def plot_sorts(nums, quick, insert=None, hybrid=None):
    plt.title('Quicksort vs Insertionsort vs Hybridsort')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')

    x = nums

    yQ = quick

    if insert:
        yI = insert
        plt.plot(x, yI, color='red', linewidth=1, label='Insertion sort')

    if hybrid:
        yH = hybrid
        plt.plot(x, yH, color='green', linewidth=1, label='Hybridsort')


    plt.plot(x, yQ, color='blue', linewidth=1, label='Quicksort')

    plt.legend()
    plt.savefig('all3sorts')
    print('Saved')
    

def main():
    NUM_ITEMS_LIST = []
    quick = []
    insert = []
    hyb = []
    random_lists = []
    num_iterations = 5000
   
    for NUM_ITEMS in range(1,101):
        NUM_ITEMS_LIST.append(NUM_ITEMS)
        random_lists = []
        for i in range(num_iterations):
            random_lists.append(Rand(1, 9000, NUM_ITEMS))
        sec = copy.deepcopy(random_lists)
        thir = copy.deepcopy(random_lists)
       
        beforeQ = time.time()
        for i in range(num_iterations):
            qsort(thir[i])
        afterQ = time.time()
       
        beforeI = time.time()
        for i in range(num_iterations):
            insertionSort(sec[i])
        afterI = time.time()

        beforeH = time.time()
        for i in range(num_iterations):
            hybrid(random_lists[i])
        afterH = time.time()

        quick.append(afterQ-beforeQ)
        insert.append(afterI-beforeI)
        hyb.append(afterH-beforeH)
        
    
    quick = [ ele / len(quick) for ele in quick ]
    insert = [ ele / len(insert) for ele in insert ]
    hyb = [ ele / len(hyb) for ele in hyb ]
    plot_sorts(NUM_ITEMS_LIST, quick, insert, hyb)
   
if __name__ == "__main__":
    main()