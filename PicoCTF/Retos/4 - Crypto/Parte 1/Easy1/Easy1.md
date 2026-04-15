### Descripción
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this?We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this [table](https://challenge-files.picoctf.net/c_fickle_tempest/859ffc313a4d8b63149f144745043a7312fc4f993e405eeeb8ee5ae6ca8444a8/table.txt) to solve it?.
### Solución
```
 
giselle_maz-picoctf@webshell:~$ python3 -c "
> cifrado = 'UFJKXQZQUNB'
> key = 'SOLVECRYPTO'
> decrip = ''
> for i in range(len(cifrado)):
>     # Restamos las posiciones de las letras (A=0, B=1...)
>     letra = chr(((ord(cifrado[i]) - ord(key[i]) + 26) % 26) + ord('A'))
>     decrip += letra
> print(decrip)
> "
CRYPTOISFUN

picoCTF{CRYPTOISFUN}
```
### Notas adicionales 
picoCTF{CRYPTOISFUN}
### Referencias
