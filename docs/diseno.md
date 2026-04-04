teddet
======

texto es data, data es texto.

Este proyecto son 2 cosas: 
 - Una librería para extraer data de ficheros de texto, csv, columnas de anchofijo, otros? y para poner data en forma de esos formatos de texto, esta librería consturida sobre Haxe de forma que esté disponible para diferentes lenguajes y plataformas, inicialmente, python y csharp
 - También es una interface gráfica hecha en python que permita abrir, leer, manipular y crear formatos de ficheros de texto y abrir, leer, manipular y crear ficheros de texto con data, en esos formatos.

La librería está hecha en Haxe. Inicialmente se trans-compila a python y a csharp.

La interface gráfica de usuario está hecha en python usando tk inter.

Estoy usando como ejemplo de como debería ser implementada una librería como esta la librería estandar de python para manejar csv [https://docs.python.org/3/library/csv.html].




Reader
------

Un objeto que se va a encargar de leer del fichero en cuestión.

Una vez creado el fichero se puede iterar por el.

Writer
------

Un objeto que se va a encargar de escribir el fichero en cuestión.

Una vez creado el objeto, solo hay que ir pasandole los valores que van a formar un registro.
