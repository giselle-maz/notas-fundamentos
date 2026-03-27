### Descripcion
We found this file. Recover the flag.[tunn3l_v1s10n](https://challenge-files.picoctf.net/c_wily_courier/626df9feed926c1e1280804f5d87fde5576e266ff250a819a5528b0471b0f3f7/tunn3l_v1s10n)
### Solución
### Solución 1 - Usando CyberChef

### Solución 2 - Python
```
descragamos, vemos el tipo de archivo y los metadatos, al estar corrompido lo editamos usando hexeditor, corrigiendo la altura y encabezado y guardamos 
┌──(kali㉿kali)-[~/ppt/slideMasters]
└─$ wget https://challenge-files.picoctf.net/c_wily_courier/626df9feed926c1e1280804f5d87fde5576e266ff250a819a5528b0471b0f3f7/tunn3l_v1s10n        
--2026-03-18 15:30:21--  https://challenge-files.picoctf.net/c_wily_courier/626df9feed926c1e1280804f5d87fde5576e266ff250a819a5528b0471b0f3f7/tunn3l_v1s10n
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 18.160.124.52, 18.160.124.49, 18.160.124.59, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|18.160.124.52|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2893454 (2.8M) [application/octet-stream]
Saving to: ‘tunn3l_v1s10n’

tunn3l_v1s10n           100%[==============================>]   2.76M  3.07MB/s    in 0.9s    

2026-03-18 15:30:22 (3.07 MB/s) - ‘tunn3l_v1s10n’ saved [2893454/2893454]

                                                                                               
┌──(kali㉿kali)-[~/ppt/slideMasters]
└─$ file tunn3l_v1s10n
tunn3l_v1s10n: data
                                                                                               
┌──(kali㉿kali)-[~/ppt/slideMasters]
└─$ exiftool unn3l_v1s10n
Error: File not found - unn3l_v1s10n
                                                                                               
┌──(kali㉿kali)-[~/ppt/slideMasters]
└─$ exiftool tunn3l_v1s10n
ExifTool Version Number         : 13.36
File Name                       : tunn3l_v1s10n
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2025:12:19 13:46:08-05:00
File Access Date/Time           : 2026:03:18 15:30:37-04:00
File Inode Change Date/Time     : 2026:03:18 15:30:22-04:00
File Permissions                : -rw-rw-r--
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Unknown (53434)
Image Width                     : 1134
Image Height                    : 306
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 2893400
Pixels Per Meter X              : 5669
Pixels Per Meter Y              : 5669
Num Colors                      : Use BitDepth
Num Important Colors            : All
Red Mask                        : 0x27171a23
Green Mask                      : 0x20291b1e
Blue Mask                       : 0x1e212a1d
Alpha Mask                      : 0x311a1d26
Color Space                     : Unknown (,5%()
Rendering Intent                : Unknown (826103054)
Image Size                      : 1134x306
Megapixels                      : 0.347
                                                                                               
┌──(kali㉿kali)-[~/ppt/slideMasters]
└─$ hexeditor tunn3l_v1s10n

las filas corregidas deben quedar asi 00000000  42 4D 8E 26 2C 00 00 00  00 00 36 00 00 00 28 00
00000010  00 00 28 00 00 00 6E 04  00 00 6E 04 00 00 01 00 (ayuda de gemini)

y al abrir la imagen es posible ver la flag

```
### Notas adicionales 
picoCTF{qu1t3_a_v13w_2020}
### Referencias