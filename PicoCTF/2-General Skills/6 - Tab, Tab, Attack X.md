### Descripción
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames.[Addadshashanammu.zip](https://challenge-files.picoctf.net/c_wily_courier/56f53a4189949d066fe969e998769a4e0390123be59782c06e6c0a52c78403e2/Addadshashanammu.zip)
### Solución
### Solución 1 - Consola
descargamos el archivo y lo descomprimimos:
```
giselle_maz-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/56f53a4189949d066fe969e998769a4e0390123be59782c06e6c0a52c78403e2/Addadshashanammu.zip
--2026-02-11 20:02:30--  https://challenge-files.picoctf.net/c_wily_courier/56f53a4189949d066fe969e998769a4e0390123be59782c06e6c0a52c78403e2/Addadshashanammu.zip
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.40, 3.160.5.95, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5166 (5.0K) [application/octet-stream]
Saving to: 'Addadshashanammu.zip'

Addadshashanammu. 100%[==========>]   5.04K  --.-KB/s    in 0s      

2026-02-11 20:02:30 (715 MB/s) - 'Addadshashanammu.zip' saved [5166/5166]

giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ file Addadshashanammu.zip
Addadshashanammu.zip: Zip archive data, at least v1.0 to extract, compression method=store
giselle_maz-picoctf@webshell:~$ unzip Addadshashanammu.zip 
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
 extracting: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet.c  
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  
``` 

Entramos a todas las carpetas con Tab y vemos el contenido de la ultima:
```
giselle_maz-picoctf@webshell:~$ cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
giselle_maz-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalm
imilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ ls
fang-of-haynekhtnamet  fang-of-haynekhtnamet.c
```

filtramos la palabra pico con strings y listo:

```
lkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ str
ings fang-of-haynekhtnamet | grep pico
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

### Notas Adicionales
picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}