### Descripción
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image.[dds1-alpine.flag.img.gz](https://challenge-files.picoctf.net/c_wily_courier/89797cb52348a4096884e4f58164b42a892f8cac34b91d887491f44a5f144718/dds1-alpine.flag.img.gz)
### Solución
### Solución 1 - consola
```
descargamos el archivo
giselle_maz-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/89797cb52348a4096884e4f58164b42a892f8cac34b91d887491f44a5f144718/dds1-alpine.flag.img.gz
--2026-03-25 18:48:40--  https://challenge-files.picoctf.net/c_wily_courier/89797cb52348a4096884e4f58164b42a892f8cac34b91d887491f44a5f144718/dds1-alpine.flag.img.gz
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.95, 3.160.5.18, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 29768911 (28M) [application/octet-stream]
Saving to: 'dds1-alpine.flag.img.gz'

dds1-alpine.flag 100%[=========>]  28.39M  1.82MB/s    in 16s     

2026-03-25 18:48:55 (1.82 MB/s) - 'dds1-alpine.flag.img.gz' saved [29768911/29768911]

giselle_maz-picoctf@webshell:~$

intentamos descomprimirlo pero no hay espacio

giselle_maz-picoctf@webshell:~$ gunzip dds1-alpine.flag.img.gz

gzip: dds1-alpine.flag.img: No space left on device

usamos una alternativa sin descomprimir
leemos el archivo sin guardarloy analizamos el flujo.
giselle_maz-picoctf@webshell:~$ zcat dds1-alpine.flag.img.gz | strings | grep "picoCTF{"
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
```
### Notas adicionales 
picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
### Referencias
