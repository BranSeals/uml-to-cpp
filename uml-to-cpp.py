# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-05
from UmlClass import UmlClass

print("== UML to CPP ==")
print("Create or modify C++ header and implementation files by plaintext UML.")
#print("Enter a UML filename: ") # file import currently disabled
# check if file isn't too bonkers
uml = [] # pull UML into memory as string list, 1 line per element
# check if file is properly formatted
# create blank object

# for each in uml list:
    # if first 4 = "class" and ends in {:
        # create new object with className (use same variable to reset prev object)
    # if +, obj.addToPublic(uml[current])
    # if -, obj.addToPrivate(uml[current])
    # if neither, obj.addToPrivate(uml[current]) and print message
    # if }:
        # obj.build()
        # create name.hpp file and write using hpp list
        # create name.cpp file and write using cpp list