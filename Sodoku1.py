#Vishal Tandale
import sys, string, time
global counter
counter = 0
#check if this is a valid solution
def validateSolution(puzzle):
    '''solution = {}
    count = 0
    for i in range(9):
        solution[i] = {}
        for x in range(9):
            solution[i][x] = puzzle[count:count+1]
            count+=1
    '''
    checkrow = {}
    checkcol = {}
    count = 0
    i = 0
    x = 0
    for i in range(9):
        checkrow.clear()
        for x in range(9):
            Temp = puzzle[count:count+1]
            if not x in checkcol:
                checkcol[x] = {}
            if (Temp in checkrow or Temp in checkcol[x]) and not Temp==".":
                return False
            checkrow[Temp]= ""
            checkcol[x][Temp]=""
            count+=1
    return True

def bruteForce(puzzle):
    if not validateSolution(puzzle):
        return ""
    pos = puzzle.find('.')
    if pos<0: return puzzle
    for c in "123456789":
        global counter
        counter+=1
        bf = bruteForce(puzzle[:pos]+c+puzzle[pos+1:])
        if(bf!=""):
            return bf
    return ""
def printneat(puzzle):
    Temp = ""
    print("|-----------------|")
    count = 0
    for i in range(9):
        if not Temp =="":
            print(Temp)
        Temp = "|"
        for x in range(9):
            Temp+= puzzle[count:count+1]+"|"
            count +=1
    print(Temp)
    print("|-----------------|")


Temp = open("sudoku128.txt").read().split()
#printneat(Temp[10])
'''for i in range(15,20):
        printneat(Temp[i])
        t = time.clock()
        Temp1= bruteForce(Temp[i])
        if(validateSolution(Temp1)):
            printneat(Temp1)
            print(str(time.clock()-t))
        else:
            print("You have an error")
'''
#printneat(bruteForce(Temp[12]))
if len(sys.argv)>2:
    if int(sys.argv[1])==0:
        print("What Puzzle zero?")
        sys.argv[1] = 1
    for i in range(int(sys.argv[1])-1,int(sys.argv[2])):
        print(str(i+1)+": "+Temp[i])
        counter = 0
        T= time.clock()
        Temp1 = bruteForce(Temp[i])
        T = time.clock()-T
        #if(validateSolution(Temp1)):
        print(str(i+1)+": "+Temp1)
        print("")
        #global counter
        print("Guesses: "+str(counter))
        print("Time: "+str(T))
        print("")
elif len(sys.argv)>1:
    if int(sys.argv[1])==0:
        print("What Puzzle zero?")
    else:
        printneat(Temp[int(sys.argv[1])-1])
        T = time.clock()
        printneat(bruteForce(Temp[int(sys.argv[1])]))
        #global counter
        print("Guesses: "+str(counter))
        print("Time: "+ str(time.clock()-T))