### Descripcion
We found this weird message being passed around on the servers, we think we have a working decryption scheme.Download the message [here](https://artifacts.picoctf.net/c/129/message.txt).Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
### Solucion

```
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c/129/message.txt
giselle_maz-picoctf@webshell:~$ cat message.txt
350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213 

y con ayuda de gemini deciframos segun las indicaciones (mod 37)

### Resultado Final

Al unir todos los caracteres obtenidos, el mensaje es: `R0UND_N_R0UND_ADD17EC2`.

**La flag es:** `picoCTF{R0UND_N_R0UND_ADD17EC2}`

o

giselle_maz-picoctf@webshell:~$ nano sol.py

#!/usr/bin/env python3

# Datos extraídos del mensaje
numbers = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213]

# Definición del mapa de caracteres (índice 0 a 36)
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

def solve():
    result = ""
    for n in numbers:
        # Aplicar módulo 37 para obtener el índice
        index = n % 37
        # Mapear el índice al carácter correspondiente
        result += charset[index]
    
    # Formatear la salida con el prefijo del reto
    print(f"picoCTF{{{result}}}")

if __name__ == "__main__":
    solve()


giselle_maz-picoctf@webshell:~$ python3 sol.py
picoCTF{R0UND_N_R0UND_ADD17EC2}

```
### Notas adicionales 
picoCTF{R0UND_N_R0UND_ADD17EC2}
### Referencias

