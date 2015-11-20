__author__ = 'Vishal Tandale'
#Vishal Tandale
import sys, string, time
global counter
counter = 0
#check if this is a valid solution
def validateSolution(puzzle):
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


def groups(puzzle, pos):
    Group = {}
    row = int(pos/9)
    column = pos%9
    if(row<3 and column<3):
        grp = 1
    elif(row<3 and column<6):
        grp=2
    elif(row<3 and column<9):
        grp = 3
    elif(row<6 and column<3):
        grp=4
    elif(row<6 and column<6):
        grp = 5
    elif(row<6 and column<9):
        grp=6
    elif(row<9 and column<3):
        grp = 7
    elif(row<9 and column<6):
        grp=8
    elif(row<9 and column<9):
        grp=9
    grp+=-1
    #grp = (int((row)/3)+int((column)/3))+int((row)/3)*int((column)/3)
    dctpos = {}
    Group["rows"] = {puzzle[(i+((row)*9))] for i in range(9)}
    Group["col"] = {puzzle[((column) +(i-1)*9)] for i in range((9))}
    Group["grp"] = {}
    #print((3*(grp%3))+ 9*int(grp/3))
    #start = ((3*(grp%3)) + 9*int(grp/3))+((3*(grp%3))*(9*int(grp/3)))
    Start = [0,3,6,27,30,33,54,57,60]
    start = Start[grp]
    #Group[grp][puzzle[start]]
    for i in range(1,3):
        Group["grp"][puzzle[start+i]] = 0
        Group["grp"][puzzle[start+9*i]] =0
        Group["grp"][puzzle[start+(i)*(9+1)]]=0
    Group["grp"][puzzle[start]] =0
    Group["grp"][puzzle[start+9+2]]=0
    Group["grp"][puzzle[start+18+1]]=0
    #dctpos = {i for i in range(9) if i in Group[0]}
    for i in "123456789":
        if not i in Group["rows"] and not i in Group["col"] and not i in Group['grp']:
            dctpos[i] = 0
    return dctpos

def bruteForce(puzzle):
   #if not validateSolution(puzzle):
    #    return ""
    pos = puzzle.find('.')
    if pos<0: return puzzle
    #for c in "123456789":
    Group = groups(puzzle,pos)
    for c in Group:
        #if not c in Group[0] and not c in Group[1]:
        #if c in Group:
        global counter
        counter+=1
        newpuz = puzzle[:pos]+c+puzzle[pos+1:]
        bf = bruteForce(newpuz)
        if(bf!=""):
            return bf
    return ""
def printneat(puzzle):
    Temp = ""
    count = 0
    for i in range(9):
        if not Temp =="":
            print(Temp)
        Temp = "|"
        if(i%3==0):
            print("-------------------")
        for x in range(9):
            Temp+= puzzle[count:count+1]
            if(count%3==2):
                Temp+="|"
            else:
                Temp+=" "
            count +=1
    print(Temp)
    print("-------------------")


Temp = open("sudoku128.txt").read().split()
#print(int(len(Temp)))
#printneat(Temp[12])
#57printneat(bruteForce(Temp[12]))
#printneat("9876")



#Command Line Stuff

#Range of Values
if len(sys.argv)>2:
    Start = time.clock()
    if int(sys.argv[1])==0:
        print("What Puzzle zero?")
        sys.argv[1] = 1
    for i in range(int(sys.argv[1])-1,int(sys.argv[2])):
        print(str(i+1)+": "+Temp[i])
        counter = 0
        T= time.clock()
        Temp1 = bruteForce(Temp[i])
        print("*"),
        T = time.clock()-T
        if validateSolution(Temp1):
            print(str(i+1)+": "+Temp1)
            print("")
            print("Guesses: "+str(counter))
            print("Time: "+str(T))
            print("")
    print("Total Time"+str(time.clock()-Start))

#Print one puzzle
elif len(sys.argv)>1:
    if int(sys.argv[1])==0:
        print("What Puzzle zero?")
    else:
        printneat(Temp[int(sys.argv[1])-1])
        T = time.clock()
        printneat(bruteForce(Temp[int(sys.argv[1]-1)]))
        print("Guesses: "+str(counter))
        print("Time: "+ str(time.clock()-T))