### Descripción

### Solución
```

giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/151/leak.tar
giselle_maz-picoctf@webshell:~$ grep -n "cultiris" usernames.txt
grep: usernames.txt: No such file or directory
giselle_maz-picoctf@webshell:~$ tar -xf leak.tar
giselle_maz-picoctf@webshell:~$ ls
README.txt                contenido_oculto.bin     heapdump        scrambled1.png
_flag.png-0.extracted     cookies.txt              jwt.txt         scrambled2.png
_flag.png.extracted       data.enc                 leak            secret
_pico.flag.png.extracted  dds1-alpine.flag.img.gz  leak.tar        sol.py
atbash.jpg                decodificar.py           message.txt     solucion.py
bookshelf-pico.zip        enc_flag                 message.txt.1   solution.py
bookshelf-pico.zip.1      encrypted.txt            message.txt.2   solve.py
bookshelf-pico.zip.2      exploit.py               pico.flag.png   solve_amiable.py
bookshelf_pico            flag.png                 readmycert.csr
capture.pcap              flag.png.1               reto_pixelated
concat_v.png              flag_revelada.png        salida_secreta
giselle_maz-picoctf@webshell:~$ cd leak
giselle_maz-picoctf@webshell:~/leak$ grep -n "cultiris" usernames.txt
378:cultiris

giselle_maz-picoctf@webshell:~/leak$ sed -n '378p' passwords.txt
cvpbPGS{P7e1S_54I35_71Z3}


giselle_maz-picoctf@webshell:~/leak$ echo "cvpbPGS{P7e1S_54I35_71Z3}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
picoCTF{C7r1F_54V35_71M3}
```
### Notas adicionales 
picoCTF{C7r1F_54V35_71M3}
### Referencias