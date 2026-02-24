### Descripción
Fix the syntax error in this Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/27/fixme1.py)
### Solución
### Solución 1 -  Python
```
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/27/fixme1.py
giselle_maz-picoctf@webshell:~$ python fixme1.py
  File "/home/giselle_maz-picoctf/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent

```
se analiza y elimina los espacios extra, accedemos a la linea 20 con control 7, 20, guardamos y volvemos a ejecutar
```
giselle_maz-picoctf@webshell:~$ nano fixme1.py
giselle_maz-picoctf@webshell:~$ python fixme1.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_182342f7}
```
### Notas adicionales 

### Referencias