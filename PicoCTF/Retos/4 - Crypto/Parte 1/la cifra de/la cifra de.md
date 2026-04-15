### Descripción
I found this cipher in an old book.Can you figure out what it says? Connect with nc fickle-tempest.picoctf.net 59571.
### Solución
```
@webshell:~$ nc fickle-tempest.picoctf.net 60772
Encrypted message:
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3ximdI91f3}

Ehk ktryy herq-ooizxetypd jjdcxnatoty ol f aordllvmlbkytc inahkw socjgex, bls sfoe gwzuti 1467 my Rjzn Hfetoxea Gqmexyt.

Tnj Gimjyèrk Htpnjc iy ysexjqoxj dosjeisjd cgqwej yse Gqmexyt Doxn ox Fwbkwei Inahkw.

Tn 1508, Ptsatsps Zwttnjxiax tnbjytki ehk xz-cgqwej ylbaql rkhea (g rltxni ol xsilypd gqahggpty) ysaz bzuri wazjc bk f nroytcgq nosuznkse ol yse Bnretèwp Cousex.

Gplrfdo’y xpcuso butvlky lpvjlrki tn 1555 gx l cuseitzltoty ol yse lncsz. Yse rthex mllbjd ol yse gqahggpty fce tth snnqtki cemzwaxqj, bay ehk fwpnfmezx lnj yse osoed qptzjcs gwp mocpd hd xegsd ol f xnkrznoh vee usrgxp, wnnnh ify bk itfljcety hizm paim noxwpsvtydkse.

 decifrar: hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3ximdI91f3} hasta encontrarla 
 giselle_maz-picoctf@webshell:~$ python3 -c "
> cifrado = 'hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3ximdI91f3}'
> llave = 'SOLVECRYPTO'
> resultado = ''
> llave_index = 0
> for char in cifrado:
>     if char.isalpha():
>         offset = ord('A') if char.isupper() else ord('a')
>         k_char = llave[llave_index % len(llave)].upper()
>         k_off = ord(k_char) - ord('A')
>         descifrado = chr((ord(char) - offset - k_off + 26) % 26 + offset)
>         resultado += descifrado
>         llave_index += 1
>     else:
>         resultado += char
> print('Tu bandera es:', resultado)
> "
Tu bandera es: psfvlmqbNGW{u311m50_0m_f1nl3g3_j1lo3jqysN91b3}
giselle_maz-picoctf@webshell:~$ python3 -c "
> cifrado = 'hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3ximdI91f3}'
> llave = 'SQUIRREL'
> resultado = ''
> llave_index = 0
> for char in cifrado:
>     if char.isalpha():
>         offset = ord('A') if char.isupper() else ord('a')
>         k_char = llave[llave_index % len(llave)].upper()
>         k_off = ord(k_char) - ord('A')
>         descifrado = chr((ord(char) - offset - k_off + 26) % 26 + offset)
>         resultado += descifrado
>         llave_index += 1
>     else:
>         resultado += char
> print('Tu bandera es:', resultado)
> "
Tu bandera es: pqwiyxdoKJQ{e311j50_0g_w1gv3h3_n1sq3geblS91l3}
giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ python3 -c "
> cifrado = 'hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3ximdI91f3}'
> llave = 'scout'
> resultado = ''
> llave_index = 0
> for char in cifrado:
>     if char.isalpha():
>         offset = ord('A') if char.isupper() else ord('a')
>         # Usamos la llave en minúsculas para calcular el desplazamiento
>         k_char = llave[llave_index % len(llave)].lower()
>         k_off = ord(k_char) - ord('a')
>         # Desciframos restando el desplazamiento
>         descifrado = chr((ord(char) - offset - k_off + 26) % 26 + offset)
>         resultado += descifrado
>         llave_index += 1
>     else:
>         resultado += char
> print('La bandera real es:', resultado)
> "
La bandera real es: pecwwwflIGS{k311m50_0d_h1zl3j3_n1hp3vuskQ91d3}
giselle_maz-picoctf@webshell:~$ python3 -c "
> cifrado = 'hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3ximdI91f3}'
> # Sabemos que las primeras 7 letras deben ser 'picoCTF'
> real_start = 'picoCTF'
> llave = ''
> 
> # Calculamos la llave letra por letra
> for i in range(len(real_start)):
>     diff = (ord(cifrado[i].lower()) - ord(real_start[i].lower()) + 26) % 26
>     llave += chr(diff + ord('a'))
> 
> print(f'Llave detectada: {llave}')
> 
> # Ahora desciframos todo con esa llave
> resultado = ''
> for i in range(len(cifrado)):
>     if cifrado[i].isalpha():
>         offset = ord('A') if cifrado[i].isupper() else ord('a')
>         k_off = ord(llave[i % len(llave)]) - ord('a')
>         res_char = chr((ord(cifrado[i]) - offset - k_off + 26) % 26 + offset)
>         resultado += res_char
>     else:
>         resultado += cifrado[i]
> print('Bandera:', resultado)
> "
Llave detectada: syocnvc
Bandera: picoctfhELI{r311m50_0f_m1es3f3_f1ff3zukqN91h3}
giselle_maz-picoctf@webshell:~$ 


```
### Notas adicionales 

### Referencias
