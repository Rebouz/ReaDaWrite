import os,sys,time,easygui

global lastObj
lastObj = ""

#Modules:
#Utils
#Basics
#Clear
#Format

def createObj(filename):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if not os.path.isfile(filepath):
        file = open(filepath, "w+")
        file.write("")
        file.close()
        print("successfully created Object '"+filename+"'")
        return True

    else:
        print("File already exists")
        return False

def addAttr(filename, count, attr):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if os.path.isfile(filepath):
        file = open(filepath, "a")
        file.write(count+"\t"+attr+"\n")
        file.close()
        return True
    else:
        print("File not found, creating one.")
        createObj(filename)
        addAttr(filename, count, attr)
        return True

def printObj(filename):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if os.path.isfile(filepath):
        file = open(filepath, "r")
        for line in file.read().split("\n"):
            print(line)
        file.close()
        return True
    else:
        print("File '"+filename+"' not found.")
        return False

def delObj(filename):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if os.path.isfile(filepath):
        os.remove(filepath)
        print("successfully removed Object '"+filename+"'")
        return True
    else:
        print("File '"+filename+"' not found.")
        return False

def delAttr(filename, attr):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if os.path.isfile(filepath):
        file = open(filepath, "r")
        tmp = file.read().split("\n")
        newtmp=[]
        for item in tmp:
            if item == "":
                continue
            itemS = item.split("\t")
            if (len(itemS)==2 and attr not in itemS[1]) or (len(itemS)==3 and attr not in itemS[2]):
                newtmp.append(item)
        file.close()

        file = open(filepath, "w")
        for item in newtmp:
            file.write(item+"\n")
        file.close()
        return True
    else:
        print("File '"+filename+"' not found.")
        return False

def clearObj(filename):
    print("Attempting to clear '"+filename+"'")
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if os.path.isfile(filepath):
        file = open(filepath, "r")
        arr=file.read().split("\n")
        file.close()
        arr=clearArr(arr)
        arr=reformat(arr)
        file = open(filepath, "w")
        for item in arr:
            file.write(item+"\n")
        file.close()
        return True
    else:
        print("File '"+filename+"' not found.")
        return False

def clearObjs():
    objs = os.listdir("objects\\")
    tmp=[]
    for item in objs:
        tmp.append(item[:-4])
    print("Clearing the Objects: "+str(tmp))
    for item in tmp:
        clearObj(item)
    usedObjects=[]

def reformat(arr):
    oldArrCounts=[]
    oldArrItems=[]
    for item in arr:
        item = item.split("\t")
        oldArrCounts.append(item[0])
        oldArrItems.append(item[1])

    newArrItems=clearDuplicates(oldArrItems)
    newArrCounts=[]
    newArrItems2 = []
    i=-1
    for item in oldArrItems:
        i+=1
        print("i "+str(i))
        try:
            newArrCounts[newArrItems2.index(item)] += int(oldArrCounts[i])
            print(newArrCounts[newArrItems2.index(item)])
        except ValueError:
            newArrItems2.append(oldArrItems[i])
            newArrCounts.append(int(oldArrCounts[i]))
            print("1st "+str(oldArrItems[i]))

    print(newArrItems, newArrItems2, newArrCounts)
    newArr=[]
    i=-1
    for item in newArrItems2:
        i+=1
        print("i "+str(i))
        newArr.append(str(newArrCounts[i])+"\t"+newArrItems2[i])
    return newArr

def toWords(text):
    arr = text.split(" ")
    arr2 = []
    itemIndex=-1
    specialChars=["+","-","*","/","(",")","[","]","{","}","?","!",".","_","~","#","'","\"","=","<",">","|","$","§","%","&","´","`","²","³","@",";",":","\n","\t","\v","\r","."]
    string=""
    for item in arr:
        itemIndex=itemIndex+1
        item2=""
        for char in item:
            isSpecial=False
            for i in specialChars:
                if (char==i):
                    print("found '" +char+"' in '"+item)
                    isSpecial=True
            if not isSpecial==True:
                item2=item2+char
            else:
                print("cleared out '"+char+"' in '"+item+"'")
        arr[itemIndex]=item2
    print("new array:")
    for item in arr:
        string=string+item+", "
    print(string)
    return clearArr(arr)


