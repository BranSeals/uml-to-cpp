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
        # create new object with className (use same variable to reset prev object)
    # if +, obj.addToPublic(uml[current])
    # if -, obj.addToPrivate(uml[current])
    # if neither, obj.addToPrivate(uml[current]) and add message to noteList
    # if }:
        # obj.build()
        # create name.hpp file and write using hpp list
        # create name.cpp file and write using cpp list

class UmlClass:
    def __init__(self, className):
        self.name = className
        self.functions = [] # list of functions used to build cpp file
        self.parameters = [] # to help in creating functions
        self.hppPrivate = ["private:"]
        self.hppPublic = ["public:"]
        self.cpp = [ # will contain final version of cpp file
            "// Copyright (C) 2016. All rights reserved.",
            "// Created: ", # add creation date
            "",
            "#include \"" + self.name + ".hpp\"", 
        ]
        self.hpp = [ # will contain final version of hpp file
            "// Copyright (C) 2016. All rights reserved.",
            "// Created: ", # add creation date
            "",
            "#ifndef " + self.name + "_hpp", 
            "#define " + self.name + "_hpp",
            "",
            "class " + self.name,
            "{",
            "};",
            "#endif"
        ] 

    def addToPublic(self, pubMember): # adds given string to public scope list
        self.hppPublic.append(pubMember)

    def addToPrivate(self, privMember): # adds given string to private scope list
        self.hppPrivate.append(privMember)

    #def isFunction(self): # looks for function syntax
                       # used when creating cpp file from hpp list

    #def checkForLibs(self): # include libraries for data types that need them

    #def formatFunc(self): # formats function from hpp to cpp style
                       # also takes into account return type and variable names

    #def buildHpp(self): # builds hpp using information
        # insert "private:"
        # for each in hppPrivate, insert after "private:
        # insert "public:"
        # for each in hppPublic, insert after "public:"

    #def buildCpp(self): # builds cpp using information
        # for each in hpp:
            # if isFunction, append to function list
        # for each in function list, append it to cpp using formatFunc()

    def build(self):
        buildHpp()
        buildCpp()
        checkForLibs()
        # create file: self.name + ".hpp"
        # write with self.hpp
        # close file
        # create file: self.name + ".cpp"
        # write with self.cpp
        # close file