import random
import math
import timeit
import time
import numpy as np
from sorts import mergesort_bottom, merge_bottom, mergesort, merge, mergesort_implementation2
from sorts import merge_implementation2, mergesort_three, merge_three, mergesort_three_implementation2
from sorts import merge_three_implementation2, create_near_sorted_list, create_random_list

#creating tests
# time test for bottom-up mergesort
def test_mergesort_bottom(i):
    totalTime = 0
    for j in range(50):
        L = create_random_list(i)
        t0 = timeit.default_timer()
        mergesort_bottom(L)
        t1 = timeit.default_timer()
        totalTime += t1 - t0
    return (totalTime/50)

# time test for two-way mergesort
def test_mergesort(i):
    totalTime = 0
    for j in range(50):
        L = create_random_list(i)
        t0 = timeit.default_timer()
        mergesort(L)
        t1 = timeit.default_timer()
        totalTime += t1 - t0
    return (totalTime/50)

# time test for three-way mergesort
def test_mergesort_three(i):
    totalTime = 0
    for j in range(50):
        L = create_random_list(i)
        t0 = timeit.default_timer()
        mergesort_three(L)
        t1 = timeit.default_timer()
        totalTime += t1 - t0
    return (totalTime/50)

# time test for second implementation of three-way mergesort
def test_mergesort_three_implementation2(i):
    totalTime = 0
    for j in range(50):
        L = create_random_list(i)
        t0 = timeit.default_timer()
        mergesort_three_implementation2(L)
        t1 = timeit.default_timer()
        totalTime += t1 - t0
    return (totalTime/50)

# time test for second implementation of two-way mergesort
def test_mergesort_implementation2(i):
    totalTime = 0
    for j in range(50):
        L = create_random_list(i)
        t0 = timeit.default_timer()
        mergesort_implementation2(L)
        t1 = timeit.default_timer()
        totalTime += t1 - t0
    return (totalTime/50)

# outputing results of tests
# compare mergesort two-way and three-way
def analysis_mergesort():
    outF = open("out1.txt", "w")
    for i in range(1000):
        outF.write(str(i) + " " +  str(test_mergesort(i)) + " " + str(test_mergesort_three(i))  + "\n" )
    outF.close()

# compare all functions
def analysis_all_mergesorts():
    outF = open("out2.txt", "w")
    for i in range(1000):
        outF.write(str(i) + " " +  str(test_mergesort(i)) + " " + str(test_mergesort_implementation2(i)) + " " + str(test_mergesort_three(i)) + " " + str(test_mergesort_three_implementation2(i))  + "\n" )
    outF.close()

# compare the two implementations of two-way mergesort
def analysis_two():
    outF = open("out3.txt", "w")
    for i in range(1000):
        outF.write(str(i) + " " +  str(test_mergesort(i)) + " " + str(test_mergesort_implementation2(i))  + "\n" )
    outF.close()

# compare the two implementations of three-way mergesort
def analysis_three():
    outF = open("out4.txt", "w")
    for i in range(1000):
        outF.write(str(i) + " " +  str(test_mergesort_three(i)) + " " + str(test_mergesort_three_implementation2(i))  + "\n" )
    outF.close()

# compare the extra implementations
def analysis_implementation2():
    outF = open("out5.txt", "w")
    for i in range(1000):
        outF.write(str(i) + " " +  str(test_mergesort_implementation2(i)) + " " + str(test_mergesort_three_implementation2(i))  + "\n" )
    outF.close()

# used for testing the best implementation (two-way mergesort or bottom-up mergesort)
def best_implementation():
    outF = open("out6.txt", "w")
    for i in range(1000):
        outF.write(str(i) + " " +  str(test_mergesort(i)) + " " + str(test_mergesort_bottom(i))  + "\n" )
    outF.close()

# code for worst case portion of assignment
def test_worst_case(i):
    totalTime = 0
    for j in range(50):
        L = create_near_sorted_list(100,i)
        t0 = timeit.default_timer()
        mergesort_bottom(L)
        t1 = timeit.default_timer()
        totalTime += t1 - t0
    return (totalTime/50)

def worst_case():
    outF = open("out7.txt", "w")
    for i in np.arange(0, 0.5, 0.0001):
        outF.write(str(i) + " " +  str(test_worst_case(i)) + "\n" )
    outF.close()
