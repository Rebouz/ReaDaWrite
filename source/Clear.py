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
