### Descripción
I've hidden a flag in this file. Can you find it?[Forensics_is_fun.pptm](https://challenge-files.picoctf.net/c_wily_courier/d78815176c19ddc85a1388233268d2f4c459fcbbaab197b4a29ebafc88294c54/Forensics_is_fun.pptm)
### Solución
### Solución 1 - kali
```

se descraga, descomprime y vemos donde esta la bandera, hacemos un cat.

└─$ wget https://challenge-files.picoctf.net/c_wily_courier/d78815176c19ddc85a1388233268d2f4c459fcbbaab197b4a29ebafc88294c54/Forensics_is_fun.pptm 

--2026-03-18 15:15:02--  https://challenge-files.picoctf.net/c_wily_courier/d78815176c19ddc85a1388233268d2f4c459fcbbaab197b4a29ebafc88294c54/Forensics_is_fun.pptm
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 18.154.206.121, 18.154.206.27, 18.154.206.14, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|18.154.206.121|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 100093 (98K) [application/octet-stream]
Saving to: ‘Forensics_is_fun.pptm.1’

Forensics_is_fun.pptm.1 100%[==============================>]  97.75K   134KB/s    in 0.7s    

2026-03-18 15:15:06 (134 KB/s) - ‘Forensics_is_fun.pptm.1’ saved [100093/100093]
            
┌──(kali㉿kali)-[~]
└─$ file "Forensics is fun.pptm.1"
Forensics is fun.pptm.1: cannot open `Forensics is fun.pptm.1' (No such file or directory)
                     
┌──(kali㉿kali)-[~]
└─$ ls
8.7              Desktop     Forensics_is_fun.pptm    message.wav            Pictures   Videos
buildings.png    Documents   Forensics_is_fun.pptm.1  Music                  Public
buildings.png.1  Downloads   garden.jpg               pico_img.png           sstv
capture.pcap     extensions  hash                     pico_img.png_original  Templates                                           
┌──(kali㉿kali)-[~]
└─$ unzip "Forensics is fun.pptm"
unzip:  cannot find or open Forensics is fun.pptm, Forensics is fun.pptm.zip or Forensics is fun.pptm.ZIP.       
┌──(kali㉿kali)-[~]
└─$ unzip Forensics_is_fun.pptm
Archive:  Forensics_is_fun.pptm
  inflating: [Content_Types].xml     
  inflating: _rels/.rels             
  inflating: ppt/presentation.xml    
  inflating: ppt/slides/_rels/slide46.xml.rels  
  inflating: ppt/slides/slide1.xml   
  inflating: ppt/slides/slide2.xml   
  ...  ppt/slideLayouts/_rels/slideLayout11.xml.rels  
  inflating: ppt/theme/theme1.xml    
 extracting: docProps/thumbnail.jpeg  
  inflating: ppt/vbaProject.bin      
  inflating: ppt/presProps.xml       
  inflating: ppt/viewProps.xml       
  inflating: ppt/tableStyles.xml     
  inflating: docProps/core.xml       
  inflating: docProps/app.xml        
  inflating: ppt/slideMasters/hidden  
                                                                                               
┌──(kali㉿kali)-[~]
└─$ cd ppt/slideMasters
cat hidden
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q                                                                                               
┌──(kali㉿kali)-[~/ppt/slideMasters]
└─$ cat hidden | tr -d ' ' | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}                                     
```
### Notas adicionales 
picoCTF{D1d_u_kn0w_ppts_r_z1p5}
### Referencias