### Descripción
Fix the syntax error in the Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/6/fixme2.py)
### Solución
### Solución 1 -  Python
```
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/6/fixme2.py
giselle_maz-picoctf@webshell:~$ python fixme2.py
  File "/home/giselle_maz-picoctf/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
giselle_maz-picoctf@webshell:~$ nano fixme2.py
giselle_maz-picoctf@webshell:~$ python fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}
```
### Notas adicionales 
picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}

error en linea 22, faltaba un '='
### Referencias