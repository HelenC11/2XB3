import timeit


#Append time function
def timetestAppends(runs, n):
    outF = open("out3.csv", "w")
    numberList = []
    for j in range(n):
        total = 0
        for i in range(runs):
            start = timeit.default_timer()
            numberList.append(j)
            end = timeit.default_timer()
            total += end - start
        #print(j, total/runs)
        outF.write(str(j) + "," + str(total/runs) + "\n")
    outF.close()

