### Descripción
This file contains more than it seems.Get the flag from [garden.jpg](https://challenge-files.picoctf.net/c_fickle_tempest/26ad1e959e2e6f15113d4dc2b43649625499d960e546d1b874357c6fcb8c5229/garden.jpg).
### Solución
### Solución 1 - kali
```
se descarga el archivi y se le hace un grep

wget https://challenge-files.picoctf.net/c_fickle_tempest/26ad1e959e2e6f15113d4dc2b43649625499d960e546d1b874357c6fcb8c5229/garden.jpg
--2026-03-09 14:23:05--  https://challenge-files.picoctf.net/c_fickle_tempest/26ad1e959e2e6f15113d4dc2b43649625499d960e546d1b874357c6fcb8c5229/garden.jpg
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.161.44.103, 3.161.44.22, 3.161.44.84, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.161.44.103|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2295191 (2.2M) [application/octet-stream]
Saving to: ‘garden.jpg’

garden.jpg              100%[===============================>]   2.19M  1011KB/s    in 2.2s    

2026-03-09 14:23:21 (1011 KB/s) - ‘garden.jpg’ saved [2295191/2295191]

                                                                                                
┌──(kali㉿kali)-[~]
└─$ file garden.jpg                                                         
garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3



└─$ strings garden.jpg | grep pico
Here is a flag: picoCTF{more_than_m33ts_the_3y333f84d7c}

```
### Notas adicionales 
picoCTF{more_than_m33ts_the_3y333f84d7c}

La esteganografía es una ==técnica milenaria para ocultar información confidencial dentro de otro archivo o soporte físico== (imágenes, audio, texto) para que pase desapercibida. A diferencia de la criptografía, que cifra el mensaje, la esteganografía busca esconder la propia existencia de la comunicación, haciendo que el portador parezca inofensivo. ![Kaspersky](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABIUlEQVQ4jWP8//8/Awww5sXCOf8nLWZkIAIwEaNomBgw8eDOPMa82P8wvP7i6QCiDTj/+KFBwdolE2H8OveApkB90w1EGXD/7Wv5oLn962D8AF3j9Y3ewfVEeyFobv+GB+/eKjIwMDAoCAnfnxedkogsj9eAwvVL+y48eWzAwMDAIMDJ9X5fTpWjIBfPR6INmLB/RyGMPS8qJUlRROwhuhoSohF7wsRrQJ6d2yQYO2nZ7Hn337yWJ8mAiSGx+QYychcYGBgYPnz/Jug0pXX/+29f+Yk2gIGBgWFdcn6AgpDwfQYGBoYH794qJi2dPZ8kAxSFxR6uSy4IgvE3XD4b2LhjfR3RBjAwMDAYyipc6AuIgsdIw7Z1jesvnglgYGBgAABX/GGOHtCjMQAAAABJRU5ErkJggg==)Kaspersky +3
### Referencias
https://www.google.com/search?sca_esv=c9866652b0fe63dd&sxsrf=ANbL-n6Z3uZcMrR53jtXLYE97ele__mjJg:1773080552914&q=esteganograf%C3%ADa&spell=1&sa=X&ved=2ahUKEwjH3o7kt5OTAxW_I0QIHW6mC8UQBSgAegQIDBAB&biw=1280&bih=603&dpr=1.5