### Descripción
There is some interesting information hidden around this site. Can you find it? http://wily-courier.picoctf.net:55295/
### Solución
### Solución 1 - Python
```
codigo fuente = primera parte

<!-- Here's the first part of the flag: picoCTF{t -->

hoja de estilos
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */

robots.txt
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?

http://wily-courier.picoctf.net:55295/.htaccess
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.

http://wily-courier.picoctf.net:55295/.DS_Store

Congrats! You've completed the scavenger hunt! Part 5: _9588550}
```
### Notas adicionales 
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}
### Referencias
https://en.wikipedia.org/wiki/.DS_Store