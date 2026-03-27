## **Descripcion**
We intercepted a suspiciously encoded message, but it’s clearly hiding a flag. No encryption, just multiple layers of obfuscation. Can you peel back the layers and reveal the truth?Download the [message](https://challenge-files.picoctf.net/c_plain_mesa/4d704277dbae3e29292d21448721b73ceede014eec796d45dc59ceb945f649f6/message.txt).
## **Solucion**

picoCTF{nested_enc0ding_848a466b}
## **Notas adicionales**
Para resolverlo, se utilizó la herramienta **CyberChef** siguiendo este "Pipeline" de operaciones:

1. **From Base64**: Convierte la cadena original en una secuencia de números hexadecimales.
    
2. **From Hex**: Transforma los números en una cadena de texto que aún parece cifrada (`cvpbPGS%7B...`).
    
3. **URL Decode**: Traduce los caracteres especiales como `%7B` y `%7D` en llaves `{` y `}`.
    
4. **ROT13**: Descifra la rotación de caracteres de la bandera.
## **Referencias**
https://gchq.github.io/CyberChef/