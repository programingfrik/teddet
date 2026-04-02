Requerimientos
==============

Estos requerimientos son la lista de funcionalidades que se espera que tenga la solución que surja de este proyecto.

La idea es que los requerimientos vayan de lo más básico, de la funcionalidad más necesaria a las funcionalidades de uso menos frecuente.

El orden de las cosas para hacer un cambio es primero conciliar los nuevos requerimientos con los requerimientos previos en este documento, luego hacer cambios al diseño y luego hacer cambios a los fuentes.

Este proyecto consiste en 2 subpartes. El núcleo la prate base una librería que sirva para manejar ficheros de texto tanto de columna de ancho fijo como ficheros separados por comas, a través de formatos predefinidos. La segunda parte una interfaz gráfica para elaborar formatos y también para trabajar con ficheros en base a esos formatos. Trabajar es crearlos y editarlos pero también convertirlos a otros formatos.

Requerimientos para la librería (libteddet)
===========================================

Esta es la parte de la librería que es el núcleo del proyecto. Este núcleo va

- La librería tiene que ser escrita en HAXE
- Apartir de la versión de HAXE tienen que construirse otras versiones
  - Versión para python
  - Versión para csharp
- La librería puede abrir ficheros a partir de un formato.
- Pueden ser ficheros de texto de columnas de ancho fijo.
- Pueden ser fichero de texto separados por coma
- Se puede elegir el formato de las columnas:
  - Columnas de texto
  - Columnas de números enteros
  - Columnas de números decimales con precisión arbitrária elegida por el usuario.
  - Columnas de fecha y hora.
  - Columnas con solo fecha.
  - Columnas con solo hora.
- Se pueden crear reglas de validación para esos ficheros.
  - Validar que una columna solo debe contener digitos decimales.
  - Validar que una columna debe contener un número decimal válido.
  - Validar que los registros de un fichero de ancho fijo tengan la cantidad de texto esperado y no más y no menos.
  - Validar que un fichero separado por comas tenga la cantidad de columnas que se esperan, o sea la cantidad de separadores correctos.
  - Validar que una columna contenga en todos los registros fechas válidas
  - Validar que una columna de texto todos los caracteres se puedan codificar en la codificación de texto actual.
  - Una validación que establezca que una columna no puede estar en blanco.
  - Una validación que establezca una lista blanca de valores que puede tener una columna.
  - Una validación que establezca una lista negra de valores que no puede contener una columna.
  - Una validación que establezca que en una columna todos los registros deben coincidir con una expresión regular.
- La librería tiene que ir acompañada de un banco de pruebas y de un programita para ejecutar esas pruebas.
- un fichero puede tener varios bloques
- Se le puede pedir al programa que haga un sumario de una o de varias columnas númericas
- se le puede pedir al programa que cuente los registros que contiene un fichero en un bloque.
- Una versión de la librería disponible para python.
- Una versión de la librería disponible para csharp.
- La librería hace conversión entre el texto y la data que representa en forma de tiupos de datos nativos.
- La librería debería ser lo más fácil de usar que sea posible (tomar como ejemplo la librería csv de python).

Para el futuro

- Se puede poner en el formato la codificación de texto que usa el fichero.
- Soporta data en formato XML
- Soporta data en formato json.
- Que el programa trate de adivinar el formato de un fichero.


Requerimientos para la interface gráfica (teddetui)
===================================================

- Se puede crear un fichero que tiene el formato del fichero de texto.
- El usuario puede mantener un inventario de formatos de ficheros
- El usuario puede abrir un fichero de texto que contiene datos y seleccionar el formato de ese fichero.
- El programa muestra el contenido de ese fichero de datos en una cuadrícula.
- El programa permite ordenar la tabla del texto por cualquiera de las columnas que posee los datos.
- El programa pone automáticamente de primero una columna con el número de cada registro.
- El programa está implementado en python tk con la versión moderna del GUI
- El programa usa libteddet para abrir los ficheros y los formatos y para escribir la data y los formatos.
- Cuando se abre un fichero de columnas de ancho fijo se muestra en la parte superior de la tabla una regla en la que se ve el tamaño en caracteres de cada campo alineado con las columnas de la tabla.
- El texto en la tabla usa un tipo de letra mono, de ancho fijo de modo que no se distorcione el ancho del texto.
- Se puede leer un fichero en un formato, por ejemplo CSV y luego exportarlo a otro formato, a un fichero de columnas de ancho-fijo y viceversa.
