### Descripción

### Solución
### Solución 1 - kali
```
──(kali㉿kali)-[~]
└─$ wget -q https://challenge-files.picoctf.net/c_fickle_tempest/c0eec6af0f04316e2bdc4a9f095afd0e2d0121f5e543dbc4a65bb0038d72a993/buildings.png
                                                                             
┌──(kali㉿kali)-[~]
└─$ exiftool buildings.png
ExifTool Version Number         : 13.36
File Name                       : buildings.png
Directory                       : .
File Size                       : 625 kB
File Modification Date/Time     : 2025:11:07 14:37:28-05:00
File Access Date/Time           : 2026:03:09 14:39:19-04:00
File Inode Change Date/Time     : 2026:03:09 14:39:19-04:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 657
Image Height                    : 438
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 657x438
Megapixels                      : 0.288
al no encontrar nada buscamos una herrmienta de estenografia en linea que decodifica la bandera. 

```
### Notas adicionales 
picoCTF{h1d1ng_1n_th3_b1t5}
### Referencias
https://stylesuxx.github.io/steganography/