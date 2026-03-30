# 6 - Secret of the Polyglot

## Descripcion

The Network Operations Center (NOC) of your local institution picked up a
suspicious file, they're getting conflicting information on what type of file
it is. They've brought you in as an external expert to examine the file. Can
you extract all the information from this strange file?
Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/7/flag2of2-final.pdf).

## Solucion

abrimos el pdf y visualizamos parte de la flag:

1n_pn9_&_pdf_53b741d6}

vemos tipo de archivo

┌`──(xrengariox㉿PC)-[~/ex1/4]
└─$ wget -q [https://artifacts.picoctf.net/c_titan/7/flag2of2-final.pdf](https://artifacts.picoctf.net/c_titan/7/flag2of2-final.pdf)`

`┌──(xrengariox㉿PC)-[~/ex1/4]
└─$ file flag2of2-final.pdf
flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced`

convertimos a png

`┌──(xrengariox㉿PC)-[~/ex1/4]
└─$ mv flag2of2-final.pdf flag_parte1.png`

acemos un cat

`┌──(xrengariox㉿PC)-[~/ex1/4]
└─$ cat flag_parte1.png
───────┬──────────────────────────────────────────────────────
│ File: flag_parte1.png   <BINARY>
───────┴──────────────────────────────────────────────────────`

instalamos esta herramienta para convertir los colores de una imagen en caracteres de colores de la terminal (ANSI)

`┌──(xrengariox㉿PC)-[~/ex1/4]
└─$ sudo apt install catimg
catimg flag_parte1.png`

esto muestra una “imagen” con la primera parte de la flag

┌──(xrengariox㉿PC)-[~/ex1/4]
└─$

## Notas Adicionales

picoCTF{f1u3n7_1n_pn9_&_pdf_53b741d6}

## Referencias