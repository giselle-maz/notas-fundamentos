### Descripción
Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/136/disk.flag.img.gz)
### Solución
### Solución 1 - 
descargamos y descomprimimos
```

giselle_maz-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/136/disk.flag.img.gz
--2026-03-25 19:05:53--  https://artifacts.picoctf.net/c/136/disk.flag.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.77, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 47534571 (45M) [application/octet-stream]
Saving to: 'disk.flag.img.gz'

disk.flag.img.gz     100%[====================>]  45.33M  1.82MB/s    in 25s     

2026-03-25 19:06:18 (1.82 MB/s) - 'disk.flag.img.gz' saved [47534571/47534571]

giselle_maz-picoctf@webshell:/tmp$ gunzip disk.flag.img.gz
```
analizamos tabla de peticiones y extraemos el historial de comandos
```
mmls disk.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)


giselle_maz-picoctf@webshell:/tmp$ fls -o 2048 disk.flag.img
d/d 11: lost+found
r/r 12: ldlinux.sys
r/r 13: ldlinux.c32
r/r 15: config-virt
r/r 16: vmlinuz-virt
r/r 17: initramfs-virt
l/l 18: boot
r/r 20: libutil.c32
r/r 19: extlinux.conf
r/r 21: libcom32.c32
r/r 22: mboot.c32
r/r 23: menu.c32
r/r 14: System.map-virt
r/r 24: vesamenu.c32
V/V 25585:      $OrphanFiles
```
lo que nos dice que la bandera se guardó en `/root/my_folder/flag.uni.txt` tras ser convertida a UTF-16.
entonces vemos la lista el contenido del directorio /root
```
fls -o 360448 disk.flag.img 1995
r/r 2363:       .ash_history
d/d 3981:       my_folder
```

vemos el contenido de my_folder
```
giselle_maz-picoctf@webshell:/tmp$ fls -o 360448 disk.flag.img 3981
r/r * 2082(realloc):    flag.txt
r/r 2371:       flag.uni.txt
```
y vemos el **contenido en hexadecimal** del archivo de la bandera, y nos la muestra:
```

giselle_maz-picoctf@webshell:/tmp$ icat -o 360448 disk.flag.img 2371 | xxd
00000000: 0070 0069 0063 006f 0043 0054 0046 007b  .p.i.c.o.C.T.F.{
00000010: 0062 0079 0037 0033 005f 0035 0075 0072  .b.y.7.3._.5.u.r
00000020: 0066 0033 0072 005f 0033 0034 0039 0037  .f.3.r._.3.4.9.7
00000030: 0061 0065 0036 0062 007d 000a            .a.e.6.b.}..
```
### Notas adicionales 
picoCTF{by73_5urf3r_3497ae6b}
### Referencias
