### Descripción
Do you know how to use the web inspector?Start searching [here](http://titan.picoctf.net:51704/) to find the flag
### Solución
### Solución 1 - Usando CyberChef

```
checamos el codigo de cada boton, en el de about encontamos texto base64, convertimos con cyberchef y ahi esta la flag:

https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Y0dsamIwTlVSbnQzWldKZmMzVmpZek56YzJaMWJHeDVYMlF6WXpCa1pXUmZNRGRpT1RGak56bDk
```
### Notas adicionales 
picoCTF{web_succ3ssfully_d3c0ded_07b91c79}
### Referencias