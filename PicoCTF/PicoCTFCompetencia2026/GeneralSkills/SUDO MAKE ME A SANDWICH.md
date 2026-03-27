### [SUDO MAKE ME A SANDWICH](https://play.picoctf.org/events/79/challenges?category=5&page=1)

### DESCRIPCIÓN

Can you read the flag? I think you can! `ssh -p 63725 ctf-player@green-hill.picoctf.net` using password `f7e73aca`
### SOLUCIÓN

El reto consiste en una vulnerabilidad de Escalación de Privilegios mediante una configuración insegura en el archivo sudoers.

#### 1. Enumeración de privilegios:
Tras conectarnos por SSH, lo primero que hicimos fue verificar qué comandos puede ejecutar nuestro usuario con privilegios de superusuario sin conocer la contraseña de root:

```
ctf-player@challenge:~$ sudo -l
El resultado mostró la siguiente línea:
(ALL) NOPASSWD: /bin/emacs
```

Esto indica que el usuario ctf-player puede ejecutar el editor de texto Emacs como root sin necesidad de proporcionar una contraseña.
#### 2. Explotación del binario (Abusing Sudo):
Aunque intentamos leer la flag directamente con sudo cat flag.txt, el sistema lo rechazó porque el permiso de sudo estaba restringido específicamente al binario de Emacs.

Dado que Emacs tiene la capacidad de abrir cualquier archivo del sistema (si se ejecuta con los permisos adecuados), utilizamos el siguiente comando para abrir el archivo protegido:

```
sudo emacs flag.txt
```

Al ejecutarse como root, Emacs cargó el contenido del archivo saltándose las restricciones de lectura del usuario estándar.
#### 3. Obtención de la flag:
Dentro de la interfaz del editor, se visualizó el contenido:
### NOTAS ADICIONALES


### REFERENCIAS