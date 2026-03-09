### Descripción
We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/134d2a2cf6ec5b7e757effc9b32977af7cc324b8e99a5ddb64737794a14dc18d/capture.pcap). Recover the flag.
### Solución
### Solución 1 - kali
```
└─$ wget -q https://challenge-files.picoctf.net/c_fickle_tempest/134d2a2cf6ec5b7e757effc9b32977af7cc324b8e99a5ddb64737794a14dc18d/capture.pcap
                                                                                                
┌──(kali㉿kali)-[~]
└─$ file capture.pcap
capture.pcap: pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 262144)

abrimos archivo con wireshark capture.pcap &
seleccionamos un paquete udp, clic derecho y follow udp stream y en la pestaña 6 esta la flag

└─$ wireshark capture.pcap &
[2] 100393

```
### Notas adicionales 
picoCTF{StaT31355_636f6e6e}
### Referencias