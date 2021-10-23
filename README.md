# UML to CPP

## About

I'm tired of manually creating C++ class UML, header, and implementation files from scratch. The information contained in a UML is enough to generate these files automatically, so let's do that.

This project takes a plaintext UML file as input and uses it to create .hpp and .cpp files for each listed class. Functions, parameters, and return types are taken into account along with a basic code template.

The expected formatting of the plaintext UML file matches [PlantText](https://www.planttext.com/).

## Status

This project is not currently being developed or maintained.

Not all containers and data types are supported, but most are. Files contain proper C++ syntax, unless more complex containers and data types are used. 

## Potential Updates
* The ability to select file input and output locations. 
* The ability to modify existing class files using the same UML.txt file, keeping any present code intact. 

## Operation

Execute uml-to-cpp.py in the same directory as UML.txt. Additional files will be created in this same location.

For each class listed in the UML.txt file, a header file (.hpp) and implementation file (.cpp) is created. These files also include a code template that can be expanded depending on the information in the UML. If data members, member functions, and variable names are specified, these are added into the files along with supporting code. Data types that require additional libraries will automatically include these libraries. Currently, member functions with return types will return a zero or equivalent to prevent compilation errors.

## UML Example Format

~~~
class MyClass {
+publicFunction(int) : string
-privateMember : int
}
~~~

Default constructors and destructors do not have to be specified, and are taken into account to avoid duplicates if included. If parameter names exist, they will be included in the final code files. Currently, relationships and inheritance are not supported.

UML.txt is included with the project to experiment with the UML import and translation. The project could be expanded to handle more classes and weirder structures.

## Author

Bran Seals; Senior QA Engineer. I'm more apt to break code than create it, so I'm happy to receive input, advice, criticism, or other forms of help.
