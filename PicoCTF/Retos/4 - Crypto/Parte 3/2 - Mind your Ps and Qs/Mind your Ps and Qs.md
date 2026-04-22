### Descripción
In RSA, a small e value can be problematic, but what about N? Can you decrypt this?[values](https://challenge-files.picoctf.net/c_wily_courier/4540a62876bdb4e341c70e3300408ced0ae02e4d27bb41b747a80f42aef919ba/values)
### Solución
```
al ser n muy corta podemos factorizar para sacar p y q, lo haremos con https://factordb.com/index.php?query=948406957756830799684818171639547165784816468744946013083947881743680617123566349

hacemos este programa 
from gmpy2 import iroot
import gmpy2

c= 15341890103764929939105506004034128738090325640037083301857608662849501626260517
n= 948406957756830799684818171639547165784816468744946013083947881743680617123566349
e= 65537

#factorizando n
p=1891771437429478964908181306574287207137
q=501332739776173570344039681219489434626477
 
tn=(p-1)*(q-1)
d=pow(e,-1,tn)
m=pow(c,d,n)

flag=bytes.fromhex('0'+hex(m)[2:])

print(f"flag : {flag[::-1]}")

obtenemos
[Running] python -u "c:\Users\Giselle MO\Documents\S26\FUN_SEG_INF\giselle_maz\PicoCTF\Retos\4 - Crypto\Parte 3\2 - Mind your Ps and Qs\Mind.py"

flag : b'picoCTF{sma11_N_n0_g0od_1dc7ae91}\n'
```
### Notas adicionales 
picoCTF{sma11_N_n0_g0od_1dc7ae91}
### Referencias
