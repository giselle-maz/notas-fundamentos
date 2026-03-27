### Descripción
We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/capture.pcap) and [key](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/picopico.key). Recover the flag.
### Solución
### Solución 1 - wireshark
```
con wireshar, cargo la llave y el archivo:
Edit - Preferences - Protocols - TLS
pongo la llave en RSA Keys list en la columna de key
luego hago clic derecho en cualquier paquete http, follor y HTTP Stream y me arroja la llave entre la info.

picoCTF{honey.roasted.peanuts}
```
### Notas adicionales 
picoCTF{honey.roasted.peanuts}
### Referencias