## [SansAplha](https://play.picoctf.org/practice/challenge/436)

## Description

The Multiverse is within your grasp! Unfortunately, the server that contains the secrets of the multiverse is in a universe where keyboards only have numbers and (most) symbols.`ssh -p 59843 ctf-player@mimas.picoctf.net`Use password: `1db87a14`

## SOLUCIÓN

Identificamos que el reto nos sitúa en un entorno de shell restringido donde **no podemos escribir ninguna letra del alfabeto**. Cualquier intento de ingresar letras devuelve el error `Unknown character detected`. Para encontrar y leer la bandera, es necesario abusar de la expansión de comodines (_wildcards_ o _globbing_) de Bash usando únicamente símbolos y números.

- Primero, al enviar un simple asterisco `*`, forzamos al shell a evaluar el contenido del directorio actual. Descubrimos la existencia de un directorio llamado `blargh` gracias al mensaje de error devuelto:

```
SansAlpha$ *
bash: blargh: command not found
```

- Sabiendo que necesitamos un binario para leer archivos (ya que no podemos escribir comandos estándar como `cat`), apuntamos a `/bin/base64`, cuya ruta y nombre terminan en números, permitiéndonos representarlo con comodines.

- Al intentar la ruta `/???/????64`, Bash falló debido a una colisión: el patrón coincidía tanto con `/bin/base64` como con `/bin/x86_64`.

- Refinamos el comodín para forzar a Bash a que las primeras cuatro posiciones del nombre del programa **no fueran números**, usando la negación `[!0-9]`. Esto logró aislar con éxito el binario de Base64: `/*/[!0-9][!0-9][!0-9][!0-9]64`.

- Finalmente, le pasamos el archivo de la bandera como argumento usando el patrón `*/????????` (que coincide exactamente con la longitud de la ruta `blargh/flag.txt`). El comando final quedó así:

```
SansAlpha$ /*/[!0-9][!0-9][!0-9][!0-9]64 */????????
```

- Al ejecutarse, el shell tradujo silenciosamente esa línea a `/bin/base64 blargh/flag.txt`, devolviéndonos el contenido del archivo codificado en Base64: `cmV0dXJuIDAgcGljb0NURns3aDE1X211MTcxdjNyNTNfMTVfbTRkbjM1NV80OTQ1NjMwYX0=`

- Al decodificar esta cadena en nuestra máquina local, obtuvimos la bandera: `picoCTF{7h15_mu171v3r53_15_m4dn355_4945630a}`

### NOTAS ADICIONALES


### REFERENCIAS