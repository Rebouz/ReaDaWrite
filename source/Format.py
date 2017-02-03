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
