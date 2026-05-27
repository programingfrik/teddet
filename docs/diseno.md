TEDDET Diseño
=============

texto es data, data es texto.

Este proyecto son 2 cosas: 
 - Una librería para extraer data de ficheros de texto, csv, columnas de anchofijo, otros? y para poner data en forma de esos formatos de texto, esta librería está construida sobre Haxe, de forma que esté disponible para diferentes lenguajes y plataformas, inicialmente, python y csharp.
 - También es una interface gráfica hecha en python que permita abrir, leer, manipular y crear formatos de ficheros de texto y abrir, leer, manipular y crear ficheros de texto con data, en esos formatos.

La librería está hecha en Haxe. Inicialmente se trans-compila a python y a csharp.

La interface gráfica de usuario está hecha en python usando tk inter, tratando de que se vea lo más moderno posible, usando la versión "moderna" y lo menos feito posible, pero en realidad priorizando lo funcional.

Estoy usando como ejemplo de como debería ser implementada una librería como esta la librería estandar de python para manejar csv [https://docs.python.org/3/library/csv.html].


Diseño libteddet
================

The chicken and egg problem of libteddet
----------------------------------------

Libteddet wants to re-use the same functions it uses to read delimited files and fixed width files with its own file formats. But there is a little problem, to read a file and validate it, it needs the format of a file, to read a format, it needs the format's format file, that is also needed to read itself. So how is this problem solved. One idea is to have the format's format preloaded as literal values inside the library, another idea is to have a minimum amount of the relevant information to use it as a bootstrap, another one is to load the format's format without any check and have some special fuction to read it. This last solution is the one I'm choosing.

Classes and its roles
---------------------

### TDReader ###

The class that has the functions to read the files.

It can have a Format object to help it know better the file that its reading.

A TDReader can be used to iterate through a File.

The file can be read line by line, each line a row.

If a TDFormat was provided to the TDReader, and it has validation rules, while it reads a file the TDReader object can check that the file complies with the types and settings expressed in the format as well as the validation rules.

### TDWriter ###

The class that has the functions to write a File

It can have a Formate object to help it know better the file that is writing.

Once the class is created, the values pass to it will form a register.

The TDWriter validates the data that it will write against the TDFormat information, tipes, lengths, fields, and validation rules.

### TDFormat ###

The class that contains the information that describes a file format.


Diseño teddetgui
================

La pantalla principal es una ventana con una cuadrícula, un espacio para poner las tablas de texto.

Como un fichero puede tener varias tablas el espacio principal puede tener una serie de tablas.

La ventana principal tiene un menú con opciones archivo, editar, etc.
