### Descripción
Decrypt this message.Message: [message](https://challenge-files.picoctf.net/c_fickle_tempest/bfd7c036228a50ff9e76dfc29ac6cec116f209f0db26506497997f0aca083105/data.enc)
### Solución
```
giselle_maz-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_fickle_tempest/bfd7c036228a50ff9e76dfc29ac6cec116f209f0db26506497997f0aca083105/data.enc
--2026-04-14 05:42:12--  https://challenge-files.picoctf.net/c_fickle_tempest/bfd7c036228a50ff9e76dfc29ac6cec116f209f0db26506497997f0aca083105/data.enc
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.95, 3.160.5.18, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 36 [application/octet-stream]
Saving to: 'data.enc'

data.enc               100%[============================>]      36  --.-KB/s    in 0s      

2026-04-14 05:42:13 (823 KB/s) - 'data.enc' saved [36/36]

giselle_maz-picoctf@webshell:~$ file data.enc
data.enc: ASCII text
giselle_maz-picoctf@webshell:~$ strings data.enc | grep "pico"
picoCTF{dspttjohuifsvcjdpohatwvibg}

 como  obtuve el contenido de la flag cifrado
 
giselle_maz-picoctf@webshell:~$ echo "dspttjohuifsvcjdpohatwvibg" | tr 'b-zaB-ZA' 'a-yzA-YZ'
crossingtherubicongzsvuhaf
```
### Notas adicionales 
picoCTF{crossingtherubicongzsvuhaf}
### Referencias
