# UML to CPP

## About

I'm tired of manually creating C++ class UML, header, and implementation files from scratch. Over multiple academic and personal projects, I was spending more time than I needed to create these files and fill them with the same starting code. The information contained in a UML is enough to automatically generate these files.

This project takes a plaintext UML file as input and uses it to create .hpp and .cpp files for each listed class. Each class's functions are taken into account along with parameters and return type and a basic code template is written into these files.

The format of the plaintext UML file matches [PlantText](https://www.planttext.com/) as I use this for my personal projects, but this formatting is subject to change as more features are added to this project.

This project is not currently being developed or maintained.

## Status

Currently, this project is able to create C++ header and implementation files for each class in the plaintext UML.txt file. Not all containers and data types are supported, but most are. Files contain proper C++ syntax and avoid compilation errors at the outset, unless more complex containers and data types are being used. 

Moving forward, I will add the ability to select file input and output locations. I will also add the ability to modify existing class files using the same UML.txt file, keeping any present code intact. 

## Operation

Place uml-to-cpp.py and UML.txt in the same folder. In a terminal, run uml-to-cpp.py at that filepath. Additional files will be created in the same folder.

For each class listed in the UML.txt file, a header file (.hpp) and implementation file (.cpp) is created. These files also include a code template that can be expanded depending on the information in the UML. If data members, member functions, and variable names are specified, these are be added into the files along with supporting code. Data types that require additional libraries will automatically include these libraries. Currently, member functions with return types will return a zero or equivalent to prevent compilation errors, but this behavior is subject to change.

## UML Example Format

~~~
class MyClass {
+publicFunction(int) : string
-privateMember : int
}
~~~

Default constructors and destructors do not have to be specified, and are taken into account to avoid duplicates if included. If parameter names exist, they will be included in the final code files. Currently, relationships and inheritance are not supported.

UML.txt is included with the project to experiment with the UML import and translation. More classes and weirder structures will be added as the project progresses.

## Author

My name is Bran Seals and I am recent Computer Science graduate (AS) based in Columbus, Indiana. I have an interest in most everything, consider myself a lifelong learner, and enjoy being well-rounded.

I'm happy to receive input, advice, criticism, or other forms of help, as there are always new things to learn in this field. If you have any feedback, job opportunities (I'm seeking!), or just want to say hello, feel free to write to brandon.seals@gmail.com.
