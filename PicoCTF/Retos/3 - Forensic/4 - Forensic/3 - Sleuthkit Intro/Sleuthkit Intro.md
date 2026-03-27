### Descripción
Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.[Download disk image](https://artifacts.picoctf.net/c/164/disk.img.gz)Access checker program: `nc saturn.picoctf.net 51893`
### Solución
### Solución 1 - 
descragamos y descomprimimos
```
giselle_maz-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/164/disk.img.gz
--2026-03-25 18:55:28--  https://artifacts.picoctf.net/c/164/disk.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.18, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 29714372 (28M) [application/octet-stream]
Saving to: 'disk.img.gz'

disk.img.gz    0%       0  --.-KBdisk.img.gz    0% 235.11K  1.02MBdisk.img.gz    2% 800.66K  1.81MBdisk.img.gz    4%   1.16M  1.81MBdisk.img.gz    5%   1.53M  1.81MBdisk.img.gz    6%   1.90M  1.81MBdisk.img.gz    8%   2.28M  1.82MBdisk.img.gz    9%   2.65M  1.82MBdisk.img.gz   10%   3.03M  1.82MBdisk.img.gz   12%   3.40M  1.82MBdisk.img.gz   13%   3.78M  1.82MBdisk.img.gz   14%   4.15M  1.82MBdisk.img.gz   15%   4.53M  1.82MBdisk.img.gz   17%   4.90M  1.82MBdisk.img.gz   18%   5.28M  1.82MBdisk.img.gz   19%   5.65M  1.82MBdisk.img.gz   21%   6.03M  1.85MBdisk.img.gz   22%   6.40M  1.82MBdisk.img.gz   23%   6.78M  1.82MBdisk.img.gz   25%   7.15M  1.82MBdisk.img.gz   26%   7.53M  1.82MBdisk.img.gz   27%   7.90M  1.82MBdisk.img.gz   29%   8.28M  1.82MBdisk.img.gz   30%   8.65M  1.82MBdisk.img.gz   31%   9.03M  1.82MBdisk.img.gz   33%   9.40M  1.82MBdisk.img.gz   34%   9.78M  1.82MBdisk.img.gz   35%  10.15M  1.82MBdisk.img.gz   37%  10.53M  1.82MBdisk.img.gz   38%  10.90M  1.82MBdisk.img.gz   39%  11.28M  1.82MBdisk.img.gz   41%  11.65M  1.82MBdisk.img.gz   42%  12.03M  1.82MBdisk.img.gz   43%  12.40M  1.82MBdisk.img.gz   45%  12.78M  1.82MBdisk.img.gz   46%  13.15M  1.82MBdisk.img.gz   47%  13.53M  1.82MBdisk.img.gz   49%  13.90M  1.82MBdisk.img.gz   50%  14.28M  1.82MBdisk.img.gz   51%  14.65M  1.82MBdisk.img.gz   53%  15.03M  1.82MBdisk.img.gz   54%  15.40M  1.82MBdisk.img.gz   55%  15.78M  1.82MBdisk.img.gz   56%  16.15M  1.82MBdisk.img.gz   58%  16.53M  1.82MBdisk.img.gz   59%  16.90M  1.82MBdisk.img.gz   60%  17.28M  1.82MBdisk.img.gz   62%  17.65M  1.82MBdisk.img.gz   63%  18.03M  1.82MBdisk.img.gz   64%  18.40M  1.82MBdisk.img.gz   66%  18.78M  1.82MBdisk.img.gz   67%  19.15M  1.82MBdisk.img.gz   68%  19.53M  1.82MBdisk.img.gz   70%  19.90M  1.82MBdisk.img.gz   71%  20.28M  1.82MBdisk.img.gz   72%  20.65M  1.82MBdisk.img.gz   74%  21.03M  1.82MBdisk.img.gz   75%  21.40M  1.82MBdisk.img.gz   76%  21.78M  1.82MBdisk.img.gz   78%  22.15M  1.82MBdisk.img.gz   79%  22.53M  1.82MBdisk.img.gz   80%  22.90M  1.82MBdisk.img.gz   82%  23.28M  1.82MBdisk.img.gz   83%  23.63M  1.82MBdisk.img.gz   84%  24.01M  1.82MBdisk.img.gz   86%  24.38M  1.82MBdisk.img.gz   87%  24.76M  1.82MBdisk.img.gz   88%  25.13M  1.82MBdisk.img.gz   90%  25.51M  1.82MBdisk.img.gz   91%  25.88M  1.82MBdisk.img.gz   92%  26.26M  1.82MBdisk.img.gz   93%  26.63M  1.82MBdisk.img.gz   95%  27.01M  1.82MBdisk.img.gz   96%  27.38M  1.82MBdisk.img.gz   97%  27.76M  1.82MBdisk.img.gz   99%  28.13M  1.82MBdisk.img.gz  100%  28.34M  1.82MB/s    in 16s     

2026-03-25 18:55:43 (1.82 MB/s) - 'disk.img.gz' saved [29714372/29714372]

giselle_maz-picoctf@webshell:/tmp$ gunzip disk.img.gz 
``` 
 vemos el tamaño de particion y guardamos el numero
```            
giselle_maz-picoctf@webshell:/tmp$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```
nos conectamos al reto e ingresamos el tamano guardado 202752 y nos da la flag:
```
giselle_maz-picoctf@webshell:/tmp$ nc saturn.picoctf.net 51893
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
202752
Great work!
picoCTF{mm15_f7w!}
```
### Notas adicionales 
picoCTF{mm15_f7w!}
### Referencias
