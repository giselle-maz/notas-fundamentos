### Descripción
This website can be rendered only by picobrowser, go and catch the flag!http://fickle-tempest.picoctf.net:60146
### Solución
### Solución 1 - consola
```
giselle_maz-picoctf@webshell:~$ curl is http://fickle-tempest.picoctf.net:60146/flag -H 'User-Agent: picobrowser' | grep pico
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0curl: (6) Could not resolve host: is
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2115  100  2115    0     0  30641      0 --:--:-- --:--:-- --:--:-- 31102
         <!-- <strong>Title</strong> --> picobrowser!
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{p1c0_s3cr3t_ag3nt_fba5c48f}</code></p>
```
### Notas adicionales 
picoCTF{p1c0_s3cr3t_ag3nt_fba5c48f}
### Referencias