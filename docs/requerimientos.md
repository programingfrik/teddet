

- Se puede crear un fichero que tiene el formato del fichero de texto.
- se puede elegir el formato de las columnas, texto, número, etc.
- se pueden crear reglas de validación para esos ficheros.
  - Una columna numérica provoca una alerta si tiene texto.
  - Un fichero de columnas de ancho fijo produce una alerta si uno o más registros tienen más texto del esperado.
  - Un fichero separado por comas produce una alerta si uno o más registros tienen más campos que los esperados, según el formato.
  - Una columna que contiene fechas produce una alerta si algún registro tiene una fecha que no es válida.
  - Una columna de texto puede producir una alerta si tiene un caracter que no puede ser codificado en el formato de texto actual.??
- un fichero puede tener varios bloques
- Se le puede pedir al programa que haga un sumario de una o de varias columnas númericas
- se le puede pedir al programa que cuente los registros que contiene un fichero en un bloque.

Para el futuro

- Se puede poner en el formato la codificación de texto que usa el fichero.
- Soporta data en formato XML
- Soporta data en formato json.
- Que el programa trate de adivinar el formato de un fichero.
