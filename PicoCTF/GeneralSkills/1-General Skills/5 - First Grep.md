### Descripción
Can you find the flag in the file? This would be really tedious to look through manually, something tells me there is a better way.The flag is in this [file](https://challenge-files.picoctf.net/c_fickle_tempest/9e4f9113960f157ceb824bdb449dc2a74504b484346c1442e64854408d5a90c5/file).
### Solución
### Solución 1 - Manualmente
![[Pasted image 20260209123755.png]]
### Solución 2 - Consola
```
giselle_maz-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_fickle_tempest/9e4f9113960f157ceb824bdb449dc2a74504b484346c1442e64854408d5a90c5/file 

giselle_maz-picoctf@webshell:~$ grep "pico" file
```
### Notas adicionales 
picoCTF{grep_is_good_to_find_things_9C6Ef2F7}

primero descargar archivo con wget, luego busacr con grep palabra clave y luego el nombre del archivo descargado
### Referencias