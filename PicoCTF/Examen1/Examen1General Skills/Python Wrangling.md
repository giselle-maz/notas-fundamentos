
## [Python Wrangling](https://play.picoctf.org/practice/challenge/166)
## SOLUCIÓN

El reto nos proporciona tres archivos: un script de Python (`ende.py`), un archivo de texto con una contraseña (`password.txt`) y un archivo encriptado que contiene la bandera (`flag.txt.en`). El objetivo es utilizar el script para desencriptar el archivo usando la llave proporcionada.

1. **Obtener los archivos:** Si estamos en nuestra máquina local o en la terminal del juego, descargamos los archivos usando `wget` con los enlaces proporcionados en la descripción del reto:

    ```
    wget <enlace_a_ende.py>
    wget <enlace_a_password.txt>
    wget <enlace_a_flag.txt.en>
    ```

2. **Leer la contraseña:** Utilizamos el comando `cat` para leer el contenido del archivo de la contraseña. Copiamos esa cadena de texto:

    ```
    cat password.txt
    ```

3. **Entender el funcionamiento del script:** Si intentamos ejecutar el script directamente, este nos mostrará sus instrucciones de uso. Necesitamos indicarle si queremos encriptar (`-e`) o desencriptar (`-d`):

    ```
    python3 ende.py
    # Salida: Usage: ende.py (-e/-d) [file]
    ```

4. **Desencriptar la bandera:** Ejecutamos el script pasándole el argumento para desencriptar (`-d`) y el nombre del archivo objetivo (`flag.txt.en`).

    ```
    python3 ende.py -d flag.txt.en
    ```

    El script se pausará y nos pedirá que ingresemos la contraseña. Pegamos la cadena que copiamos en el paso 2 y presionamos Enter.

5. Al proporcionar la contraseña correcta, el script descifrará el archivo y nos imprimirá la bandera directamente en la consola. 

```
┌──(kali㉿kali)-[~/Desktop/Ex1]
└─$ python3 ende.py -d flag.txt.en
Please enter the password:720b6ad346f84cd483c60c7464dd95d4
picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}

```
## NOTAS ADICIONALES


## REFERENCIAS