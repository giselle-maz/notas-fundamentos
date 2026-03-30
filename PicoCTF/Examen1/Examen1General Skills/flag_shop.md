### [flag_shop](https://play.picoctf.org/practice/challenge/49)

### DESCRIPCIÓN

There's a flag shop selling stuff, can you buy a flag?[Source](https://challenge-files.picoctf.net/c_fickle_tempest/3b8dcb92959510cff4c72e182cec42febd0b32bd1911c385e3a4a74a03181e9d/store.c). Connect with nc fickle-tempest.picoctf.net 60444.
### SOLUCIÓN

El objetivo de este reto es comprar la "1337 Flag" (la bandera real) que cuesta $100,000, pero empezamos con un balance inicial muy bajo (generalmente $1,100). Identificamos que el programa en C es vulnerable a un **Integer Overflow** (Desbordamiento de Entero) al calcular el costo total de las banderas.

- Nos conectamos al servidor del reto usando netcat desde nuestra terminal en Kali Linux:

```
nc fickle-tempest.picoctf.net 52230
```

- Entramos al menú de compra de banderas (opción `2`) y seleccionamos la bandera barata o falsa ("Definitely not the flag Flag", opción `1`), que cuesta $900.

- El sistema nos pregunta cuántas banderas queremos comprar. Ingresamos un número enorme, como `3000000` (tres millones).

```
These knockoff Flags cost 900 each, enter desired quantity
3000000
```

- **El Explotación:** Al multiplicar 3,000,000 por 900, el resultado es 2,700,000,000. Este número supera el límite máximo de un entero con signo de 32 bits (2,147,483,647). Debido al sistema de "complemento a dos" (Two's complement), el número "da la vuelta" y se convierte en un valor negativo.

- El programa calcula nuestro nuevo balance restando el costo total. Como el costo ahora es negativo, la matemática hace lo siguiente: `Balance = Balance - (-Costo)`. Restar un número negativo equivale a una suma. ¡El sistema termina inyectando millones de dólares a nuestra cuenta!

- Con nuestro nuevo balance multimillonario, volvemos al menú de compra (opción `2`), seleccionamos la bandera real ("1337 Flag", opción `2`) y compramos `1`.

- El servidor verifica que tenemos fondos más que suficientes, procesa la compra y nos imprime la bandera en pantalla:
   
   picoCTF{m0n3y_bag5_F2Eb382F}
### NOTAS ADICIONALES

- **¿Qué es el Integer Overflow y el Complemento a Dos?** En lenguajes de bajo nivel como C, la memoria asignada para un número es fija (por ejemplo, 32 bits). El primer bit de la izquierda se usa para indicar el signo (0 para positivo, 1 para negativo). Si realizas una operación matemática que da como resultado un número más grande del que cabe en los 31 bits restantes, el valor invade el bit del signo, cambiándolo a 1. De repente, tu número gigante y positivo es interpretado por la computadora como un número negativo.

- **Mitigación:** Para prevenir esto, los desarrolladores deben usar variables de mayor capacidad (como enteros de 64 bits o `long long` en C) para operaciones financieras, o implementar validaciones que comprueben si el resultado de una multiplicación es menor que los operandos antes de realizar la resta.
### REFERENCIAS

[CWE-190: Integer Overflow or Wraparound](https://cwe.mitre.org/data/definitions/190.html) 

