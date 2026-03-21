# Reto: StegoRSA

## Descripción

A message has been encrypted using RSA. The public key is gone… but someone might have been careless with the private key. Can you recover it and decrypt the message? Download the flag and image.

## Solución

descargamos

```
┌──(xrengariox㉿PC)-[~/pico_challenge/StegoRSA]
└─$ wget -q https://challenge-files.picoctf.net/c_plain_mesa/95f2734024e3177de0251995130f525745a8e5d2d9074016f6c7113a76e7e963/flag.enc

┌──(xrengariox㉿PC)-[~/pico_challenge/StegoRSA]
└─$ wget -q https://challenge-files.picoctf.net/c_plain_mesa/95f2734024e3177de0251995130f525745a8e5d2d9074016f6c7113a76e7e963/image.jpg
```

Análisis de esteganografía
Al inspeccionar los metadatos de la imagen con exiftool, se identifica que el campo Comment contiene una cadena de texto en formato hexadecimal.

```jsx
┌──(xrengariox㉿PC)-[~/pico_challenge/StegoRSA]
└─$ exiftool image.jpg
ExifTool Version Number         : 13.50
File Name
```

Extracción de la llave privada
Se extrae el contenido del comentario, se procesa para obtener únicamente el valor hexadecimal y se convierte a binario para reconstruir el archivo de la llave privada (private.pem).
Bash

```jsx
┌──(xrengariox㉿PC)-[~/pico_challenge/StegoRSA]
└─$ exiftool -Comment image.jpg | awk -F': ' '{print $2}' | xxd -r -p > private.pem
```

Descifrado de la bandera
Utilizando la herramienta openssl y la llave recuperada, se realiza el descifrado del archivo flag.enc.
Bash

```
──(xrengariox㉿PC)-[~/pico_challenge/StegoRSA]
└─$ openssl rsa -in private.pem -text -noout
Private-Key: (2048 bit, 2 primes)
modulus:
```

Flag: picoCTF{rs4_k3y_1n_1mg_ce170c3d}

no me aceptaba la flag asi que limpie de caracteres ocultos y listo 

```jsx
┌──(xrengariox㉿PC)-[~/pico_challenge/StegoRSA]
└─$ openssl pkeyutl -decrypt -inkey private.pem -in flag.enc | tr -d '\n\r '
picoCTF{rs4_k3y_1n_1mg_ce170c3d}
```

## Notas adicionales