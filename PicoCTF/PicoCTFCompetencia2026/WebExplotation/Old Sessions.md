## **Descripcion**
Proper session timeout controls are critical for securing user accounts. If a user logs in on a public or shared computer but doesn’t explicitly log out (instead simply closing the browser tab), and session expiration dates are misconfigured, the session may remain active indefinitely.This then allows an attacker using the same browser later to access the user’s account without needing credentials, exploiting the fact that sessions never expire and remain authenticated.Your friend tells you to check out a new social media platform he built a few years ago. Although its still under development, he said the site is almost complete. He also mentioned that he hates constantly logging into sites, and so has made his page that 'once you login, you never have to log-out again'!Browse [here](http://dolphin-cove.picoctf.net:52800/), and find the flag!
## **Solucion**
picoCTF{s3t_s3ss10n_3xp1rat10n5_77b6684a}
## **Notas adicionales**
#### Paso 1

Tras registrar un usuario de prueba y navegar por el sitio, se accedió a la ruta

En esta página se encontró una tabla con los identificadores de sesión (Session IDs) de todos los usuarios conectados, incluyendo el del usuario **admin**.

#### Paso 2

Se identificó y copió el ID de sesión asociado al administrador:
    
#### Paso 3

Utilizando la extensión **Cookie Editor** en Firefox, se procedió a interceptar la identidad del administrador:

1. Se abrió la extensión mientras se estaba en la página del reto.
    
2. Se localizó la cookie de nombre `session`.
    
3. Se reemplazó el valor original (del usuario de prueba) por el **Session ID del admin** copiado previamente.
    
4. Se guardaron los cambios y se refrescó la página (`F5`).
    

### Paso 4

Al refrescar el navegador, el servidor reconoció la "llave" del administrador. La interfaz cambió para mostrar el perfil de administrador, revelando la bandera.
