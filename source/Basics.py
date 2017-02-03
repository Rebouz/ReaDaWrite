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
