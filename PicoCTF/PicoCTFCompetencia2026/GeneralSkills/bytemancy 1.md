
### DESCRIPCIÓN

Can you conjure the right bytes? The program's source code can be downloaded here. `nc foggy-cliff.picoctf.net 56355`
### SOLUCIÓN

En este reto, el servidor incrementa la complejidad al requerir una cantidad masiva de bytes específicos, lo que hace inviable la entrada manual y obliga al uso de automatización por scripting.
#### 1. Análisis de la condición:
El código fuente indica que la entrada del usuario (`user_input`) debe ser exactamente igual a `"\x65" * 1751`.

`\x65` sigue siendo el valor hexadecimal para el decimal 101 (la letra 'e').

El operador `*` en Python para strings realiza una repetición.

#### 2. Construcción del Payload Automatizado:
Para generar exactamente 1751 repeticiones de la letra 'e' sin errores, utilizamos un comando de Python en línea. La salida de este comando se conecta directamente a la entrada del servidor mediante un pipe (|).
#### 3. Ejecución:
Ejecutamos el siguiente comando en la terminal:

```
python3 -c "print('e' * 1751)" | nc foggy-cliff.picoctf.net 56355
```

El servidor valida la longitud y el contenido de la cadena, liberando la bandera almacenada en flag.txt.
### NOTAS ADICIONALES


### REFERENCIAS