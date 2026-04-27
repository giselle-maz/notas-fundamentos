### Descripción
This service provides you an encrypted flag. Can you decrypt it with just N & e?Connect to the program with netcat:`$ nc verbal-sleep.picoctf.net 53276`The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/b1999e70e98a4fb11d441bd4ef60a948c1ae4a27a3a7154ed2678990b91f52e4/encrypt.py).
### Solución
```

giselle_maz-picoctf@webshell:~/leak$ nc verbal-sleep.picoctf.net 53276
N: 22641736591898196020001528945685736821786038320165643579060676722778050919363835487755702470259320071388039503574355274318372601444679655046114013891336818
e: 65537
cyphertext: 9132916083281900683759978534177981672159767876414781117353383651831557784208337123609652624517870778468493655977398402727802777851448582676763753480146089

 luego debemos factorizar n para obtener p y q con factor db y creamos el codigo para encontrar la flag 
 n = 22641736591898196020001528945685736821786038320165643579060676722778050919363835487755702470259320071388039503574355274318372601444679655046114013891336818

e = 65537

c = 9132916083281900683759978534177981672159767876414781117353383651831557784208337123609652624517870778468493655977398402727802777851448582676763753480146089
# Los factores reales de tu N:
p = 2
q = n // 2
# 1. Calcular Phi correctamente
phi = (p - 1) * (q - 1)
# 2. Calcular d (Llave privada)
d = pow(e, -1, phi)
# 3. Descifrar el mensaje
m = pow(c, d, n)
# 4. Convertir a texto

hex_string = hex(m)[2:]

if len(hex_string) % 2 != 0:

    hex_string = '0' + hex_string
try:

    flag = bytes.fromhex(hex_string).decode('ascii')

    print(f"Tu Flag es: {flag}")

except:

    # Si no es ascii puro, intentamos ver el hex

    print(f"Resultado en hex: {hex_string}")

 [Running] python -u "c:\Users\Giselle MO\Documents\S26\FUN_SEG_INF\giselle_maz\PicoCTF\Tareas\Tarea 4\3 - EVEN RSA CAN BE BROKEN\sol.py"

Tu Flag es: picoCTF{tw0_1$_pr!m305af7255}
```
### Notas adicionales 
picoCTF{tw0_1$_pr!m305af7255}
### Referencias