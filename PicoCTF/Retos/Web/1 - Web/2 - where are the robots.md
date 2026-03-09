### Descripción
Can you find the robots? http://fickle-tempest.picoctf.net:64363 
### Solución
### Solución 1 - Inspeccionar
```
vemos el archivo robot.txt
http://fickle-tempest.picoctf.net:64363/robots.txt

vemos archivos ocultos
User-agent: *
Disallow: /cc6b1.html

vamos a esa liga y encontramos flag
Guess you found the robots  
picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}
```
### Notas adicionales 
control + a -> seleccionar todo
picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}

Un archivo robots.txt indica a los rastreadores de los buscadores a qué URLs de tu sitio pueden acceder. Principalmente, se utiliza para evitar que las solicitudes que recibe tu sitio lo sobrecarguen; **no es un mecanismo para impedir que una página web aparezca en Google**. Si quieres que una página web no aparezca en Google, [bloquea la indexación con `noindex`](https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=es) o protege la página con una contraseña.
### Referencias
https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=es

http://fickle-tempest.picoctf.net:64363/robots.txt