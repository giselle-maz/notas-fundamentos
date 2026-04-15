
### Descripción 
Unzip this archive and find the flag.
- [Download zip file](https://artifacts.picoctf.net/c/503/big-zip-files.zip)
### Solución
### Solución 1 - Consola
- wget Download zip file](https://artifacts.picoctf.net/c/503/big-zip-files.zip
- unzip 


```
giselle_maz-picoctf@webshell:~$ ls
README.txt  big-zip-files  big-zip-files.zip  enc_flag
giselle_maz-picoctf@webshell:~$ grep -r pico   
.python_history:'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
.bash_history:nc saturn.picoctf.net 49386
.bash_history:nc wily-courier.picoctf.net 61493
.bash_history:nc fickle-tempest.picoctf.net 53600
.bash_history:wget https://challenge-files.picoctf.net/c_fickle_tempest/6577d3f1500aebcd300787bd5d96216b30aed379c811f5e83e888f897da4a3d5/strings
.bash_history:strings strings | grep pico
.bash_history:wget https://challenge-files.picoctf.net/c_wily_courier/5a478d0b24d6a4f4185e3adb7a78c41cdad626fb02fe80e083dc33bf8b197d3d/warm
.bash_history:wget https://challenge-files.picoctf.net/c_wily_courier/b06384f5fdb3a6e3f0f254d1064d203e7df4bf7e9a5780a95622523367d82bc0/static
.bash_history:wget https://challenge-files.picoctf.net/c_wily_courier/b06384f5fdb3a6e3f0f254d1064d203e7df4bf7e9a5780a95622523367d82bc0/ltdis.sh
.bash_history:string static | grep pico
.bash_history:strings static | grep pico
.bash_history:ssh picoplayer@saturn.picoctf.net -p59144
.bash_history:wget https://challenge-files.picoctf.net/c_wily_courier/56f53a4189949d066fe969e998769a4e0390123be59782c06e6c0a52c78403e2/Addadshashanammu.zip
.bash_history:sshh ctf-player@wily-courier.picoctf.net -p57041
.bash_history:ssh ctf-player@wily-courier.picoctf.net -p57041
README.txt:Welcome to the picoCTF webshell!
README.txt:picoCTF challenges.
README.txt:other@picoctf.org and we will consider adding it.
README.txt:  Extensive brute-forcing is not necessary to solve picoCTF challenges.
README.txt:- If you change your username through the picoCTF website, you will
big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

### Notas adicionales
unzip -l kscn.zip listar sin des empaquetar

picoCTF{gr3p_15_m4g1c_ef8790dc}

