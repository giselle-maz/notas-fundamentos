## **Descripcion**
A message was encrypted using a shared secret... but it looks like one side of the exchange leaked something. Can you piece together the secret and get the flag? Download the [message](https://challenge-files.picoctf.net/c_plain_mesa/c8a5539995f5df2ced4781eae39980d1aae02329b3aadfcce172854a0ea27f98/message.txt). And source [code](https://challenge-files.picoctf.net/c_plain_mesa/c8a5539995f5df2ced4781eae39980d1aae02329b3aadfcce172854a0ea27f98/encryption.py)
## **Solucion**
picoCTF{dh_s3cr3t_32ec2679}


## **Notas adicionales**
- `message.txt`: Contiene los parámetros públicos (g,p,A), un valor supuestamente privado (b) y el mensaje cifrado en hexadecimal (`enc`).
    
- `encryption.py`: El código fuente que revela cómo se generó el secreto y cómo se aplicó el cifrado a la bandera.
    
Identificación de la Vulnerabilidad

El error crítico de seguridad (el "leak") reside en la exposición de la variable **b** en el archivo `message.txt`.

En un intercambio Diffie-Hellman estándar:

1. **a y b** son llaves privadas que nunca deben compartirse.
    
2. **A y B** son llaves públicas calculadas como gprivada(modp).
    
3. El **Secreto Compartido** (S) se calcula como Ab(modp) o Ba(modp).
    

Al filtrarse b, cualquier atacante puede calcular el secreto compartido S usando la llave pública A del servidor.
## Proceso de Explotación y Resolución

### Paso 1: Reconstrucción del Secreto

Utilizando la función de potencia modular de Python, calculamos el valor de `shared`:

shared=Ab(modp)

### Paso 2: Derivación de la Llave Simétrica

El código original define la llave de cifrado como el último byte del secreto compartido: `key = shared % 256`

### Paso 3: Reversión del Cifrado XOR

El cifrado utilizado es un **XOR (OR exclusivo)**. Una propiedad fundamental del XOR es que es su propia inversa:

- Si Texto⊕Llave=Cifrado
    
- Entonces Cifrado⊕Llave=Texto
    

Se aplicó la operación XOR a cada byte del valor hexadecimal `enc` usando la `key` calculada.
## **Referencias**
https://www.scaler.com/topics/xor-in-python/
https://realpython.com/ref/builtin-functions/pow/