## **Descripcion**
This file doesn't look like much... just a bunch of 1s and 0s. But maybe it's not just random noise. Can you recover anything meaningful from this? Download the file [here](https://challenge-files.picoctf.net/c_plain_mesa/c443005e8024af39085323276b34da0e92f968746547f8e7f8b650ab37e668d1/digits.bin).
## **Solucion**
picoCTF{h1dd3n_1n_th3_b1n4ry_cc2099d3}
## **Notas adicionales**
### Paso 1:

Se utilizó la herramienta **CyberChef** (u otro script de conversión) para transformar la cadena de texto de base 2 (binario) a su representación en bytes (raw data).

1. **Input:** Se pegó el contenido completo de unos y ceros.
    
2. **Operación:** Se aplicó la receta **"From Binary"**. Esto convierte cada grupo de 8 bits en un byte real.
    
### Paso 2: 

Dado que el resultado no era texto ASCII legible (la "flag"), se interpretó que el output era un objeto binario.

1. Se utilizó la opción **"Download output to file"** en CyberChef.
    
2. Se guardó el archivo con la extensión identificada en la fase 2: `.jpg`.
    

### Paso 3: 

Al abrir el archivo de imagen resultante (`imagen.jpg`), se visualizó el contenido gráfico que contenía el texto de la flag en formato `picoCTF{...}`.
## **Referencias**
https://en.wikipedia.org/wiki/List_of_file_signatures
https://gchq.github.io/CyberChef/