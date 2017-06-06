# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-05

print("== UML to CPP ==")
print("Create or modify C++ header and implementation files by plaintext UML.")
#print("Enter a UML filename: ") # file import currently disabled
# check if file isn't too bonkers
uml = [] # pull UML into memory as string list, 1 line per element
# check if file is properly formatted
# create blank object
noteList = [] # if weird things happen, this list will show potential errors
              # will be displayed after files are created for user info

# for each in uml list:
    # if first 4 = "class" and ends in {:
        # create new object with className
    # if +, obj.addToPublic(uml[current])
    # if -, obj.addToPrivate(uml[current])
    # if neither, obj.addToPrivate(uml[current]) and add message to noteList
    # if }:
        # create name.hpp file and write using hpp list
        # create name.cpp file and write using cpp list

class UmlClass:
    def __init__(self, className):
        self.name = className
        self.cpp = [] # will contain final implementation file
        self.functions = [] # list of functions used to build cpp file
        self.hppPrivate = []
        self.hppPublic = []
        self.hpp = [] # will contain final hpp template, built from hppPub, hppPriv

    def addToPublic(self, pubMember): # adds given string to public scope list
        self.hppPublic.append(pubMember)

    def addToPrivate(self, privMember): # adds given string to private scope list
        self.hppPrivate.append(privMember)

    #def isFunction(): # looks for function syntax
                       # used when creating cpp file from hpp list

    #def checkForLibs(): # include libraries for data types that need them

    #def formatFunc(): # formats function from hpp to cpp style
                       # also takes into account return type and variable names

    #def buildHpp(): # builds hpp using information

    #def buildCpp(): # builds cpp using information

    #def build(): # overall build file function
        #buildHpp()
        #buildCpp()