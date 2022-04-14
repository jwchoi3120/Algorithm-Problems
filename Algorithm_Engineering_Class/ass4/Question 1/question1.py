# QUESTION 1
import time
import random
import matplotlib.pyplot as plt


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
    _quicksort(xs, start, p - 1)
    _quicksort(xs, p + 1, end)


def quicksort(xs):
    _quicksort(xs, 0, len(xs) - 1)


def qsort(arr):
    return arr if len(arr) <= 1 else qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort(
        [x for x in arr[1:] if x >= arr[0]])


# INSERTION SORT taken from geeksforgeeks (https://www.geeksforgeeks.org/python-program-for-insertion-sort/)
# Function to do insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res


def main():
    NUM_ITEMS_LIST = []
    quicksort_time = []
    insertion_time = []
    random_lists = []
    num_iterations = 300

    for NUM_ITEMS in range(1, 1000):
        NUM_ITEMS_LIST.append(NUM_ITEMS)
        random_lists = []
        for i in range(num_iterations):
            random_lists.append(Rand(1, 9000, NUM_ITEMS))
        sec = random_lists[:]

        before = time.time()
        for i in range(num_iterations):
            qsort(sec[i])
        after = time.time()
        quicksort_time.append(after - before)

        before = time.time()
        for i in range(num_iterations):
            insertionSort(random_lists[i])
        after = time.time()
        insertion_time.append(after - before)

        # ENDFOR
        # print(insertion_time)
        # print(quicksort_time)
        # plotting the line 1 points
        plt.plot(NUM_ITEMS_LIST, insertion_time, label="Insertion sort")

        # plotting the line 2 points
        plt.plot(NUM_ITEMS_LIST, quicksort_time, label="Quick sort")

        # naming the x axis
        plt.xlabel('Number of elements')
        # naming the y axis
        plt.ylabel('Time taken')
        # giving a title to my graph
        plt.title('Insertion sort vs Quick sort')

        # show a legend on the plot
        plt.legend()

        # function to show the plot
        plt.show()


if __name__ == "__main__":
    main()