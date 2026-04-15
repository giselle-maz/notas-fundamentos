### Descripción
Can you get the real meaning from this file.Download the file [here](https://artifacts.picoctf.net/c_titan/2/enc_flag).
### Solución
```
sabemos que el contenido esta codificado base 64 4ntonces:

giselle_maz-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/2/enc_flag
--2026-04-14 04:54:52--  https://artifacts.picoctf.net/c_titan/2/enc_flag
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.72, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 73 [application/octet-stream]
Saving to: 'enc_flag'

enc_flag               100%[============================>]      73  --.-KB/s    in 0s      

2026-04-14 04:54:52 (32.5 MB/s) - 'enc_flag' saved [73/73]

giselle_maz-picoctf@webshell:~$ cat enc_flag | base64 -d
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzc4MjUwaG1qfQ=='
giselle_maz-picoctf@webshell:~$ echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzc4MjUwaG1qfQ=="| base64 -d
wpjvJAM{jhlzhy_k3jy9wa3k_78250hmj}giselle_maz-picoctf@webshell:~$ echo "wpjvJAM{jhlzhy_k3jy9A-St-za-s'hmj}" | tr 'A-Za-z' 'T-ZA
picoCTF{caesar_d3cr9pt3d_78250afc}


a medio camino reconovemos el formato de la flag pero con las letras recorridas, solucionamos y listo

picoCTF{caesar_d3cr9pt3d_78250afc}
```
### Notas adicionales 
picoCTF{caesar_d3cr9pt3d_78250afc}
### Referencias
