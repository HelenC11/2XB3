<<<<<<< HEAD
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

=======

def are_valid_groups(listStudentNum, listOfGroups):
  result = True
  for x in listStudentNums:
       result = any(x in sl for sl in listOfGroups)
       if result == False:
           return False
                
  return result

HAHAKJSKAJSLAJLSJALJKWNLKDNDJA"J"K"AKSLNKNSL:ASLKAS"KA"S:KALSMASM<MSLAKQLEKN><DA><
>>>>>>> c2d3f6235e98504a1daefc1acd8d7de366593ba1
