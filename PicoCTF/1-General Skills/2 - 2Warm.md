### Descripción
Can you convert the number 42 (base 10) to binary (base 2)?
### Solución
### Solución 1 - CyberChef
https://gchq.github.io/CyberChef/#recipe=To_Base(2)&input=NDIK

### Solución 2 - Python
```
python
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> bin(42)
'0b101010'

picoCTF{101010}
```
### Notas adicionales 
int convierte a entero.
int(0x70) = 112

chr devuelve el caracter ASCII correspondiente al número dado. 
chr(112) = 'p'