### Descripción
We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/capture.pcap) and [key](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/picopico.key). Recover the flag.
### Solución
### Solución 1 - wireshark
```
con wireshar, cargo la llave y el archivo:
Edit - Preferences - Protocols - TLS
pongo la llave en RSA Keys list en la columna de key
luego hago clic derecho en cualquier paquete http, follor y HTTP Stream y me arroja la llave entre la info.


picoCTF{nongshim.shrimp.crackers}
```
### Notas adicionales 
picoCTF{nongshim.shrimp.crackers}
### Referencias