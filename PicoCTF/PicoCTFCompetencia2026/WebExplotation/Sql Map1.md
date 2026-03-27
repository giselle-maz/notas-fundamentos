## **Descripcion**
You’ve been hired by a shadowy group of pentesters who love a good puzzle. The system looks ordinary, but appearances lie. Somewhere inside, sloppy code and legacy hashing practices left a tiny, perfect doorway for an attacker.Your mission — should you choose to accept it — is to slip through that doorway, act as a legit user and retrieve the secret flag.Login [here](http://lonely-island.picoctf.net:61464/) and find the flag!

## **Solucion**
picoCTF{F0uNd_s3cr3T_K3y_f0R_w3_<>}
## **Notas adicionales**
#### Paso 1

Se identificó que el parámetro `q` en la URL (`/vuln.php?q=`) no sanitizaba las entradas, permitiendo una inyección de tipo **UNION**. Tras probar el número de columnas con `' UNION SELECT 1, 2--`, se procedió a extraer la información de la tabla de usuarios.

**Payload utilizado:** `' UNION SELECT username, password FROM users--`

#### Paso 2

La inyección devolvió una lista de usuarios y sus respectivos hashes. Se identificó el objetivo principal:

- **Usuario:** `ctf-player`
    
- **Hash (MD5):** `7a67ab5872843b22b5e14511867c4e43`
    

_(Nota: Aunque la tabla mostraba banderas como señuelos, estas eran falsas ya que contenían el texto "not_flag")._

#### Paso 3

Dado que el hash tiene una longitud de 32 caracteres y el reto mencionaba "legacy hashing", se confirmó que era **MD5**. Se utilizó la herramienta **CrackStation** para realizar un ataque de diccionario inverso.

- **Hash:** `7a67ab5872843b22b5e14511867c4e43`
    
- **Resultado (Password):** `picoCTF` (o la palabra específica que te haya devuelto).
    
### Paso 4

Al ingresar en el formulario de login con las credenciales obtenidas:
- **Login:** `ctf-player`
- **Password:** `[Contraseña_dada en crackstation]`

# **Referencias**
https://crackstation.net/
https://www.w3schools.com/sql/sql_injection.asp


