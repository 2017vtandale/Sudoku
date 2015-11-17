__author__ = 'Vishal Tandale'
#Vishal Tandale
import sys, string, time
global counter
counter = 0
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
    for x in agrp["grp"]:
        if pos in agrp["grp"][x]:
            return x

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
    return {"dctpos":dictpos,"agrps":agrps}

def remove(min, agrp, dictpos, c):
    for x in agrp["row"][int(min/9)]:
        if x in dictpos and c in dictpos[x]:
            dictpos[x] = dictpos[x]-{c}
    for x in (agrp["col"][min%9]):
        if x in dictpos and c in dictpos[x]:
            dictpos[x] = dictpos[x]-{c}
    for x in (agrp["row"][getGrp(min,agrp)]):
        if x in dictpos and c in dictpos[x]:
            dictpos[x] = dictpos[x]-{c}

def bruteForce(puzzle,Lists):

    min = puzzle.find('.')
    for i in range(len(puzzle)):
        if puzzle[i] == '.':
            if len(Lists["dctpos"][i])==1:
                min = i
                break
            if len(Lists["dctpos"][i])<len(Lists["dctpos"][min]):
                min = i
    Group = Lists["dctpos"][min]
    for c in Group:
        global counter
        counter+=1
        newpuz = puzzle[:min]+c+puzzle[min+1:]
        print()
        printneat(newpuz)
        dctPosC = {key: Lists["dctpos"][key].copy() for key in Lists["dctpos"]}
        remove(min,Lists["agrps"],dctPosC,c)
        bf = bruteForce(newpuz,[dctPosC,Lists["agrps"]])
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
printneat(Temp[12])
printneat(bruteForce(Temp[12],cagrps(Temp[12])))
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
        print(str(i+1)+": "+Temp1)
        print("")
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
        print("Guesses: "+str(counter))
        print("Time: "+ str(time.clock()-T))