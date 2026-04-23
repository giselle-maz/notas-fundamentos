### Descripcion
I have these 2 images, can you make a flag out of them?[scrambled1.png](https://challenge-files.picoctf.net/c_wily_courier/e9637222852661fff9c7ef33644e4f2084ffe3c693d4efaad4d88eec98ddd3e4/scrambled1.png) [scrambled2.png](https://challenge-files.picoctf.net/c_wily_courier/e9637222852661fff9c7ef33644e4f2084ffe3c693d4efaad4d88eec98ddd3e4/scrambled2.png)
### Solución
```
descragamos y buscamos la flag
giselle_maz-picoctf@webshell:~/reto_pixelated$ wget https://challenge-files.picoctf.net/c_wily_courier/e9637222852661fff9c7ef33644e4f2084ffe3c693d4efaad4d88eec98ddd3e4/scrambled1.png
--2026-04-22 19:47:19--  https://challenge-files.picoctf.net/c_wily_courier/e9637222852661fff9c7ef33644e4f2084ffe3c693d4efaad4d88eec98ddd3e4/scrambled1.png
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.18, 3.160.5.40, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 197174 (193K) [application/octet-stream]
Saving to: 'scrambled1.png'

scrambled1.png         100%[============================>] 192.55K  --.-KB/s    in 0.1s    

2026-04-22 19:47:19 (1.86 MB/s) - 'scrambled1.png' saved [197174/197174]

giselle_maz-picoctf@webshell:~/reto_pixelated$ wget https://challenge-files.picoctf.net/c_wily_courier/e9637222852661fff9c7ef33644e4f2084ffe3c693d4efaad4d88eec98ddd3e4/scrambled2.png
--2026-04-22 19:47:21--  https://challenge-files.picoctf.net/c_wily_courier/e9637222852661fff9c7ef33644e4f2084ffe3c693d4efaad4d88eec98ddd3e4/scrambled2.png
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.95, 3.160.5.18, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 197173 (193K) [application/octet-stream]
Saving to: 'scrambled2.png'

scrambled2.png         100%[============================>] 192.55K  --.-KB/s    in 0.1s    

2026-04-22 19:47:21 (1.86 MB/s) - 'scrambled2.png' saved [197173/197173]

giselle_maz-picoctf@webshell:~/reto_pixelated$ convert scrambled1.png scrambled2.png -compose plus -composite flag.png
giselle_maz-

usando este codigo:
from PIL import Image
import numpy as np

# Cargar las imágenes
img1 = Image.open("scrambled1.png").convert("RGB")
img2 = Image.open("scrambled2.png").convert("RGB")

# Convertir a arrays numéricos para operar
data1 = np.asarray(img1).astype(np.uint64) # Usamos uint64 para evitar desbordamiento al sumar
data2 = np.asarray(img2).astype(np.uint64)

# Sumar los píxeles (esto es el "stacking")
# El módulo 256 asegura que el resultado vuelva a ser un color válido (0-255)
res_data = (data1 + data2) % 256

# Guardar la imagen resultante
res_img = Image.fromarray(res_data.astype(np.uint8))
res_img.save("flag_revelada.png")
print("¡Hecho! Revisa flag_revelada.png")
picoctf@webshell:~/reto_pixelated$ nano fla.py
giselle_maz-picoctf@webshell:~/reto_pixelated$ python3 fla.py
¡Hecho! Revisa flag_revelada.png


encontramso la flag en base 64
giselle_maz-picoctf@webshell:~/reto_pixelated$ 
giselle_maz-picoctf@webshell:~/reto_pixelated$ base64 flag_revelada.png
iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAH1UlEQVR4nO3YTUiU7xrH8ds6aaPB
TE1aamTSQoMWFRFk4YwSQbXIRQWWaSWGRCQtgwiMCiSjJHohSsoiJEWN1EW4zSJaTiBhLlxEi3yr
lJEZvc5iqDM4FZ7Tyfzz+35Wz8zcc90P+nydeUwyMweoWvC3TwD4mwgA0ggA0ggA0ggA0ggA0ggA
0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA
0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA0ggA
0ggA0ggA0ggA0ggA0ggA0gjgP2pqampra/+39/b19dXV1Y2Njf3+adTW1p4+ffr352BW7B8iFArd
vHlzNivv3LmzcePGwsLC3bt3Dw4OmllbW1sgEAgEAgsXLowdtLS0eDyewDdXrlwxM6/XG4lEenp6
tm7dGgwGt2/f3tvb++u9vF5v7CA/P7+hoSEUCu3cuTMQCOzZs+fjx49mNj4+fuDAgUAgsGnTps7O
zsQJiQsikcj3sfjT/jEBzNLz58+LioomJibMrLu7u7i4OP7V+Asr8SKLPZOTkzMwMGBm/f3969at
+/V234f4fD4z27FjR09Pj5n19PRUV1ebWV1d3eXLl83sw4cPOTk5iRN+uIAA5sy//vYn0E/5fL6q
qqpXr14lJSU9ePAgNzfX5/ONjo5++vTp+PHjw8PDycnJjx49mp6ePnbs2NevX5csWdLY2FhfX3/p
0iWPx+Oc27VrV3t7eyQSWbRo0ez39fv9Q0NDubm5Q0ND4+PjzrkZO5pZVVXVyMjI2rVrY2+5devW
ly9fgsFgKBQKBoPOuWAweOLECedcVVVVWlqac+7t27ex05gxLXEB5tTfLvCnFi9e3NzcbGYPHz4s
KSmxb38Xy8vLHz9+bGaNjY3V1dUHDx5samoys6ampkOHDmVnZ4fD4Z/N/MUnQGdn5759+8zs9evX
KSkp69evT0lJefbsWeKOZWVlsQza29tTUlLipxUXF7e1tZlZS0tL/PyysrLU1NTYh8OMaYkLzGz/
/v0//L6E/7v5G4DH45mcnDSzcDi8YsUK+3aRZWdnx56PRqOjo6NZWVmxKz4cDmdlZa1cuXKWAcTf
A/T19XV1de3du9fMCgsLW1tbzezJkydHjx5N3HHVqlWxLSKRSGpqavzkgYGBkpKSYDBYX1+fnp4e
v3VHR8fhw4cTpyUuMLPS0tKurq7f+OFhtuZvAGlpadFo1MzC4fDq1avt20U24xLPzMyMD6CwsPDV
q1exl6anp8vLy+NnzuYeYOnSpVNTU2YWjUb9fn/ijhkZGbGHk5OTHo8n/r0XL16MXdzv3r3btm2b
mZ08eTISicSmLVu2LHFa4oIfnhv+kPn7b9BoNNrd3e2ca2lpKSoq+v78li1bnj596py7e/fumTNn
ioqKWltbnXOtra2xb95nz56dnJx0zjU3N8cO/it5eXkvXrxwzr18+XLNmjWJOxYUFMQetre3m1n8
e9+8eRM75/v375eWljrnxsbGOjo6nHO9vb15eXmJ0xIXYC4lzfgVzh8+n6+kpGRgYMDn8927dy89
PT12E/z+/fvKykoz83q9TU1NExMTlZWV4+PjaWlpjY2NmZmZFy5caG5uTk9Pz8jIuHHjxvLly+Nn
jo6OJh7HeL3e4eHhUCh06tQp51xSUtK1a9c2bNgwY8eRkZGKigrnXEFBwe3bt2NDYtP6+/uPHDky
NTW1efPmhoaGBQsWDA4OVlRUTE9PJycnX79+PT8/f8a0z58/z1gwNTXl9/tnnBv+kHkdwBxfBDU1
NX6//9y5c3O5aaLz58+PjIxcvXr1756GCAKAtPkbADAH5u9NMDAHCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS
CADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADSCADS/g0AGtbvyH3D1AAA
AABJRU5ErkJggg==
```
### Notas adicionales 
picoCTF{d562333d}
### Referencias