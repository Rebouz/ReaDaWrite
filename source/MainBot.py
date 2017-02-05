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
        if len(inp) == 2:
            dataFromTXT(inp[1])
        else:
            dataFromTXT()
        
        
    clearObjs()
    main()

def firstStart():
    if not os.path.exists("objects\\"):
        os.makedirs("objects\\")
    
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
