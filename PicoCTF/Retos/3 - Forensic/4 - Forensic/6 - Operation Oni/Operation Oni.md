### Descripción
Download this disk image, find the key and log into the remote machine.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download disk image](https://artifacts.picoctf.net/c/70/disk.img.gz)
- Remote machine: `ssh -i key_file -p 50930 ctf-player@saturn.picoctf.net`
### Solución
### Solución 1 - 
```
giselle_maz-picoctf@webshell:/tmp$ 
giselle_maz-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/70/disk.img.gz
--2026-03-25 19:43:26--  https://artifacts.picoctf.net/c/70/disk.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.18, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 48132743 (46M) [application/octet-stream]
Saving to: 'disk.img.gz'

disk.img.gz            100%[=========================>]  45.90M  1.82MB/s    in 25s     

2026-03-25 19:43:51 (1.82 MB/s) - 'disk.img.gz' saved [48132743/48132743]

giselle_maz-picoctf@webshell:/tmp$ gunzip -f disk.img.gz
giselle_maz-picoctf@webshell:/tmp$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
giselle_maz-picoctf@webshell:/tmp$ fls -r -o 206848 disk.img | grep -E "ssh|id_rsa|key"
+ d/d 33:       keymap
++ r/r 2147:    sshd
++ d/d 44:      keys
+++ l/l 54:     sshd
+++ r/r 907:    cryptkey.files
+++ r/r 922:    keymap.files
++ r/r 554:     save-keymaps
++ r/r 2148:    sshd
+ d/d 14:       ssh
++ r/r 15:      ssh_host_ed25519_key
++ r/r 16:      ssh_host_ed25519_key.pub
++ r/r 17:      ssh_host_ecdsa_key
++ r/r 18:      ssh_host_ecdsa_key.pub
++ r/r 19:      ssh_host_dsa_key
++ r/r 20:      ssh_host_dsa_key.pub
++ r/r 21:      ssh_host_rsa_key
++ r/r 22:      ssh_host_rsa_key.pub
++ r/r 2136:    ssh_config
++ r/r 2149:    sshd_config
+++++ r/r 1050: keywrap.ko
+++++++ r/r 1202:       hyperv-keyboard.ko
++++++ r/r 1213:        dm-flakey.ko
+++++ d/d 2048: key
++++++ r/r 1691:        af_key.ko
++++++ r/r 1884:        act_tunnel_key.ko
+++++ d/d 2066: keys
++++++ d/d 2067:        encrypted-keys
+++++++ r/r 2068:       encrypted-keys.ko
++ l/l 355:     showkey
++ r/r 2084:    ssh-keygen
++ r/- * 0:     ssh-copy-id
++ r/- * 0:     ssh-keyscan
++ r/- * 0:     ssh-pkcs11-helper
++ r/r 2140:    ssh-add
++ r/r 2145:    ssh
++ r/r 2193:    keytab-lilo
++ r/r 2144:    ssh-pkcs11-helper
++ r/r 2143:    ssh-keyscan
++ r/r 2142:    ssh-copy-id
++ l/l 346:     setkeycodes
++ r/r 2141:    ssh-agent
++ r/r 2150:    sshd
+++++ r/r 676:  sshd
+++ d/d 787:    keys
++ d/d 3907:    ssh
+++ r/r 2152:   ssh-sk-helper
+++ r/r 2151:   ssh-pkcs11-helper
+ r/r 707:      setup-keymap
+ r/r 712:      setup-sshd
+ d/d 3916:     .ssh
giselle_maz-picoctf@webshell:/tmp$ fls -r -o 206848 disk.img 3916
r/r 2345:       id_ed25519
r/r 2346:       id_ed25519.pub
giselle_maz-picoctf@webshell:/tmp$ icat -o 206848 disk.img 2345 > key_file
giselle_maz-picoctf@webshell:/tmp$ chmod 600 key_file
giselle_maz-picoctf@webshell:/tmp$ ssh -i key_file -p 50930 ctf-player@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:50930 ([13.59.203.175]:50930)' can't be established.
ED25519 key fingerprint is SHA256:XBSvB1lk28EctsAVdKJtsl0A7C5bonqPrvHCYH8aEy4.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:50930' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.8.0-1047-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$ cat flag.txt
picoCTF{k3y_5l3u7h_b5066e83}
```
### Notas adicionales 
picoCTF{k3y_5l3u7h_b5066e83}
### Referencias
