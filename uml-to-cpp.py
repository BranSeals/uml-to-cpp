# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-05
from UmlClass import UmlClass

print("[ UML to CPP ]")
print("Create or modify C++ header and implementation files by plaintext UML.")
print("> Attempting to create files...")
#print("Enter a UML filename: ") # file import currently disabled
umlFile = open("UML.txt", 'r')
# TODO: check if file isn't too bonkers, and properly formatted

uml = umlFile.read().splitlines() # pull UML into memory, 1 line per element
umlFile.close()
filesCreated = 0

for line in uml:
    if line[:5] == "class" and line[-1:] == "{":
        obj = UmlClass(line[6:-2])
    elif line[:1] == "+":
        obj.addToPublic(line[1:])
    elif line[:1] == "-":
        obj.addToPrivate(line[1:])
    elif line == "}":
        obj.createFiles()
        filesCreated += 2
    elif line == "":
        continue
    else:
        print("> Syntax error in UML file")

print("> " + str(filesCreated) + " files created")