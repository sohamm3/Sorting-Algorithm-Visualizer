import time
from random import randint

# Dict to store  time taken for differnet algos for variety of input
time_dict={"Bubble Sort":[],"Insertion Sort":[],"Merge Sort":[],"Selection Sort":[],"Shell Sort":[]}

# Sample size for average time
sample_size=5
size_lst=[50,100,500,1000,2000,10000,100000,1000000,10000000]

# Generate a random array of a given size
def generate_array(size,maxx=500):
    rndm_arr=[randint(0,maxx) for _ in range(size)]
    return rndm_arr

# Code for sorting algos with_out visualsation

# Bubble Sort
def BubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

# Selection Sort 
def SelectionSort(arr):
    n=len(arr)
    for i in range(n):
        min =i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr

# Insertion Sort
def InsertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1],arr[j]=arr[j],arr[j+1]
            j=j-1
        arr[j+1]=key
    return arr


def command():
    # Time taken for bubble sort
    for size in size_lst[:5]:
        total_time=0.0
        for _ in range(sample_size):
            arr=generate_array(size)
            t1=time.time()
            BubbleSort(arr)
            t2=time.time()
            total_time+=t2-t1
        time_dict["Bubble Sort"].append(total_time/float(sample_size))

# Time taken for insertion sort
    for size in size_lst[:5]:
        total_time=0.0
        for _ in range(sample_size):
            arr=generate_array(size)
            t1=time.time()
            InsertionSort(arr)
            t2=time.time()
            total_time+=t2-t1
        time_dict["Insertion Sort"].append(total_time/float(sample_size))

# Time taken for selection sort
    for size in size_lst[:5]:
        total_time=0.0
        for _ in range(sample_size):
            arr=generate_array(size)
            t1=time.time()
            SelectionSort(arr)
            t2=time.time()
            total_time+=t2-t1
        time_dict["Selection Sort"].append(total_time/float(sample_size))

    return (time_dict,size_lst) 