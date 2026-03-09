### Descripción
Find the flag in this [picture](https://challenge-files.picoctf.net/c_fickle_tempest/8e74516a5167183bf254f082a836fe7b925c25d6899feeffb68f78b1549a1224/pico_img.png).
### Solución
### Solución 1 - kali
```
metadatos

┌──(kali㉿kali)-[~]
└─$ exiftool pico_img.png
ExifTool Version Number         : 13.36
File Name                       : pico_img.png
Directory                       : .
File Size                       : 109 kB
File Modification Date/Time     : 2025:11:21 14:10:56-05:00
File Access Date/Time           : 2026:03:09 14:28:24-04:00
File Inode Change Date/Time     : 2026:03:09 14:28:24-04:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Artist                          : picoCTF{s0_m3ta_9a8b5aa1}
Image Size                      : 600x600
Megapixels                      : 0.360


o con un filtro de metadatos

exiftool pico_img.png -Artist
Artist                          : picoCTF{s0_m3ta_9a8b5aa1}

```
### Notas adicionales 
picoCTF{s0_m3ta_9a8b5aa1}

agregar o editar metadatos
exiftool -nombre="valor" a_quien'

```
┌──(kali㉿kali)-[~]
└─$ exiftool -Comment="te hackie" pico_img.png
    1 image files updated
                                                                                                
┌──(kali㉿kali)-[~]
└─$ exiftool pico_img.png -Comment            
Comment                         : te hackie

```

### Referencias