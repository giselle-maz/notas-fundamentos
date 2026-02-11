### Descripción
Can you look at the data in this binary? The bash script might help![static](https://challenge-files.picoctf.net/c_wily_courier/b06384f5fdb3a6e3f0f254d1064d203e7df4bf7e9a5780a95622523367d82bc0/static), [ltdis.sh](https://challenge-files.picoctf.net/c_wily_courier/b06384f5fdb3a6e3f0f254d1064d203e7df4bf7e9a5780a95622523367d82bc0/ltdis.sh)
### Solución
### Solución 1 - Consola
```
giselle_maz-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/b06384f5fdb3a6e3f0f254d1064d203e7df4bf7e9a5780a95622523367d82bc0/static
--2026-02-11 18:41:04--  https://challenge-files.picoctf.net/c_wily_courier/b06384f5fdb3a6e3f0f254d1064d203e7df4bf7e9a5780a95622523367d82bc0/static
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.95, 3.160.5.40, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.95|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16776 (16K) [application/octet-stream]
Saving to: 'static'

static               100%[======================>]  16.38K  --.-KB/s    in 0.005s  

2026-02-11 18:41:04 (3.55 MB/s) - 'static' saved [16776/16776]

giselle_maz-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/b06384f5fdb3a6e3f0f254d1064d203e7df4bf7e9a5780a95622523367d82bc0/ltdis.sh
--2026-02-11 18:41:23--  https://challenge-files.picoctf.net/c_wily_courier/b06384f5fdb3a6e3f0f254d1064d203e7df4bf7e9a5780a95622523367d82bc0/ltdis.sh
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.40, 3.160.5.95, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.40|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 785 [application/octet-stream]
Saving to: 'ltdis.sh'

ltdis.sh             100%[======================>]     785  --.-KB/s    in 0s      

2026-02-11 18:41:24 (398 MB/s) - 'ltdis.sh' saved [785/785]

giselle_maz-picoctf@webshell:~$ ls
README.txt  file  flag  ltdis.sh  salida  static  strings  warm
giselle_maz-picoctf@webshell:~$ file ltdis   
ltdis: cannot open `ltdis' (No such file or directory)
giselle_maz-picoctf@webshell:~$ file ltdis.sh
ltdis.sh: Bourne-Again shell script, ASCII text executable
giselle_maz-picoctf@webshell:~$ file statics 
statics: cannot open `statics' (No such file or directory)
giselle_maz-picoctf@webshell:~$ file static 
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=9a00d4dca6b92d22aa0cd1fceffa4ed7495b8534, for GNU/Linux 3.2.0, not stripped
giselle_maz-picoctf@webshell:~$ chmod +x ltdis.sh
giselle_maz-picoctf@webshell:~$ chmod +x static  
giselle_maz-picoctf@webshell:~$ .\static 
-bash: .static: command not found
giselle_maz-picoctf@webshell:~$ .\ltdis.sh static
-bash: .ltdis.sh: command not found
giselle_maz-picoctf@webshell:~$ string static | grep pico
-bash: string: command not found
giselle_maz-picoctf@webshell:~$ strings static | grep pico
picoCTF{d15a5m_t34s3r_20335e41}
giselle_maz-picoctf@webshell:~$ ^C
```

### Notas adicionales

picoCTF{d15a5m_t34s3r_20335e41}