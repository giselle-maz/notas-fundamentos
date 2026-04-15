### Descripción
Can you make sense of this file?Download the file [here](https://artifacts.picoctf.net/c/472/enc_flag).

### Solución
### Solución 1 - Consola
```
giselle_maz-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/472/enc_flag
--2026-02-11 19:09:48--  https://artifacts.picoctf.net/c/472/enc_flag
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 349 [application/octet-stream]
Saving to: 'enc_flag'

enc_flag             100%[======================>]     349  --.-KB/s    in 0s      

2026-02-11 19:09:48 (66.2 MB/s) - 'enc_flag' saved [349/349]

giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ cat enc_flag
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZrTTBKeldWaHdRMDB4V2tWU2JFNVdDbUpXV2tkVU1WcFhWVzFHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
giselle_maz-picoctf@webshell:~$ cat enc_flag | base64 -d
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlVkM0JzWVhwQ00xWkVSbE5WCmJWWkdUMVpXVW1GdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==
giselle_maz-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFUd3BsYXpCM1ZERlNV
bVZGT1ZWUmFteEVXbm93T1VOblBUMEsK
giselle_maz-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d | base64 -d
WTBkc2FtSXdUbFZTYm5ScFdWaE9iRTVxVW1aaWFrNTZaRVJPYTFneVVuQlpla0pyU1ZjME5GZ3lV
WGRrTWpWelRVUlNhMDB5VW1aTwplazB3VDFSUmVFOVVRamxEWnowOUNnPT0K
giselle_maz-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d
Y0dsamIwTlVSbnRpWVhObE5qUmZiak56ZEROa1gyUnBZekJrSVc0NFgyUXdkMjVzTURSa00yUmZO
ek0wT1RReE9UQjlDZz09Cg==
giselle_maz-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfNzM0OTQxOTB9Cg==
giselle_maz-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_73494190}
```

### Solución 2 - Cyber Chef
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVhRmRXZWtab1dWWmtSMk5yTlZWWA0KYlVaVFZtdHdVVmRXVWtkaWJWWlhWbTVXVWdwaVNFSnpXVlJDZDJWV1ZYaFhiWEJPVWxSV1NGZHFUbk5XWjNCWVVqRktlVlpHWkhkVw0KTWxaelZXeGFWbUpGTlc5VVZWSkRUbFphV0UxWFJsVmtNMEp6V1Zod1EwMHhXa1ZTYkU1V0NtSldXa2RVTVZwWFZXMUdkR1ZGVmxoaQ0KYlRrelZERldUMkpzUWxWTlJYTkxDZz09&ieol=CRLF
 
### Notas adicionales
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_73494190}