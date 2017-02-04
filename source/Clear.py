def clearObj(filename):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    mergePlurals("objects\\"+filename)
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

def mergePlurals(filename):
    if os.path.isfile(filename[:-2]+".txt"):
        print("trying to merge some files...")
        mergeFiles(filename[:-2]+".txt", filename+".txt")
        return True
    else:
        return False

def mergeFiles(file1, file2):
    try:
        file = open(file1, "r")
        tmp=file.read()
        file.close()
        file = open(file2, "r")
        tmp+="\n"+file.read()
        file.close()
        file = open(file1, "w")
        file.write(tmp)
        file.close()
        os.remove(file2)
        print("merged files to '"+file1+"'.")
        return True
    except IOError:
        print("either '"+file1+"' or '"+file2+"' was not found")
        print("couldn't merge files.")
        return False
    
