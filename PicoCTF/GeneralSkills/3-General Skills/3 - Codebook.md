### Descripción

### Solución
### Solución 1 - Usando CyberChef

### Solución 2 - Python
descragar archivos con wget
```
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/1/code.py
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/1/codebook.txt
```
ls para saber que los archivos estan en el directorio donde estoy yo.
```
giselle_maz-picoctf@webshell:~$ ls
Addadshashanammu      README.txt  codebook.txt  files.zip  runme.py.1
Addadshashanammu.zip  code.py     files         runme.py
```
ejecutar
```
giselle_maz-picoctf@webshell:~$ python code.py
picoCTF{c0d3b00k_455157_d9aa2df2}
```
### Notas adicionales 
picoCTF{c0d3b00k_455157_d9aa2df2}
### Referencias