### Descripción
Can you decrypt this message?Decrypt this [message](https://artifacts.picoctf.net/c/158/cipher.txt) using this key "CYLAB"

### Solución
```
 
giselle_maz-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/158/cipher.txt
--2026-04-27 16:39:09--  https://artifacts.picoctf.net/c/158/cipher.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.77, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 43 [application/octet-stream]
Saving to: 'cipher.txt'

cipher.txt             100%[============================>]      43  --.-KB/s    in 0s      

2026-04-27 16:39:09 (6.82 MB/s) - 'cipher.txt' saved [43/43]

giselle_maz-picoctf@webshell:~$ cat cipher.txt
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}
giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ python3 -c "
> cipher = 'rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}'
> key = 'CYLAB'
> res = ''
> k_idx = 0
> for c in cipher:
>     if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
>         base = ord('A') if c.isupper() else ord('a')
>         k_val = ord(key[k_idx % len(key)].upper()) - ord('A')
>         res += chr((ord(c) - base - k_val) % 26 + base)
>         k_idx += 1
>     else:
>         res += c
> print(res)
> "
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}
```
### Notas adicionales 
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}
### Referencias