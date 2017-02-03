import os

sourcedir="source\\"

#Import MainTop.py as first Module
fileO = open(sourcedir+"MainTop.py", "r")
output = fileO.read()
fileO.close()

for file in os.listdir(sourcedir):
    if file.endswith(".py") and file!="MainTop.py" and file!="MainBot.py":
        fileO = open(sourcedir+file, "r")
        fileR = fileO.read()
        fileO.close()
        output += "\n" + fileR

fileO = open(sourcedir+"MainBot.py", "r")
output += "\n" + fileO.read()
fileO.close()

fileW = open("KI.py", "w")
fileW.write(output)
fileW.close()
