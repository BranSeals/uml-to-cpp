# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-05
from UmlClass import UmlClass

print("== UML to CPP ==")
print("Create or modify C++ header and implementation files by plaintext UML.")

#print("Enter a UML filename: ") # file import currently disabled
umlFile = open("ExampleUML.txt", 'r')
# TODO: check if file isn't too bonkers, and properly formatted

uml = umlFile.read().splitlines() # pull UML into memory, 1 line per element

for line in uml:
    if line[:5] == "class" and line[-1:] == "{":
        obj = UmlClass(line[6:-2])
    elif line[:1] == "+":
        obj.addToPublic(line[1:])
    elif line[:1] == "-":
        obj.addToPrivate(line[1:])
    elif line == "}":
        obj.build()
        filesCreated += 2
    else:
        print("> Syntax error in UML file")

print("> " + str(filesCreated) + " files created")