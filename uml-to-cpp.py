# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-05

print("== UML to CPP ==")
print("Create or modify C++ header and implementation files by plaintext UML.")
#print("Enter a UML filename: ") # file import currently disabled
# check if file isn't too bonkers
#uml = [] # pull UML into memory as string list
# check if file is properly formatted

classList = [] # list of classes that will be created, along with members
noteList = [] # if weird things happen, this list will show potential errors
              # will be displayed after files are created for user info

# while uml list items exist:
    # get class name
    # while } not reached:
        # if +, put into hppPub
        # if -, put into hppPriv
        # if neither, put into hppPriv and add message to noteList
    # use these to create UmlClass object and append to classList

# for each in classList:
    # build hpp list using hpp, hppPublic, hppPrivate
    # checkForLibs()
    # while hpp list item exists:
        # if isFunction, append to functions list
    # while functions list item exists:
        # format function and append to cpp list
    # create name.hpp file and write using hpp list
    # create name.cpp file and write using cpp list
    # remove object from classList?

class UmlClass:
    def __init__(self, className, hppPub, hppPriv):
        self.name = className
        self.hppPublic = list(hppPub)
        self.hppPrivate = list(hppPriv)

    functions = [] # list of functions used to build cpp file
    hpp = [] # will contain final hpp template, built from hppPub, hppPriv
    cpp = [] # same as hpp, but with implementation file

    #def isFunction(): # looks for function syntax
                       # used when creating cpp file from hpp list

    #def checkForLibs(): # include libraries for data types that need them

    #def formatFunc(): # formats function from hpp to cpp style
                       # also takes into account return type and variable names