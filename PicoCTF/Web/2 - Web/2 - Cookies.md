### Descripción
Who doesn't love cookies? Try to figure out the best one. http://wily-courier.picoctf.net:63480/
### Solución
### Solución 1 - cookie editor + consola
```
name = 18

ciclo for

for i in {1...20}; do curl -s http://wily-courier.picoctf.net:63480/ -H "Cookie: name=$i" done | grep pico
```
### Notas adicionales 
`picoCTF{3v3ry1_l0v3s_c00k135_a4dadb49}`
### Referencias
