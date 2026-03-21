
### DESCRIPCIÓN

Can you conjure the right bytes? The program's source code can be downloaded here. `nc lonely-island.picoctf.net 63785`
### SOLUCIÓN

Este reto introduce la manipulación de bytes crudos (raw bytes) que se encuentran fuera del rango de caracteres imprimibles de la tabla ASCII estándar.
#### 1. Análisis del mecanismo de entrada:
A diferencia de los niveles 0 y 1, este programa utiliza sys.stdin.buffer.readline(). El uso de .buffer indica que el programa no está leyendo "texto", sino flujos de datos binarios. La condición para obtener la bandera es que la entrada sea exactamente b"\xff\xff\xff".
#### 2. byte 0xFF:
El valor hexadecimal 0xFF representa el número binario 11111111. En muchos sistemas, este valor no se puede introducir simplemente mediante el teclado, ya que no corresponde a una letra o símbolo visual.
#### 3. Inyección de Bytes con Python:
Para resolverlo, construimos un payload que hable el mismo lenguaje binario que el servidor. Usamos sys.stdout.buffer.write para evitar que Python intente convertir los bytes a una cadena de texto (string) codificada, lo cual corrompería el valor antes de enviarlo.

```
python3 -c "import sys; sys.stdout.buffer.write(b'\xff\xff\xff\n')" | nc lonely-island.picoctf.net 63785
```

Nota: Se añade \n al final porque el servidor espera una línea completa mediante readline().
### NOTAS ADICIONALES

**Bytes vs Strings:** En la programación moderna (especialmente en Python 3), existe una distinción estricta entre **Strings** (secuencias de caracteres Unicode) y **Bytes** (secuencias de números de 8 bits). En ciberseguridad, casi siempre trabajamos con la capa de **Bytes**, ya que nos permite manipular la memoria del sistema de forma exacta, enviando valores que los protocolos de texto normales filtrarían o transformarían erróneamente.
### REFERENCIAS

- [Python Binary I/O](https://docs.python.org/3/library/io.html)
