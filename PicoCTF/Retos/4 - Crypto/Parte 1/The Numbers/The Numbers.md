### Descripción
The numbers... what do they mean?[numbers.png](https://challenge-files.picoctf.net/c_fickle_tempest/7b39deba4212c233b1628c93f16639ed02ad90f51436d2a8914bb11f74a982d3/the_numbers.png)
### Solución
```
primero almacenamos los numeros dentro de la imagen, luego los traducimos del codigo ASCII y listo, formamos la flag

giselle_maz-picoctf@webshell:~$ NUMEROS="20 8 5 14 21 13 2 5 18 19 13 1 19 15 14"
giselle_maz-picoctf@webshell:~$ python3 -c "numbers=[20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]; print(''.join([chr(n + 64) for n in numbers]))"
THENUMBERSMASON
```
### Notas adicionales 
picoCTF{THENUMBERSMASON}
### Referencias
