TEDDET Design
=============

texto es data, data es texto.

is the spanish for text is data, data is text.

[Versión en español](docs/design.es.md)

This project is 2 things:
 - A library for extracting data from text files, csv, fixed width columns, others? and to put data in the form of text, this library is build on Haxe, so this source code is available for diferent languages and platforms, initialy, python and csharp.
 - It is also a graphical interface build on python that allows to open, read, manipulate and create text file formats and open, read, manipulate and create text files with data, on those formats.

The graphical interface for the users is build on python using tkinter, trying that it looks the most modern possible, usnig the "modern" version and the less ugly possible, but really prioritizing the functionality.

I'm using various projects as examples and as inspiration:
 - [https://docs.python.org/3/library/csv.html] as an example of a library that implements means to manage a csv file.
 - [https://github.com/python/cpython/tree/3.14/Lib/idlelib] as an example of a user interface build on tkinter.


libteddet design
================

The chicken and egg problem of libteddet
----------------------------------------

Libteddet wants to re-use the same functions it uses to read delimited files and fixed width files with its own file formats. But there is a little problem, to read a file and validate it, it needs the format of a file, to read a format, it needs the format's format file, that is also needed to read itself. So how is this problem solved. One idea is to have the format's format preloaded as literal values inside the library, another idea is to have a minimum amount of the relevant information to use it as a bootstrap, another one is to load the format's format without any check and have some special fuction to read it. This last solution is the one I'm choosing.

Classes and its roles
---------------------

### TDReader ###

The class that has the functions to read the files.

It can have a TDFormat object with its full information to help it know better the file that its reading, or it can have a small sub set of the TDFormat information, or it can try to guess the file format.

A text file can have more than one table. One can iterate over the tables.

A TDReader can be used to iterate through the rows of each table in a text file.

Also the TDReader allows to access each line or row, one by one.

If a TDFormat was provided to the TDReader, and it has validation rules, while it reads a file the TDReader object can check that the file complies with the types and settings expressed in the format as well as the validation rules.

The minimum information that the TDDataReader needs from a TDFormat is:
 - The file type
 - If its a delimited file, it needs the delimiter.
 - If its a fixed width file, it needs the length of each field.
 - If it has one table or multiple tables.
 - Does the file has headers or not.

Properties:
 - file
 - format
 
Functions:
 - new
 - read_row()
 - read_table()
 - read_file()

### TDWriter ###

The class that has the functions to write a File

It can have a Formate object to help it know better the file that is writing.

Once the class is created, the values pass to it will form a register.

The TDWriter validates the data that it will write against the TDFormat information, tipes, lengths, fields, and validation rules.

Properties:
 - file
 - format
 
 Functions:
 - new
 - write_row()
 - write_table()
 - write_file()
 
### TDFormat ###

The class that contains the information that describes a file format.

A format can be read from a file or it can be build from scratch programaticaly.

Properties:
 - frmtbase
 - frmtf
 - frmtfh
 - name
 - description
 - fileType
 - tableHaveHeaders
 - tables
 - rules
 
 Functions:
 - new

A format can be represented as a multi table coma delimited text file.

teddetgui design
================

La pantalla principal es una ventana con una cuadrícula, un espacio para poner las tablas de texto.

Como un fichero puede tener varias tablas el espacio principal puede tener una serie de tablas.

La ventana principal tiene un menú con opciones archivo, editar, etc.
