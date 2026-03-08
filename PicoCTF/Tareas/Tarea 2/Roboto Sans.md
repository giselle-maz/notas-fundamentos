### Descripción
The flag is somewhere on this web application not necessarily on the website. Find it.Check [this](http://saturn.picoctf.net:61101/) out.
### Solución
### Solución 1 - Usando CyberChef
```

por el nombre del reto vamos a
robots.txt
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.
encontramos texto base64 

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/

lo transformamos con cyberchef
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=YW5NdmJYbG1hV3hsTG5SNGRB&ieol=CRLF&oeol=CRLF

nos da la direccion /js/myfile.txt,el cual visitamos y nos da la flag

http://saturn.picoctf.net:61101/js/myfile.txt
picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}
```
### Notas adicionales 
picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}
### Referencias