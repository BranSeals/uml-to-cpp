# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-06

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
        # find index of "{" in hpp
        # for each in hppPublic, insert into hpp
        # for each in hppPrivate, insert into hpp

    #def buildCpp(self): # builds cpp using information
        # for each in hpp:
            # if isFunction, append to function list
        # for each in function list, append it to cpp using formatFunc()

    def build(self):
        buildHpp()
        buildCpp()
        checkForLibs()
        # TODO: verify() # makes sure each file is properly formatted
        # create file: self.name + ".hpp"
        # write with self.hpp
        # close file
        # create file: self.name + ".cpp"
        # write with self.cpp
        # close file