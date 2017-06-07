# Copyright (C) 2017 Bran Seals. All rights reserved.
# Created: 2017-06-05
from datetime import date

# UmlClass translates plaintext UML file into .hpp and .cpp files
class UmlClass:

    # Initialize with these values to return to default .hpp/.cpp in loop
    def __init__(self, className):
        self.name = className

        # List of private and public members
        self.hppPrivate = ["private:"]
        self.hppPublic = ["public:"]

        # Starting .cpp template
        self.cpp = [
            "// Copyright (C) 2016. All rights reserved.",
            "// Created: " + str(date.today()),
            "",
            "#include \"" + self.name + ".hpp\""
        ]

        # Starting .hpp template
        self.hpp = [
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

    # Soft tab size 4
    indent = "    "

    # Adds a given string to public member list
    def addToPublic(self, pubMember):
        self.hppPublic.append(pubMember)

    # Adds a given string to private member list
    def addToPrivate(self, privMember):
        self.hppPrivate.append(privMember)

    # Checks if given string is a member function
    def isFunction(self, line):
        if "(" in line and ")" in line and "(C)" not in line:
            return True

    # Searches and includes libraries for data types that need them
    # Requires namespace to be assigned before this function is called
    def includeLibs(self):

        # Data types being searched
        stringFound = False
        vectorFound = False

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

    # Builds hpp using public and private member lists
    def buildHpp(self):
        # Insert public members after {, where class begins
        self.hpp[self.hpp.index("{")+1:1] = self.hppPublic
        # Insert private members after last public member
        self.hpp[self.hpp.index(self.hppPublic[-1])+1:1] = self.hppPrivate

    # Formats hpp list into proper .hpp syntax
    def formatHpp(self):
        self.moveReturnType()
        self.addNamespace()
        self.includeLibs()
        self.indentAndSemiColon()

    # Build and format hpp and cpp lists
    def build(self):
        self.buildHpp()
        self.formatHpp()
        self.buildCpp()
        self.formatCpp()

    # Adds std:: prefix to data types that require it
    def addNamespace(self):
        for line in self.hpp:
            i = self.hpp.index(line)
            if "string" in line:
                line = line.replace("string", "std::string", 1)
                self.hpp[i] = line
            if "vector" in line:
                line = line.replace("vector", "std::vector", 1)
                self.hpp[i] = line

    # Swaps location of returned data type
    def moveReturnType(self):
        for line in self.hpp:
            i = self.hpp.index(line)
            if self.isMember(line):
                if " : " in line:
                    line = line[line.index(":")+1:].strip() + " " + line[:line.index(":")].strip()
                else:
                    line = "void " + line
            self.hpp[i] = line

    # Checks if given string is a member function of data member
    # This determines if a line needs to be formatted or not
    def isMember(self, line):
        notMember = ["/", "#", "class ", "{", "}", "public:", "private:", "protected:", "return"]
        if any(notM in line for notM in notMember) or line == "":
            return False
        else:
            return True

    # Indents a member and adds semicolon at the end
    def indentAndSemiColon(self):
        for line in self.hpp:
            i = self.hpp.index(line)
            if self.isMember(line):
                line = self.indent + line + ";"
                self.hpp[i] = line

    # Builds cpp list using members in hpp list
    # Copies member without indent and semicolon
    def buildCpp(self):
        for line in self.hpp:
            if (self.isFunction(line)):
                self.cpp.append(line[len(self.indent):-1]) # remove indent and ;

    # Adds class namespace and function body along with return statement (if needed)
    def formatCpp(self):
        for line in self.cpp:
            i = self.cpp.index(line)
            if self.isMember(line):
                line = self.insertClassName(line)
                # Add function body
                line = "\n" + line + "\n{\n" + self.indent + self.insertReturnType(line) + "\n}"
                self.cpp[i] = line

    # Returns the return statement (if needed)
    def insertReturnType(self, line):
        line = line[:line.index("(")]

        # If return type exists, construct a return statement
        if len(line.split()) > 1:
            if line[:line.index(self.name)].strip() == "void":
                return ""
            else:
                return "\n" + self.indent + "return " + self.findReturnDefault(line) + ";"
        else:
            return ""

    # If there is a return type, inserts a default return value
    # This will prevent compilation errors from the outset
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

    # Returns the class namespace used in the .cpp file
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

    # Builds hpp and cpp lists and creates all relevant files
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