### Descripción
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?
### Solución
### Solución 1 - Usando CyberChef
https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=eDcw
### Solución 2 - Python
```
python
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> int(0x70)
112
>>> chr(112)
'p'
```
### Notas adicioales 
int convierte a entero.
int(0x70) = 112

chr devuelve el caracter ASCII correspondiente al número dado. 
chr(112) = 'p'
### Referencias