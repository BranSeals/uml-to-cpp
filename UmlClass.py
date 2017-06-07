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

    def addToPublic(self, pubMember): # adds given string to public scope list
        self.hppPublic.append(pubMember)

    def addToPrivate(self, privMember): # adds given string to private scope list
        self.hppPrivate.append(privMember)

    def isFunction(self, line):
        if "(" in line and ")" in line and "(C)" not in line:
            return True

    def includeLibs(self): # include libraries for data types that need them
        
        # Data types being searched
        stringFound = False
        vectorFound = False

        # Search for types with required libraries
        for line in self.hpp:
            if "std::string" in line:
                stringFound = True
            if "std::vector" in line:
                vectorFound = True

        # Include libraries, along with extra space if found
        if stringFound:
            self.hpp[self.hpp.index("class " + self.name):1] = ["#include <string>"]
        if vectorFound:
            self.hpp[self.hpp.index("class " + self.name):1] = ["#include <vector>"]
        if stringFound or vectorFound:
            self.hpp[self.hpp.index("class " + self.name):1] = [""]

    def buildHpp(self):
        # Insert public members after {, where class begins
        self.hpp[self.hpp.index("{")+1:1] = self.hppPublic

        # Insert private members after last public member
        self.hpp[self.hpp.index(self.hppPublic[-1])+1:1] = self.hppPrivate

    def build(self):
        self.buildHpp()
        self.moveReturnType()
        self.includeLibs()
        self.addNamespace()
        self.buildCpp()
        self.indentHpp() # indent here for easier cpp building

    def addNamespace(self):
        for line in self.hpp:
            i = self.hpp.index(line)
            if "string" in line:
                line = line.replace("string", "std::string", 1)
                self.hpp[i] = line
            if "vector" in line:
                line = line.replace("vector", "std::vector", 1)
                self.hpp[i] = line

    def moveReturnType(self):
        for line in self.hpp:
            i = self.hpp.index(line)
            if " : " in line:
                line = line[line.index(":")+1:].strip() + " " + line[:line.index(":")].strip()
                self.hpp[i] = line

    def isMember(self, line):
        notMember = ["/", "#", "class ", "{", "}", "public:", "private:", "protected:"]
        if any(notM in line for notM in notMember) or line == "":
            return False
        else:
            return True

    def indentHpp(self):
        indent = "    "
        for line in self.hpp:
            i = self.hpp.index(line)
            if self.isMember(line):
                line = indent + line
                self.hpp[i] = line

    def buildCpp(self):
        for line in self.hpp:
            if (self.isFunction(line)):
                self.functions.append(line)
        # for each in function list, append it to cpp using formatFunc()

    def createFiles(self):
        self.build()

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