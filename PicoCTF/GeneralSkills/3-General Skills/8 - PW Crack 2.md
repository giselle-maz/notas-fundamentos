### Descripción
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/14/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/14/level2.flag.txt.enc) in the same directory too.
### Solución
### Solución 1 -  Python
descargar y ejecutar
```
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/14/level2.py
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/14/level2.flag.txt.enc
giselle_maz-picoctf@webshell:~$ python level2.py
Please enter correct password for flag: 
That password is incorrect
```
al no conocer la contraseña la buscamos en el codigo fuente, pero esta encriptada asi que la convertimos 
o sin convertir, en codigo fuente le decimos que nos la muestre
 ```
giselle_maz-picoctf@webshell:~$ nano level2.py
giselle_maz-picoctf@webshell:~$ python level2.py
4ec9
Please enter correct password for flag: 43c9
That password is incorrect
giselle_maz-picoctf@webshell:~$ python level2.py
4ec9
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681}
 ```

### Notas Adicionales
picoCTF{tr45h_51ng1ng_9701e681}
### Referencias