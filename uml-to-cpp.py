# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-05
from datetime import date

class UmlClass:
    def __init__(self, className):
        self.name = className
        self.hppPrivate = ["private:"]
        self.hppPublic = ["public:"]
        self.cpp = [ # will contain final version of cpp file
            "// Copyright (C) 2016. All rights reserved.",
            "// Created: " + str(date.today()),
            "",
            "#include \"" + self.name + ".hpp\"", 
        ]
        self.hpp = [ # will contain final version of hpp file
            "// Copyright (C) 2016. All rights reserved.",
            "// Created: " + str(date.today()),
            "",
            "#ifndef " + self.name + "_hpp", 
            "#define " + self.name + "_hpp",
            "",
            "class " + self.name,
            "{",
            "};",
            "#endif"
        ]

    indent = "    " # soft tab size 4

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

    def formatHpp(self):
        self.moveReturnType()
        self.includeLibs()
        self.addNamespace()
        self.indentAndSemiColon()

    def build(self):
        self.buildHpp()
        self.formatHpp()
        self.buildCpp()
        self.formatCpp()

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
        notMember = ["/", "#", "class ", "{", "}", "public:", "private:", "protected:", "return"]
        if any(notM in line for notM in notMember) or line == "":
            return False
        else:
            return True

    def indentAndSemiColon(self):
        for line in self.hpp:
            i = self.hpp.index(line)
            if self.isMember(line):
                line = self.indent + line + ";"
                self.hpp[i] = line

    def buildCpp(self):
        for line in self.hpp:
            if (self.isFunction(line)):
                self.cpp.append(line[len(self.indent):-1]) # remove indent and ;

    def formatCpp(self):
        for line in self.cpp:
            i = self.cpp.index(line)
            if self.isMember(line):
                line = self.insertClassName(line)
                # Add function body
                line = "\n" + line + "\n{\n" + self.indent + self.insertReturnType(line) + "\n}"
                self.cpp[i] = line

    def insertReturnType(self, line):
        line = line[:line.index("(")]

        # If return type exists, construct a return statement
        if len(line.split()) > 1:
            if line[:line.index(self.name)].strip() == "void":
                return ""
            else:
                return "return " + self.findReturnDefault(line) + ";"
        else:
            return ""

    def findReturnDefault(self, line):
        line = line[:line.index(self.name)].strip()

        # Check for data types and return some default zero value
        if line == "int" or line == "char" or line == "double" or line == "float" or line == "short":
            return "0"
        elif line == "std::string":
            return "\"\""
        elif line == "bool":
            return "false"
        elif line == "void":
            return ""
        else:
            return ""

    def insertClassName(self, line):
        # Search and insert className::
        splitLine = line.split()
        for bit in splitLine:
            j = splitLine.index(bit)
            if "(" in bit:
                bit = self.name + "::" + bit
                splitLine[j] = bit
        if len(splitLine) > 1:
            line = " ".join(splitLine)
        else:
            line = "".join(splitLine)
        return line

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

# Main function
print("[ UML to CPP ] Create .hpp and .cpp files from UML.txt")
print("> Attempting to create files...")
umlFile = open("UML.txt", 'r')

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