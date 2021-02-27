import timeit
import random
import math

from heap import Heap

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

# tests all of the build heaps, change the __init__ specifications each time
def test_build_heap(i):
    totalTime = 0
    for j in range(50):
        L = create_random_list(i)
        t0 = timeit.default_timer()
        Heap(L)
        t1 = timeit.default_timer()
        totalTime += t1 - t0
    return (totalTime/50)

def analysis_build_heap():
    outF = open("heap3.txt", "w")
    for i in range(1000):
        outF.write( str(test_build_heap(i))  + "\n" )
    outF.close()

analysis_build_heap()


#heap = Heap([])
#print(heap)