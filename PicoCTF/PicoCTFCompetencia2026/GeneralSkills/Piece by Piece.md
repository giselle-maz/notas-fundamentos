### [Piece by Piece](https://play.picoctf.org/events/79/challenges?category=5&page=1#:~:text=General%20Skills-,Piece%20by%20Piece,-3%2C550%20solves)

### DESCRIPCIÓN

After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag.

`ssh to dolphin-cove.picoctf.net:62694` and login as ctf-player with password `1ad5be0d`.
### SOLUCIÓN

El reto consiste en la reconstrucción de un archivo comprimido que ha sido fragmentado en varias partes y protegido por una contraseña.

#### 1. Combinación de fragmentos:
Identificamos cinco archivos (part_aa hasta part_ae). Utilizamos el comando cat para unirlos en un solo archivo manteniendo el orden alfabético:

```
ctf-player@pico-chall$ cat part_* > combined_file
```

#### 2. Identificación y extracción protegida:
Al usar el comando file, confirmamos que el resultado es un archivo ZIP. Al intentar descomprimirlo con unzip, el sistema solicitó una contraseña. Para encontrarla, revisamos el archivo de pistas:

```
ctf-player@pico-chall$ cat instructions.txt
```

El archivo indicaba: Use this "supersecret" password to extract the zip file.

#### 3. Obtención de la bandera:
Ejecutamos el comando de descompresión ingresando la contraseña encontrada y finalmente leímos el archivo extraído:

```
ctf-player@pico-chall$ unzip combined_file
[combined_file] flag.txt password: supersecret
extracting: flag.txt
ctf-player@pico-chall$ cat flag.txt
```


### NOTAS ADICIONALES


### REFERENCIAS