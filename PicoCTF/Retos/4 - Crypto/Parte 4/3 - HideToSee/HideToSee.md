### Descripción
How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/235/atbash.jpg).
### Solución
```
descargamos y vemos la imagen, pero no nos dice mucho asi que extraemos el mensaje oculto

steghide extract -sf atbash.jpg
y luego lo decodificamos

giselle_maz-picoctf@webshell:~$ cat encrypted.txt | tr 'a-zA-Z' 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
picoCTF{atbash_crack_92533667}
```
### Notas adicionales 
picoCTF{atbash_crack_92533667}
### Referencias
