## [Specialer](https://play.picoctf.org/practice/challenge/378)

## DESCRIPCIÓN

Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.

`ssh -p 60618 ctf-player@saturn.picoctf.net`. The password is `483e80d4`

## SOLUCIÓN

Identificamos que el reto nos sitúa en un entorno de shell restringido (Restricted Shell), donde comandos básicos del sistema como `ls` o `cat` están deshabilitados. Para encontrar y leer la bandera, es necesario abusar de las funciones y comandos internos (_built-ins_) propios de Bash.

- Como no podemos usar `ls` para ver qué hay en el sistema, aprovechamos la expansión de comodines del shell (_bash globbing_). Al pasar asteriscos al comando `echo`, forzamos al shell a listar el contenido de los subdirectorios:

```
Specialer$ echo */*
abra/cadabra.txt abra/cadaniel.txt ala/kazam.txt ala/mode.txt sim/city.txt sim/salabim.txt
```

- Para leer el contenido, inicialmente probamos sustituciones de comandos erróneas como `echo $(abra/cadabra.txt)`, las cuales fallan devolviendo `Permission denied` porque el shell intenta ejecutar el texto plano.

- Corregimos la sintaxis utilizando la redirección de entrada `<` dentro de la sustitución de comandos. Esto le indica a Bash que lea internamente el archivo y se lo entregue al comando `echo`:

```
Specialer$ echo $(<abra/cadabra.txt)
Nothing up my sleeve!
Specialer$ echo $(<abra/cadaniel.txt)
Yes, I did it! I really did it! I'm a true wizard!
Specialer$ echo $(<sim/salabim.txt)
#He was so kind, such a gentleman tied to the oceanside#
Specialer$ echo $(<sim/city.txt)
05ed181c-4aa0-4d4a-8505-2fe6ca9097d3
Specialer$ echo $(<ala/mode.txt)
Yummy! Ice cream!
```

- Tras revisar los archivos devueltos, encontramos la bandera escondida dentro de `ala/kazam.txt`:

```
Specialer$ echo $(<ala/kazam.txt)
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_d5ef8b71}
```

picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_d5ef8b71}

### NOTAS ADICIONALES


### REFERENCIAS