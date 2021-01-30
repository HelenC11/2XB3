import timeit

# time test copy
def timeTestCopy(iterations,n):
    totalTime = 0
    for i in range(iterations):
        listNum = list(range(n))
        t0 = timeit.default_timer()
        listNumCopy = listNum.copy()
        t1 = timeit.default_timer()
        totalTime += t1 - t0
    return totalTime/iterations

# output for the timeTestCopy
def testCopy():
    for i in range(1, 1000):
        print(i*10, timeTestCopy(50, i*10))

# time test Lookups
def timeTestLookups(iterations, n):
    listNum = list(range(n))
    for j in range(n):
        totalTime = 0
        for i in range(iterations):
            t0 = timeit.default_timer()
            elem = listNum[j]
            t1 = timeit.default_timer()
            totalTime += t1 - t0
        print(j, totalTime/iterations)

# output for Lookups
def testLookups():
    outF = open("out3.txt", "w")
    def timeTestLookups(iterations, n):
        listNum = list(range(n))
        for j in range(n):
            totalTime = 0
            for i in range(iterations):
                t0 = timeit.default_timer()
                elem = listNum[j]
                t1 = timeit.default_timer()
                totalTime += t1 - t0
            outF.write(str(j) + " " +  str(totalTime/iterations) + "\n" )
    print(timeTestLookups(1000, 1000000))
    outF.close()
    
#Append time function
def timetestAppends(runs, n):
    outF = open("out3.csv", "w")
    numberList = []
    for j in range(n):
        total = 0
        for i in range(runs):
            start = timeit.default_timer()
            numberList.append(1)
            end = timeit.default_timer()
            total += end - start
        #print(j, total/runs)
        outF.write(str(j) + "," + str(total/runs) + "\n")
    outF.close()
