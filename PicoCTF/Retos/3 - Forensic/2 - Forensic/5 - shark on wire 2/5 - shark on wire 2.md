### Descripción
#### Description

We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/07bf5ee832c595a6de406476b6c07f164d2951fbcfcf9cf3739c25dea26e5f0b/capture.pcap). Recover the flag.
### Solución
### Solución 1 - shell
```
descragamos 
giselle_maz-picoctf@webshell:~$ wget -q https://challenge-files.picoctf.net/c_fickle_tempest/07bf5ee832c595a6de406476b6c07f164d2951fbcfcf9cf3739c25dea26e5f0b/capture.pcap



 hacemos la extraccion
 
giselle_maz-picoctf@webshell:~$ python3 -c "from scapy.all import rdpcap, UDP, IP; pkts = rdpcap('capture.pcap'); print(''.join([chr(p[UDP].sport - 5000) for p in pkts if IP in p and UDP in p and p[IP].src == '10.0.0.66' and p[UDP].dport == 22 and p[UDP].sport > 5000]))"
picoCTF{p1LLf3r3d_data_v1a_st3g0}
```
### Notas adicionales 
picoCTF{p1LLf3r3d_data_v1a_st3g0}
### Referencias