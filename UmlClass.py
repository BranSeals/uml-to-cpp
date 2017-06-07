# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-06

class UmlClass:
    def __init__(self, className):
        self.name = className
        self.functions = [] # list of functions used to build cpp file
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

    indent = "    "

    def addToPublic(self, pubMember): # adds given string to public scope list
        self.hppPublic.append(self.indent + pubMember)

    def addToPrivate(self, privMember): # adds given string to private scope list
        self.hppPrivate.append(self.indent + privMember)

    def isFunction(self, line):
        if "(" in line and ")" in line and "(C)" not in line:
            return True

    def includeLibs(self): # include libraries for data types that need them
        for line in self.hpp:
            if "string" in line:
                self.hpp.insert(self.hpp.index("class " + self.name),
                "#include <string>",
                ""
                )

    #def formatFunc(self): # formats function from hpp to cpp style
                           # also takes into account return type and variable names

    def buildHpp(self):
        # add public members after {, where class begins
        self.hpp[self.hpp.index("{")+1:1] = self.hppPublic
        # add private members after last public member
        self.hpp[self.hpp.index(self.hppPublic[-1])+1:1] = self.hppPrivate

    def buildCpp(self):
        for line in self.hpp:
            if (self.isFunction(line)):
                self.functions.append(line[4:])
        # for each in function list, append it to cpp using formatFunc()

    def build(self):
        self.buildHpp()
        #self.buildCpp()
        self.includeLibs()
        # TODO: self.verify() # makes sure each file is properly formatted

        # Create .hpp
        self.hppFile = open(self.name + ".hpp", "w")
        for line in self.hpp:
            self.hppFile.write(line + "\n")
        self.hppFile.close()

        # Create .cpp
        self.cppFile = open(self.name + ".cpp", "w")
        for line in self.cpp:
            self.cppFile.write(line + "\n")
        self.cppFile.close()