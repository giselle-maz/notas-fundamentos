
### DESCRIPCIÓN

Can you conjure the right bytes? The program's source code can be downloaded here. `nc candy-mountain.picoctf.net 54596`
### SOLUCIÓN

El reto requiere enviar una cadena específica de bytes que satisfaga una condición de igualdad en el servidor. El programa solicita el valor ASCII Decimal 101 repetido tres veces.
#### 1. Traducción de Bytes:
Analizando la tabla ASCII, el valor decimal 101 corresponde al carácter minúsculo e. En el código fuente, esto se confirma con la comparación hexadecimal \x65, que es el equivalente de 101 en base 16.

`101 (Dec) = 0x65 (Hex) = 'e' (ASCII)`
#### 2. Construcción del Input:
El programa espera "101, 101, 101, uno al lado del otro, sin espacios". Esto se traduce simplemente a la cadena de texto eee.

#### 3. Ejecución:
Utilizamos un pipe para enviar la cadena directamente al servicio remoto:

```
echo "eee" | nc candy-mountain.picoctf.net 54596
```

Al recibir la entrada correcta, el programa ejecuta la instrucción open("./flag.txt", "r").read(), imprimiendo la bandera en la terminal.
### NOTAS ADICIONALES


### REFERENCIAS