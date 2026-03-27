## **Descripcion**
We intercepted a suspicious file from a system, but instead of the password itself, it only contains its SHA-1 hash. Using OSINT techniques, you are provided with personal details about the target. Your task is to leverage this information to generate a custom password list and recover the original password by matching its hash.Download the following files:[userinfo](https://challenge-files.picoctf.net/c_plain_mesa/3c16fb8e48ddae444f6840e81660a5a8cb2d30b69092b04f619d6ac34676a919/userinfo.txt): Contains the personal details.[hash](https://challenge-files.picoctf.net/c_plain_mesa/3c16fb8e48ddae444f6840e81660a5a8cb2d30b69092b04f619d6ac34676a919/hash.txt): Contains the SHA-1 hash of the password.[check_password](https://challenge-files.picoctf.net/c_plain_mesa/3c16fb8e48ddae444f6840e81660a5a8cb2d30b69092b04f619d6ac34676a919/check_password.py): Script to test passwords against the hash.

## **Solucion**
picoCTF{Aj_15901990}
## **Notas adicionales**

### Paso 1. 
Se utilizó la herramienta **CUPP** en modo interactivo (`-i`). Se ingresaron los nombres de Alice, su pareja (Bob), su hijo (Charlie) y su fecha de nacimiento.
    cd cupp python3 cupp.py -i
### Paso 2
 Se activaron las opciones de **Leet mode**, caracteres especiales y números al final para cubrir variaciones comunes de contraseñas.
### Paso 3	
Se renombró el archivo resultante a `passwords.txt` y se ejecutó el script `check_password.py`. El script calculó el hash SHA-1 para cada entrada hasta encontrar la coincidencia.
    mv alice.txt ../passwords.txt cd ..
## **Referencias**
https://github.com/Mebus/cupp