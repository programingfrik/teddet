TEDDET Requirements
===================

[Versión en español](docs/requirements.es.md)

This requirements, are the list of functionalities that are expected from the solution that this project will produce.

The idea is that the requirements go from the basics, the most needed functionalities to the less frequent used ones.

The order of the things to touch to make a change is, first reconcile the new requirements with the previous ones in this document, then make changes in the design and then make the changes in the files of the source code.

This project consists of 2 sub-parts. The core, the base part, a library that facilitates text files management, fixed with ones, as well as delimited ones, through predefine file formats. The second part a graphical interface to elaborate, formats and also to work with files in those formats. Work with this files means create them, edit, but also convert them to other formats.


Requirements for the library (libteddet)
========================================

This is the part of the library, that is the core of the project. This core requires the next functionalities:

- The library has to be written in HAXE
- From the HAXE version other versions have to be build
  - python version
  - csharp Version
- The library can open files using a format.
- Can be fixed width columns text files
- Can be coma separated text files
- Formats can be chosen for the columns:
  - Text columns
  - Integer columns
  - Decimal numbers columns with arbitrary precision chosen by the user
  - Date and time columns
  - Just date columns
  - Just time colmuns
- Validation rules can be created for those files
  - Validate that a column should only contain decimal digits
  - Validate that a column should only contain a valid decimal number
  - Validate that the records of a fixed width file have the amount of text expected and no more and no less.
  - Validate that a coma separated file has the amount of columns that are expected, meaning the right amount of separators.
  - Validate that a column contains valid date on all records.
  - Validate that on a column of text all characters can be encoded in the codec of the current text.
  - A validation that establishes that a column cant be left blank.
  - A validation that establishes a white list of values that a column can have.
  - A validation that establishes a black list of values that a column can't have.
  - A validation that establishes that all records in a column must match a regular expression.
- The library must be accompanied by a test set and a program to execute those tests.
- A file can have vaious blocks.
- The program can be asked for a sumary of one or various numeric columns
- The program can be asked for a count of the registers that a file has on a block
- The library makes convertions between the text and the data that represents in the form of native data types
- The library should be the easiest to use posible (take as a example the csv standard csv python library)
- The format of a file can establish columns with fixed literal values
- The format files are files that can be managed by this own software itself
- The format files have be made according to a format, the formats format


For the future

- The library can manage big volume files: example 9GB, 10GB, avoiding loading all the data to memory at the same time, loading parts of the file on demand as the user moves through the text
- The library can be used to parse text streams that behave like fixed width text files, just intead of files, network data packages.
- The format file can contain the character encoding that uses the file.
- The program supports data on XML format
- The program supports data on json format
- The program can try to guess the format of a file.


Requerimientos para la interface gráfica (teddetui)
===================================================

- Se puede abrir ficheros de texto de ancho fijo y separados por coma.
- Se puede editar los campos de texto del fichero.
- Se puede salvar el fichero modificado.
- Se puede crear un fichero que tiene el formato del fichero de texto.
- El usuario puede mantener un inventario de formatos de ficheros.
- El usuario puede abrir un fichero de texto que contiene datos y seleccionar el formato de ese fichero.
- El programa muestra el contenido de ese fichero de datos en una cuadrícula.
- El programa permite ordenar la tabla del texto por cualquiera de las columnas que posee los datos.
- El programa pone automáticamente de primero una columna con el número de cada registro.
- El programa está implementado en python tk con la versión moderna del GUI.
- El programa usa libteddet para abrir los ficheros y los formatos y para escribir la data y los formatos.
- Cuando se abre un fichero de columnas de ancho fijo se muestra en la parte superior de la tabla una regla en la que se ve el tamaño en caracteres de cada campo alineado con las columnas de la tabla.
- El texto en la tabla usa un tipo de letra mono, de ancho fijo de modo que no se distorcione el ancho del texto.
- Se puede leer un fichero en un formato, por ejemplo CSV y luego exportarlo a otro formato, a un fichero de columnas de ancho-fijo y viceversa.
- Tiene que soportar drag and drop para abrir ficheros que se sueltan dentro de la ventana.
- Al formato se le pueden poner validaciones para el fichero.
- El programa tiene que mostrar una lista con los errores de validación.
- Las validaciones tienen mensajes explicitos entendibles que se pueden usar para endender porque una validación no está pasando.
- Cuando se hace clic en el mensaje de error la grilla enfoca ese elemento que tiene problemas.
- Dentro de la propia tabla se marcan los elementos que infringen alguna validación, si es una sola celda, esa celda, si es toda una colmuna esa columna, si es una fila completa, esa fila.
- Si un elemento está marcado porque tiene un error, fila, columna, celda, cuando se toca ese elemento se muestra un mensaje con la validación que está infringiendo.

Para el futuro:

- El programa puede manejar fichero de gran volúmen, ej: 9GB, 10GB cargando pedazos del fichero en la memoria por partes según vaya siendo necesario.
