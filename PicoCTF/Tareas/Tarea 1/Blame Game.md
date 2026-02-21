### Descripción

### Solución
Someone's commits seems to be preventing the program from working. Who is it?You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/159/challenge.zip)
### Solución 1 - Python
```
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c_titan/159/challenge.zip

giselle_maz-picoctf@webshell:~$ cd drop-in
giselle_maz-picoctf@webshell:~/drop-in$ ls
message.py
```

necesitaremos filtrar 
```
git log -- message.py
```

y encontramos la llave 
```
commit 23e9d4ce78b3cea725992a0ce6f5eea0bf0bcdd4
Author: picoCTF{@sk_th3_1nt3rn_81e716ff} <ops@picoctf.com>
Date:   Tue Mar 12 00:07:15 2024 +0000

    optimize file size of prod code

commit 3ce5c692e2f9682a866c59ac1aeae38d35d19771
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:15 2024 +0000

    create top secret project
```
### Notas adicionales 
picoCTF{@sk_th3_1nt3rn_81e716ff}
### Referencias