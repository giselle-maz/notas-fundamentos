## **Descripcion**
Help us test the form by submiting the username as `test` and password as `test!`
## **Solucion**
picoCTF{proxies_all_the_way_be716d8e}

## **Notas adicionales**
Se hizo uso del programa de burp suite, se abrio el navegador , se coloco el enlace proporcionado
se mantuvo el intercept off,
hasta cuando se agrego los datos de usuario y contraseña de activo,
en eso dimos en forward dos veces en la primera nos da algo asi /next-page/id=bF90aGVfd2F5X2JlNzE2ZDhlfQ== , desde b en adelante seleccionalo y en el apartado de inspector seleciona de coded from base64 y saldra la primera parte de la bandera
vuelves a forward y has lo mismo y tendras la bandera completa..
