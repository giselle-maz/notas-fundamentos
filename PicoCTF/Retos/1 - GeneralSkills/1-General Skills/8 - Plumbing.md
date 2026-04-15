### Descripción
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag?Connect to fickle-tempest.picoctf.net 54383.
### Solución
### Solución 1 - Consola
```
giselle_maz-picoctf@webshell:~$ nc fickle-tempest.picoctf.net 54383 |grep pico
picoCTF{digital_plumb3r_d3246b6B}
```
### Solución 2 - Consola (redirigir salida)
```
giselle_maz-picoctf@webshell:~$ nc fickle-tempest.picoctf.net 54383 > salida  
^C
giselle_maz-picoctf@webshell:~$ cat salida |grep pico
picoCTF{digital_plumb3r_d3246b6B}
```
### Notas adicionales 
picoCTF{digital_plumb3r_d3246b6B}

- |, pipe, redirige la salida de un comando a la entrada de otro
- >, redirige la salida de un comando a un archivo de txt
### Referencias