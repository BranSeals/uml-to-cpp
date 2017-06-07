# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-05
from UmlClass import UmlClass

print("== UML to CPP ==")
print("Create or modify C++ header and implementation files by plaintext UML.")

#print("Enter a UML filename: ") # file import currently disabled
umlFile = open("ExampleUML.txt", 'r')
# TODO: check if file isn't too bonkers, and properly formatted

uml = umlFile.read().splitlines() # pull UML into memory as string list, 1 line per element

# for each in uml list:
    # if first 4 = "class" and ends in {:
        # create new object with className (will reset previous one)
    # if +, obj.addToPublic(uml[current])
    # if -, obj.addToPrivate(uml[current])
    # if }:
        # obj.build()
        # create name.hpp file and write using hpp list
        # create name.cpp file and write using cpp list
    # if none of above, print error