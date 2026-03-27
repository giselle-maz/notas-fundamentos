### Descripción
Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/213/disk.flag.img.gz)
### Solución
### Solución 1 - 
descargamos y descomprimimos

vemos tabla de particiones y vemos los archivos dentro de la partición de offset
```
fls -r -o 411648 disk.flag.img | grep -E "flag|history"
    
+ r/r 1875: .ash_history
+ r/r 1782: flag.txt.enc
```

recuperamos contrasena
```

icat -o 411648 disk.flag.img 1875

```

desencriptamos
```
giselle_maz-picoctf@webshell:/tmp$ icat -o 411648 disk.flag.img 1782 > flag.txt.enc

giselle_maz-picoctf@webshell:/tmp$ openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567 -pbkdf2
```

bandera
```

giselle_maz-picoctf@webshell:/tmp$ cat flag.txt
picoCTF{h4un71ng_p457_5113beab}
```
### Notas adicionales 
picoCTF{h4un71ng_p457_5113beab}
### Referencias
