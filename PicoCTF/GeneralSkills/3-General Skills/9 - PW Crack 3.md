### Descripción

### Solución
### Solución 1 -  Python
descargamos y ejecutamos
```
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/17/level3.py
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/17/level3.flag.txt.enc
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/17/level3.hash.bin
giselle_maz-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: 
That password is incorrect
giselle_maz-picoctf@webshell:~$ nano level3.py
```
no conocemos la contraseña, inspeccionamos y probamos las posibles contraseñas 
```
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

giselle_maz-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: f159
That password is incorrect
giselle_maz-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: f09e
That password is incorrect
giselle_maz-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: 4dcf
That password is incorrect
giselle_maz-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: 87ab
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
```

### Notas adicionales 
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
### Referencias