def killUnvaluables(words):
    words2 = []
    for word in words:
        if (len(word)>3) and (getItemCount(word, words)> 0.125*len(words) and len(words)>8):
            print("passed word '"+word+"'")
            words2.append(word)
        elif not word[0].lower()==word[0]:
            print("passed word '"+word+"'")
            words2.append(word)            
    return words2

def addWordsToData(arr):
    for item in arr:
        item = item.lower()
        createObj(item)
        for item2 in arr:
            item2 = item2.lower()
            if not item==item2:
                addAttr(item,"1",item2)


def getSentencesFromText(text):
    arr=[]
    for item in text.split(". "):
        if not ("\n" in item) and not ("\t" in item) and not ("\v" in item) and not ("\r" in item):
            arr.append(item)
            print(item)
    return arr

def dataFromSentences(text):
    print("adding:")
    for sentence in getSentencesFromText(text):
        for item in killUnvaluables(toWords(sentence)):
            print(item)
        addWordsToData(killUnvaluables(toWords(sentence)))

def dataFromTXT():
    file = open("input.txt", "r")
    dataFromSentences(file.read())
    file.close()

def clearDuplicates(arr):
    arr2 = list(set(arr))
    arr2.reverse()
    return arr2

def getMostCommon(lst):
    return max(set(lst), key=lst.count)

def getItemCount(item, lst):
    return lst.count(item)

def itemExists(item, arr):
    for i in arr:
        if item==i:
            return true
    return false


def delItemInList(item, arr):
    tmp=[]
    for item2 in arr:
        if not item2==item:
            tmp.append(item2)


def clearArr(arr):
    arr2 = []
    itemIndex=-1
    for item in arr:
        itemIndex=itemIndex+1
        if not item == "":
            arr2.append(item)
        else:
            print("cleared out empty Item at Position "+str(itemIndex))
    return arr2

def getItemCounts(arr):
    items=[]
    itemcounts=[]
    items=clearDuplicates(arr)
    i=-1
    for item in items:
        i=i+1
        itemcounts[i]=getItemCount(item, arr)

    return items, itemcounts

##def getRawAttrList(filename):
##    arr=[]
##    filename = filename.lower()
##    filepath="objects\\"+filename+".txt"
##    if os.path.isfile(filepath):
##        file = open(filepath, "r")
##        for line in file.read().split("\n"):
##            arr.append(line.split("\t")[1])
##        file.close()
##    else:
##        print("File '"+filename+"' not found.")
##    return arr

def main():
    global lastObj
    inp = clearArr(input("Your CMD > ").split(" "))
    
    if not lastObj=="":
        inp.insert(1, lastObj)
    if inp==[] or inp[0]=="listObjs":
        x = os.listdir("objects\\")
        for item in x:
            print(item)
    elif inp[0]=="addAdj":
        x = addAttr(inp[1], "a", inp[2])
        if not x:
            print("something went wrong")
        else:
            printObj(inp[1])
            
    elif inp[0]=="createObj":
        x = createObj(inp[1])
        if not x:
            print("something went wrong")
            
    elif inp[0]=="delObj":
        x = delObj(inp[1])
        if not x:
            print("something went wrong")
            
    elif inp[0]=="printObj":
        x = printObj(inp[1])
        if not x:
            print("something went wrong")

    elif inp[0]=="setObj" and len(inp)==2:
        lastObj = inp[1]

    elif inp[0]=="addFromText":
        x = input("[German] Bitte einen Satz eingeben: ")
        dataFromSentences(x)

    elif inp[0]=="useTXT":
        dataFromTXT()
        
        
    clearObjs()
    main()

def firstStart():
    print("Create Object: 'createObj [obj]'")
    print("Add Adjective: 'addAdj [obj] <attribute>'")
    print("Add Relation: 'addRelation [obj1] <obj2>'")
    print("Print Object: 'printObj [obj]'")
    print("Delete Object: 'delObj [obj]'")
    print("Delete Attribute: 'delAttr [obj] <attribute>'")
    print("Set Object: 'setObj <obj>'")
    print("Automatically Filter new Data: 'addFromText'")
    print("List all Objects: 'listObjs'")
    print("Take Data out of input.txt: 'useTXT'")
    main();
firstStart()
