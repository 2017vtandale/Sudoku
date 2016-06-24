__author__ = 'Vishal Tandale'
#Vishal Tandale
import sys, string, time
global counter
counter = 0
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

#Create Possible Groups
def cgroups(pos):
    Group = {}
    Group["rows"] = {(i+((pos)*9)) for i in range(9)}
    Group["col"] = {((pos) +(i)*9) for i in range((9))}
    Group["grp"] = []
    Start = [0,3,6,27,30,33,54,57,60]
    start = Start[pos]
    for i in range(1,3):
        Group["grp"].append(start+i)
        Group["grp"].append(start+9*i)
        Group["grp"].append(start+(i)*(9+1))
    Group["grp"].append(start)
    Group["grp"].append(start+9+2)
    Group["grp"].append(start+18+1)
    Group["grp"] = set(Group["grp"])
    return Group

def getGrp(pos,agrp):
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
    return grp
	
	

def cagrps(puzzle):
    agrps = {"row":{},"col":{},"grp":{}}
    for x in range(9):
        Temp = cgroups(x)
        agrps["row"][x] = Temp["rows"]
        agrps["col"][x] = Temp["col"]
        agrps["grp"][x] = Temp["grp"]
    dictpos = {}
    i = 28
    dictpos[i] = {puzzle[grp] for grp in agrps["row"][int(i/9)]}
    dictpos[i] = {puzzle[grp] for grp in agrps["col"][i%9]}
    dictpos[i] = {puzzle[grp] for grp in agrps["grp"][getGrp(i,agrps)]}
    #dictpos[i] = set('123456789')-(({puzzle[grp] for grp in agrps["row"][int(i/9)]} | {puzzle[grp] for grp in agrps["col"][i%9]} | {puzzle[grp] for grp in agrps["grp"][getGrp(i,Temp[1])]})-{'.'})
    for i in range(81):
        if(puzzle[i])=='.':
            dictpos[i] = set('123456789')-(({puzzle[grp] for grp in agrps["row"][int(i/9)]} | {puzzle[grp] for grp in agrps["col"][i%9]} | {puzzle[grp] for grp in agrps["grp"][getGrp(i,agrps)]})-{'.'})
    return [dictpos,agrps]

def remove(min, agrp, dictpos, c):
    row = int(min/9)
    col = (min)%9
    grp = getGrp(min,agrp)
    for x in agrp["row"][int((min)/9)]:
        if x in dictpos and c in dictpos[x]:
            dictpos[x] = dictpos[x]-{c}
    for x in (agrp["col"][(min)%9]):
        if x in dictpos and c in dictpos[x]:
            dictpos[x] = dictpos[x]-{c}
    for x in (agrp["grp"][getGrp(min,agrp)]):
        if x in dictpos and c in dictpos[x]:
            dictpos[x] = dictpos[x]-{c}
    del dictpos[min]

def bruteForce(puzzle,Lists):
    dctpos = Lists[0]
    agrps = Lists[1]
    min = puzzle.find('.')
    if(min<0):
        if not (validateSolution(puzzle)):
            return ""
        else:
            return puzzle
    for i in range(len(puzzle)):
        if puzzle[i] == '.':
            if len(dctpos[i])==1:
                min = i
                break
            if len(dctpos[i])<len(dctpos[min]):
                min = i
    for c in dctpos[min]:
        global counter
        counter+=1
        newpuz = puzzle[:min]+c+puzzle[min+1:]
        #print()
        #printneat(newpuz)
        dctPosC = {key: dctpos[key].copy() for key in dctpos}
        remove(min,agrps,dctPosC,c)
        bf = bruteForce(newpuz,[dctPosC, agrps])
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

File = "sudoku141.txt"
Temp = open(File).read().split()
#printneat(Temp[56])
#printneat(bruteForce(Temp[12],cagrps(Temp[12])))
Start = time.clock()
for i in range(0,len(Temp)):
	print(str(i+1)+": "+Temp[i])
	counter = 0
	T= time.clock()
	Temp1 = bruteForce(Temp[i],cagrps(Temp[i]))
	T = time.clock()-T
	print(str(i+1)+": "+Temp1)
	print("")
	print("Guesses: "+str(counter))
	print("Time: "+str(T))
	print("")
print("Time it takes: "+str(time.clock()-Start))

#sys.argv[1] = '1'
#sys.argv[2] = '128'
if len(sys.argv)>2:
    Start = time.clock()
    if int(sys.argv[1])==0:
        print("What Puzzle zero?")
        sys.argv[1] = 1
    for i in range(int(sys.argv[1])-1,int(sys.argv[2])):
        print(str(i+1)+": "+Temp[i])
        counter = 0
        T= time.clock()
        Temp1 = bruteForce(Temp[i],cagrps(Temp[i]))
        T = time.clock()-T
        print(str(i+1)+": "+Temp1)
        print("")
        print("Guesses: "+str(counter))
        print("Time: "+str(T))
        print("")
    print("Time it takes: "+str(time.clock()-Start))
elif len(sys.argv)>1:
    if int(sys.argv[1])==0:
        print("What Puzzle zero?")
    else:
        printneat(Temp[int(sys.argv[1])-1])
        T = time.clock()
        List = cagrps(Temp[int(sys.argv[1])-1])
        #print(List[1])
        printneat(bruteForce(Temp[int(sys.argv[1])-1],cagrps(Temp[int(sys.argv[1])-1])))
        print("Guesses: "+str(counter))
        print("Time: "+ str(time.clock()-T))
