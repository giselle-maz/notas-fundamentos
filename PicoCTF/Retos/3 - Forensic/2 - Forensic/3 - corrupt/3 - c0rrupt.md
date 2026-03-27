### Descripción
We found this [file](https://challenge-files.picoctf.net/c_fickle_tempest/87bdc8ce30b177d033b3d68bca4647950bb07304032861baa912ebe08701d355/mystery). Recover the flag.
### Solución
### Solución 1 - kali
```
descragamos, vemos el tipo y contenido hexadecimal, notamos que esta corrupto, usamos exeditor 
┌──(kali㉿kali)-[~/sstv]
└─$ wget -q https://challenge-files.picoctf.net/c_fickle_tempest/87bdc8ce30b177d033b3d68bca4647950bb07304032861baa912ebe08701d355/mystery    
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ file mystery 
mystery: data
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ xxd -l 100 mystery
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
00000060: 8e64 cd71                                .d.q
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mistery


cambiamos los bits corruptos por los bits correctos y guardamos. al abrir el archivo nos muestra la flag (no logre instalar el sudo apt install pngcheck por ello hice todos los cambios de una vez)
                                                                                              
┌──(kali㉿kali)-[~/sstv]
└─$ sudo apt install pngcheck
[sudo] password for kali: 
Error: Unable to locate package pngcheck
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ sudo apt update
sudo apt install pngcheck
Get:1 http://kali.download/kali kali-rolling InRelease [34.0 kB]
Get:2 http://kali.download/kali kali-rolling/main amd64 Packages [20.9 MB]
Get:3 http://kali.download/kali kali-rolling/main amd64 Contents (deb) [52.7 MB]               
Get:4 http://kali.download/kali kali-rolling/contrib amd64 Packages [118 kB]                   
Get:5 http://kali.download/kali kali-rolling/contrib amd64 Contents (deb) [275 kB]             
Get:6 http://kali.download/kali kali-rolling/non-free amd64 Packages [184 kB]                  
Get:7 http://kali.download/kali kali-rolling/non-free amd64 Contents (deb) [880 kB]            
Get:8 http://kali.download/kali kali-rolling/non-free-firmware amd64 Packages [14.3 kB]        
Get:9 http://kali.download/kali kali-rolling/non-free-firmware amd64 Contents (deb) [33.8 kB]  
95% [3 Contents-amd64 store 0 B]                                                               
95% [3 Contents-amd64 store 0 B]
95% [3 Contents-amd64 store 0 B]^C
                                                                                                
^X
┌──(kali㉿kali)-[~/sstv]
└─$ pngcheck -v mistery
Command 'pngcheck' not found, but can be installed with:
sudo apt install pngcheck
Do you want to install it? (N/y)y   
sudo apt install pngcheck
Error: Unable to locate package pngcheck
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ sudo apt install libpng-tools
Error: Unable to locate package libpng-tools
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ file mystery   
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ open mystery.png
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery            
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ open mystery.png 
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ file mystery     
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ file mystery     
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery
                         
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery
                                                        
┌──(kali㉿kali)-[~/sstv]
└─$ file mystery     
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced

┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery
                                                                                              
┌──(kali㉿kali)-[~/sstv]
└─$ sudo apt install pngcheck
[sudo] password for kali: 
Error: Unable to locate package pngcheck
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ sudo apt update
sudo apt install pngcheck
Get:1 http://kali.download/kali kali-rolling InRelease [34.0 kB]
Get:2 http://kali.download/kali kali-rolling/main amd64 Packages [20.9 MB]
Get:3 http://kali.download/kali kali-rolling/main amd64 Contents (deb) [52.7 MB]               
Get:4 http://kali.download/kali kali-rolling/contrib amd64 Packages [118 kB]                   
Get:5 http://kali.download/kali kali-rolling/contrib amd64 Contents (deb) [275 kB]             
Get:6 http://kali.download/kali kali-rolling/non-free amd64 Packages [184 kB]                  
Get:7 http://kali.download/kali kali-rolling/non-free amd64 Contents (deb) [880 kB]            
Get:8 http://kali.download/kali kali-rolling/non-free-firmware amd64 Packages [14.3 kB]        
Get:9 http://kali.download/kali kali-rolling/non-free-firmware amd64 Contents (deb) [33.8 kB]  
95% [3 Contents-amd64 store 0 B]                                                               
95% [3 Contents-amd64 store 0 B]
95% [3 Contents-amd64 store 0 B]^C
                                                                                                
^X
┌──(kali㉿kali)-[~/sstv]
└─$ pngcheck -v mistery
Command 'pngcheck' not found, but can be installed with:
sudo apt install pngcheck
Do you want to install it? (N/y)y   
sudo apt install pngcheck
Error: Unable to locate package pngcheck
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ sudo apt install libpng-tools
Error: Unable to locate package libpng-tools
       
┌──(kali㉿kali)-[~/sstv]
└─$ file mystery   
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ open mystery.png
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery 

┌──(kali㉿kali)-[~/sstv]
└─$ file mystery     
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
                      
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery                                    
┌──(kali㉿kali)-[~/sstv]
└─$ file mystery     
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
                                                       
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery
                                       
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery                                                      
┌──(kali㉿kali)-[~/sstv]
└─$ file mystery     
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
                     
┌──(kali㉿kali)-[~/sstv]
└─$ hexeditor mystery
                                                                           

```
### Notas adicionales 
picoCTF{c0rrupt10n_1847995}
### Referencias