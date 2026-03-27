### Descripción
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?Image: [dolls.jpg](https://challenge-files.picoctf.net/c_wily_courier/0f5ef9c383aa83d319ccb01805f4b9499934bf6a44fdcb5a9f2039de92b6c24a/dolls.jpg)
### Solución
### Solución 1 - Usando CyberChef

### Solución 2 - Python
```
 descragamos y descomprimimos 
 
giselle_maz-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/0f5ef9c383aa83d319ccb01805f4b9499934bf6a44fdcb5a9f2039de92b6c24a/dolls.jpg
--2026-03-18 19:01:08--  https://challenge-files.picoctf.net/c_wily_courier/0f5ef9c383aa83d319ccb01805f4b9499934bf6a44fdcb5a9f2039de92b6c24a/dolls.jpg
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.18, 3.160.5.40, 3.160.5.95, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 651613 (636K) [application/octet-stream]
Saving to: 'dolls.jpg'

dolls.jpg              100%[============================>] 636.34K  1.83MB/s    in 0.3s    

2026-03-18 19:01:09 (1.83 MB/s) - 'dolls.jpg' saved [651613/651613]

giselle_maz-picoctf@webshell:~$ binwalk dolls.jpg  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378933, uncompressed size: 383920, name: base_images/2_c.jpg
651591        0x9F147         End of Zip archive, footer length: 22

giselle_maz-picoctf@webshell:~$ unzip dolls.jpg  
Archive:  dolls.jpg
warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/2_c.jpg 
  
  
repetimos hasta encontrar bandera  
    giselle_maz-picoctf@webshell:~$ cd base_images
giselle_maz-picoctf@webshell:~/base_images$ unzip 2_c.jpg  
Archive:  2_c.jpg
warning [2_c.jpg]:  187707 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/3_c.jpg     
giselle_maz-picoctf@webshell:~/base_images$ unzip 3_c.jpg  
unzip:  cannot find or open 3_c.jpg, 3_c.jpg.zip or 3_c.jpg.ZIP.
giselle_maz-picoctf@webshell:~/base_images$ cd base_images
giselle_maz-picoctf@webshell:~/base_images/base_images$ unzip 3_c.jpg  
Archive:  3_c.jpg
warning [3_c.jpg]:  123606 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/4_c.jpg     
giselle_maz-picoctf@webshell:~/base_images/base_images$ cd base_images
giselle_maz-picoctf@webshell:~/base_images/base_images/base_images$ unzip 4_c.jpg  
Archive:  4_c.jpg
warning [4_c.jpg]:  79578 extra bytes at beginning or within zipfile
  (attempting to process anyway)
 extracting: flag.txt                
giselle_maz-picoctf@webshell:~/base_images/base_images/base_images$ cat flag.txt
picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}
```
### Notas adicionales 
picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}
### Referencias