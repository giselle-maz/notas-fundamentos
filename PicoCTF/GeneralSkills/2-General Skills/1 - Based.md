### Descripción
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337?Connect with nc fickle-tempest.picoctf.net 58084.
### Solución
### Solución 1 - Usando Consola + CyberChef

Ingresamos con el comando que nos da el reto, y este mismo me devolvera la primera conversion de binario a string, lo ingresamos:
```
giselle_maz-picoctf@webshell:~$ nc fickle-tempest.picoctf.net 58084
Let us see how data is stored
lime
Please give the 01101100 01101001 01101101 01100101 as a word.
...
you have 45 seconds.....

Input:
lime
```

El siguiente número identificado como octal se mete a Cyber Chef y se convierte a string, se ingresa:
```
Please give me the  o164 o141 o142 o154 o145 as a word.
Input:
table
```
https://gchq.github.io/CyberChef/#recipe=From_Octal('Space')&input=MTY0IDE0MSAxNDIgMTU0IDE0NQ&oeol=FF

De la misma manera, el nuevo numero hexa se pasa a string y se ingresa para obtener la bandera:
```
Please give me the 616e696d6174696f6e as a word.
Input:
animation
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_acdCcfCa}
```
https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NjE2ZTY5NmQ2MTc0Njk2ZjZl

### Notas adicionales 
se deben tener abiertas varias ventanas de cyber Chef para lograrlo o se acaba el tiempo.

picoCTF{learning_about_converting_values_acdCcfCa}

### Referencias