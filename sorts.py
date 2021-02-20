import random
import math
import timeit
import time
import numpy as np

# bottom-up mergesort
def mergesort_bottom(L):
    current_size = 1
    while current_size < len(L):
        left = 0
        while left < len(L):
            mid = left + current_size
            right = left + current_size*2
            merge_bottom(L, left, mid, right)
            left = left + current_size * 2

        current_size = 2 * current_size
    return L


def merge_bottom(L, start, mid, end):
    right = L[start:mid]
    left = L[mid:end]
    i = 0
    j = 0
    result = []

    while i < len(right) and j < len(left):
        if right[i] < left[j]:
            result.append(right[i])
            i += 1
        else:
            result.append(left[j])
            j += 1

    result = result + right[i:] + left[j:]
    
    for i in range(len(L[start:end])):
        L[start + i] = result[i]

#mergesort given to us
def mergesort(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, right = L[:mid], L[mid:]

    #Mergesort core
    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]

def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j+=1
    return L

# written code for improved two-way mergesort
def mergesort_implementation2(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, right = L[:mid], L[mid:]
    mergesort_implementation2(left)
    mergesort_implementation2(right)
    temp = merge_implementation2(left, right)
    for i in range(len(temp)):
        L[i] = temp[i]


def merge_implementation2(left, right):
    L = []
    i = j = 0
    leftLength = len(left)
    rightLength = len(right)
    while i < leftLength and j < rightLength:
        if left[i] <= right[j]:
            L.append(left[i])
            i += 1
        else:
            L.append(right[j])
            j+=1
    while (i < leftLength):
        L.append(left[i])
        i += 1
    while (j < rightLength):
        L.append(right[j])
        j += 1
    return L

# three-way mergesort
def mergesort_three(L):

    low = 0
    high = len(L)

    if (high - low < 2):
        return

    partition1 = low + ((high - low) // 3)
    partition2 = low + 2*((high - low) // 3) + 1

    left, middle, right = L[:partition1], L[partition1:partition2], L[partition2:]
    mergesort_three(left)
    mergesort_three(middle)
    mergesort_three(right)
    temp = merge_three(left, middle, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge_three(left, middle, right):
    L = []
    i = j = k = 0

    while (i < len(left) or j < len(middle) or k < len(right)):
        if i >= len(left) and j >= len(middle):
            L.append(right[k])
            k += 1
        elif i >= len(left) and k >= len(right):
            L.append(middle[j])
            j += 1
        elif j >= len(middle) and k >= len(right):
            L.append(left[i])
            i += 1

        elif i >= len(left):
            while j < len(middle) and k < len(right):
                if middle[j] <= right[k]:
                    L.append(middle[j])
                    j += 1
                elif middle[j] >= right[k]:
                    L.append(right[k])
                    k += 1
        elif j >= len(middle):
            while i < len(left) and k < len(right):
                if left[i] <= right[k]:
                    L.append(left[i])
                    i += 1
                elif left[i] >= right[k]:
                    L.append(right[k])
                    k += 1
        elif k >= len(right):
            while i < len(left) and j < len(middle):
                if left[i] <= middle[j]:
                    L.append(left[i])
                    i += 1
                elif left[i] >= middle[j]:
                    L.append(middle[j])
                    j += 1

        else:
            if left[i] <= middle[j] and left[i] <= right[k]:
                L.append(left[i])
                i += 1
            elif middle[j] <= left[i] and middle[j] <= right[k]:
                L.append(middle[j])
                j += 1
            elif right[k] <= left[i] and right[k] <= middle[j]:
                L.append(right[k])
                k += 1
    return L

# three-way mergesort better implementation
def mergesort_three_implementation2(L):

    if len(L) <= 1:
        return

    if len(L) == 2:
        partition1 = 0
        partition2 = 1

    elif len(L)%2 == 0:
        third = (len(L))//3
        partition1 = third
        partition2 = 2*third 

    elif len(L)%2 == 1:
        third = (len(L))//3
        partition1 = third
        partition2 = 2*third + 1

    left, middle, right = L[:partition1], L[partition1:partition2], L[partition2:]
    mergesort_three_implementation2(left)
    mergesort_three_implementation2(middle)
    mergesort_three_implementation2(right)
    temp = merge_three_implementation2(left, middle, right)

    for i in range(len(temp)):
        L[i] = temp[i]

def merge_three_implementation2(left, middle, right):
    L = []
    i = j = k = 0
    while (i < len(left) and j < len(middle) and k < len(right)):
        if left[i] < middle[j]:
            if left[i] < right[k]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[k])
                k += 1
        else:
            if middle[j] < right[k]:
                L.append(middle[j])
                j += 1
            else:
                L.append(right[k])
                k += 1
    while (i < len(left) and j < len(middle)):
        if left[i] < middle[j]:
            L.append(left[i])
            i += 1
        else:
            L.append(middle[j])
            j += 1
    while (j < len(middle) and k < len(right)):
        if middle[j] < right[k]:
            L.append(middle[j])
            j += 1
        else:
            L.append(right[k])
            k += 1
    while (i < len(left) and k < len(right)):
        if left[i] < right[k]:
            L.append(left[i])
            i += 1
        else:
            L.append(right[k])
            k += 1
    while (i < len(left)):
        L.append(left[i])
        i += 1
    while (j < len(middle)):
        L.append(middle[j])
        j += 1
    while (k < len(right)):
        L.append(right[k])
        k += 1

    return L

# creating lists
def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

    