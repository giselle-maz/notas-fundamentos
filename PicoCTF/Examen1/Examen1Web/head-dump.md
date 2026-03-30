# head-dump

## Descripcion

Welcome to the 
challenge! In this challenge, you will explore a web application and 
find an endpoint that exposes a file containing a hidden flag.
The application is a simple blog website where 
you can read articles about various topics, including an article about 
API Documentation. Your goal is to explore the application and find the 
endpoint that generates files holding the server’s memory, where a 
secret flag is hidden.
The website is running [picoCTF News](http://verbal-sleep.picoctf.net:54241/).

## Solucion

Inspeccionar el sitio hasta encontrar algo relacionado con `heapdump`

y encontramos el **CSS de Swagger UI,** entonces hacemos un grep para encontrar la bandera

```jsx
giselle_maz-picoctf@webshell:~$ curl [http://verbal-sleep.picoctf.net:52219/heapdump](http://verbal-sleep.picoctf.net:52219/heapdump) | grep -o "picoCTF{[^}]*}"
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
Dload  Upload   Total   Spent    Left  Speed
39 10.8M   39 4388k    0     0  1360k      0  0:00:08  0:00:03  0:00:05 1360kpicoCTF{Pat!3nt_15_Th3_K3y_8df117c1}
```

## Nots adicionales

picoCTF{Pat!3nt_15_Th3_K3y_8df117c1}

## Referencias