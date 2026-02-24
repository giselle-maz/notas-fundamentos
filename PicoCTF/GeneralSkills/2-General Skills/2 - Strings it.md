### Descripción
Can you find the flag in [file](https://challenge-files.picoctf.net/c_fickle_tempest/6577d3f1500aebcd300787bd5d96216b30aed379c811f5e83e888f897da4a3d5/strings) without running it?
### Solución
### Solución 1 - Consola
```
wget https://challenge-files.picoctf.net/c_fickle_tempest/6577d3f1500aebcd300787bd5d96216b30aed379c811f5e83e888f897da4a3d5/strings

chmod +x strings
.\strings

giselle_maz-picoctf@webshell:~$ strings strings | grep pico
picoCTF{5tRIng5_1T_d6306c19}
```
### Notas adicionales 
picoCTF{5tRIng5_1T_d6306c19}
### Referencias