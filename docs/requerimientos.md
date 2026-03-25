Requerimientos
==============

Estos requerimientos son la lista de funcionalidades que se espera que tenga la solución que surja de este proyecto.


Requerimientos para la librería (libteddet)
===========================================

- Se puede crear un fichero que tiene el formato del fichero de texto.
- Se puede elegir el formato de las columnas:
  - Columnas de texto
  - Columnas de números enteros
  - Columnas de números decimales con precisión arbitrária elegida por el usuario.
  - Columnas de fecha y hora.
  - Columnas con solo fecha.
  - Columnas con solo hora.
- se pueden crear reglas de validación para esos ficheros.
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

- El usuario puede mantener un inventario de formatos de ficheros
- El usuario puede abrir un fichero de texto que contiene datos y seleccionar el formato de ese fichero.
- El programa muestra el contenido de ese fichero de datos en una cuadrícula.
- El programa permite ordenar la tabla del texto por cualquiera de las columnas que posee los datos.
- El programa pone automáticamente de primero una columna con el número de cada registro.
- El programa está implementado en python tk con la versión moderna del GUI
- El programa usa libteddet para abrir los ficheros y los formatos y para escribir la data y los formatos.
- Cuando se abre un fichero de columnas de ancho fijo se muestra en la parte superior de la tabla una regla en la que se ve el tamaño en caracteles de cada campo alineado con las columnas de la tabla.
- El texto en la tabla usa un tipo de letra mono, de ancho fijo de modo que no se distorcione el ancho del texto.
- Se puede leer un fichero en un formato, por ejemplo CSV y luego exportarlo a otro formato, a un fichero de columnas de ancho-fijo y viceversa.
