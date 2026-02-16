### Descripción
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/11/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/11/level1.flag.txt.enc) in the same directory too.
### Solución
### Solución 1 -  Python
```
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/11/level1.py
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/11/level1.flag.txt.enc
giselle_maz-picoctf@webshell:~$ python level1.py
Please enter correct password for flag: 
That password is incorrect
```
al no conocer la contraseña la buscamos en el codigo fuente
```
giselle_maz-picoctf@webshell:~$ nano level1.py
giselle_maz-picoctf@webshell:~$ python level1.py
Please enter correct password for flag: 1e1a
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_fa343060}
```
### Notas adicionales 
picoCTF{545h_r1ng1ng_fa343060}
### Referencias