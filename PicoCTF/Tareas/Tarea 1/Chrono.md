### Descripción
How to automate tasks to run at intervals on linux servers?Use ssh to connect to this server:

```
Server: saturn.picoctf.net
Port: 64393
Username: picoplayer 
Password: kZx-HVJKu8
```
### Solución
### Solución 1 - Python
```
giselle_maz-picoctf@webshell:~$ ssh -p 64393 saturn.picoctf.net -l picoplayer
The authenticity of host '[saturn.picoctf.net]:64393 ([13.59.203.175]:64393)' can't be established.
ED25519 key fingerprint is SHA256:dMTscRrUiURy7uMu5eGWwEKdd2FzqLzx6LfWhssWnNQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:64393' (ED25519) to the list of known hosts.
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

picoplayer@challenge:~$ cd etc
-bash: cd: etc: No such file or directory
picoplayer@challenge:~$ cd /etc
picoplayer@challenge:/etc$ ls -la | grep "cron"
drwxr-xr-x 1 root   root       26 Aug  4  2023 cron.d
drwxr-xr-x 1 root   root       26 Aug  4  2023 cron.daily
drwxr-xr-x 2 root   root       26 Aug  4  2023 cron.hourly
drwxr-xr-x 2 root   root       26 Aug  4  2023 cron.monthly
drwxr-xr-x 2 root   root       26 Aug  4  2023 cron.weekly
-rw-r--r-- 1 root   root       43 Aug  4  2023 crontab
picoplayer@challenge:/etc$ cat crontab
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_5b7059d0}
```
### Notas adicionales 
 picoCTF{Sch3DUL7NG_T45K3_L1NUX_5b7059d0}
### Referencias