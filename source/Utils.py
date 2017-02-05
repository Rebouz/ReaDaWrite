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
            return True
    return False


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
