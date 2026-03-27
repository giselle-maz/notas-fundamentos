### Descripción
There's something in the [building](https://challenge-files.picoctf.net/c_fickle_tempest/c0eec6af0f04316e2bdc4a9f095afd0e2d0121f5e543dbc4a65bb0038d72a993/buildings.png). Can you retrieve the flag?
### Solución
### Solución 1 - kali
```
┌──(kali㉿kali)-[~/extensions]
└─$ wget -q https://challenge-files.picoctf.net/c_fickle_tempest/31fe772e6a4c71e867af0b2a93818e06d8f8ebf8af2a9615495d00356ff576da/flag.txt     
                                                                             
┌──(kali㉿kali)-[~/extensions]
└─$ mkdir extensions
                                             
┌──(kali㉿kali)-[~/extensions]
└─$ cd!$         

┌──(kali㉿kali)-[~]
└─$ cd extensions                 
                                                                             
┌──(kali㉿kali)-[~/extensions]
└─$ xxd -l 20 flag.txt
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 06a1                                ....
                                                                             
┌──(kali㉿kali)-[~/extensions]
└─$ mv flag.txt flag.png          
                                                                             
┌──(kali㉿kali)-[~/extensions]
└─$ open flag.png 
la flag esta en la imagen, la tomamos de ahi
```
### Notas adicionales 
picoCTF{now_you_know_about_extensions}
### Referencias