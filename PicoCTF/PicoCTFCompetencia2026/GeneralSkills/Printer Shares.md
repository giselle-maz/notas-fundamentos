## **Descripcion**
Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server? The printer is on `52439`. you can try `$ nc -vz mysterious-sea.picoctf.net 52439`
## **Solucion**
Se hizo uso de la terminal
picoCTF{5mb_pr1nter_5h4re5_2f61915b}

## **Notas adicionales**
# Paso 1
Primero, comprobamos si el puerto del servidor estaba abierto usando netcat:
nc -vz mysterious-sea.picoctf.net 52439
# Paso 2
Listado de recursos compartidos SMB
Los indicios sugerían que esta impresora utilizaba el protocolo SMB. Usamos smbclient para enumerar los recursos compartidos:
smbclient -L //mysterious-sea.picoctf.net -p 52439-N
# Paso 3
Conéctate al Compartir Público
smbclient //mysterious-sea.picoctf.net/shares -p 52439-N

# Paso 4
Listar archivos en el recurso compartido
ls
# Paso 5
Descarga y lee la bandera
get flag.txt  
 exit
 cat flag.txt
## **Referencias**
https://es.wikipedia.org/wiki/Server_Message_Block