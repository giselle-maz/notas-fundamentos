### Descripción
The factory is hiding things from all of its users.Can you login as Joe and find what they've been looking at? http://fickle-tempest.picoctf.net:64564
### Solución
### Solución 1 - cookie editor
```
al intentar hacer log in descubrimos que no es mediante joe, si no con cualquier otro. pero al ingresar no muestra la bandera. Entonces, inspeccionamos networking y encontramos las cookies usadas, descubrimos que esta el usario contraseña y permisos de admin, este ultimo en false, usamos la extension de chroome "cookie editor" y cabiamos ese valor por true. recargamos y nos da la bandera

**Flag**: `picoCTF{th3_c0nsp1r4cy_l1v3s_4d184b0d}`
```
### Notas adicionales 
picoCTF{th3_c0nsp1r4cy_l1v3s_4d184b0d}
### Referencias