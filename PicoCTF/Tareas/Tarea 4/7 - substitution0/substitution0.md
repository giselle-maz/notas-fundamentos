### Descripción
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?Download the message [here](https://artifacts.picoctf.net/c/152/message.txt).
### Solución
```
wget https://artifacts.picoctf.net/c/152/message.txt
--2026-04-27 16:12:51--  https://artifacts.picoctf.net/c/152/message.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.72, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 670 [application/octet-stream]
Saving to: 'message.txt'

message.txt            100%[============================>]     670  --.-KB/s    in 0s      

2026-04-27 16:12:51 (26.9 MB/s) - 'message.txt' saved [670/670]

giselle_maz-picoctf@webshell:~$ cat message.txt
DECKFMYIQJRWTZPXGNABUSOLVH 

Ifnfuxpz Wfyndzk dnpaf, oqbi d yndsf dzk abdbfwv dqn, dzk enpuyib tf bif effbwf
mnpt d ywdaa cdaf qz oiqci qb oda fzcwpafk. Qb oda d efdubqmuw acdndedfua, dzk, db
bidb bqtf, uzrzpoz bp zdbundwqaba—pm cpunaf d ynfdb xnqhf qz d acqfzbqmqc xpqzb
pm sqfo. Bifnf ofnf bop npuzk ewdcr axpba zfdn pzf flbnftqbv pm bif edcr, dzk d
wpzy pzf zfdn bif pbifn. Bif acdwfa ofnf flcffkqzywv idnk dzk ywpaav, oqbi dww bif
dxxfdndzcf pm eunzqaifk ypwk. Bif ofqyib pm bif qzafcb oda sfnv nftdnrdewf, dzk,
bdrqzy dww biqzya qzbp cpzaqkfndbqpz, Q cpuwk idnkwv ewdtf Juxqbfn mpn iqa pxqzqpz
nfaxfcbqzy qb.

Bif mwdy qa: xqcpCBM{5UE5717U710Z_3S0WU710Z_59533D2F}giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ echo "xqcpCBM{5UE5717U710Z_3S0WU710Z_59533D2F}" | tr "DECKFMYIQJRWTZPXGNABUSOLVHdeckfmyiqjrwtzpxgnabusolvh" "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
picoCTF{5UB5717U710N_3V0LU710N_59533A2E}
```
### Notas adicionales 
picoCTF{5UB5717U710N_3V0LU710N_59533A2E}
### Referencia