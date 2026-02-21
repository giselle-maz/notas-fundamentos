### Descripción
I accidentally wrote the flag down. Good thing I deleted it!You download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/139/challenge.zip)
### Solución
### Solución 1 - Python
```
giselle_maz-picoctf@webshell:~$ wget -q https://artifacts.picoctf.net/c_titan/139/challenge.zip
giselle_maz-picoctf@webshell:~$ unzip challenge.zip 
Archive:  challenge.zip
   creating: drop-in/
   creating: drop-in/.git/
   creating: drop-in/.git/branches/
  inflating: drop-in/.git/description  
   creating: drop-in/.git/hooks/
  inflating: drop-in/.git/hooks/applypatch-msg.sample  
  inflating: drop-in/.git/hooks/commit-msg.sample  
  inflating: drop-in/.git/hooks/fsmonitor-watchman.sample  
  inflating: drop-in/.git/hooks/post-update.sample  
  inflating: drop-in/.git/hooks/pre-applypatch.sample  
  inflating: drop-in/.git/hooks/pre-commit.sample  
  inflating: drop-in/.git/hooks/pre-merge-commit.sample  
  inflating: drop-in/.git/hooks/pre-push.sample  
  inflating: drop-in/.git/hooks/pre-rebase.sample  
  inflating: drop-in/.git/hooks/pre-receive.sample  
  inflating: drop-in/.git/hooks/prepare-commit-msg.sample  
  inflating: drop-in/.git/hooks/update.sample  
   creating: drop-in/.git/info/
  inflating: drop-in/.git/info/exclude  
   creating: drop-in/.git/refs/
   creating: drop-in/.git/refs/heads/
 extracting: drop-in/.git/refs/heads/master  
   creating: drop-in/.git/refs/tags/
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
   creating: drop-in/.git/objects/
   creating: drop-in/.git/objects/pack/
   creating: drop-in/.git/objects/info/
   creating: drop-in/.git/objects/3a/
 extracting: drop-in/.git/objects/3a/71673f161f71dcf7758fc0a5844b126aad4daf  
   creating: drop-in/.git/objects/8a/
 extracting: drop-in/.git/objects/8a/b26439d85fcc8b4405ecc16f78141767b3f743  
   creating: drop-in/.git/objects/7d/
 extracting: drop-in/.git/objects/7d/3aa557ff7ba7d116badaf5307761efb3622249  
   creating: drop-in/.git/objects/d5/
 extracting: drop-in/.git/objects/d5/52d1ecd2d83fa2e65b6724d1ff73b45a7d59b7  
   creating: drop-in/.git/objects/0c/
 extracting: drop-in/.git/objects/0c/1ab266b7a3a1cd099bb509f82b7a2d03aecd03  
   creating: drop-in/.git/objects/14/
 extracting: drop-in/.git/objects/14/4fdc44b09058d7ea7f224121dfa5babadddbb9  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
   creating: drop-in/.git/logs/
  inflating: drop-in/.git/logs/HEAD  
   creating: drop-in/.git/logs/refs/
   creating: drop-in/.git/logs/refs/heads/
  inflating: drop-in/.git/logs/refs/heads/master  
 extracting: drop-in/message.txt     
giselle_maz-picoctf@webshell:~$ cd drop-in
giselle_maz-picoctf@webshell:~/drop-in$ ls
message.txt
giselle_maz-picoctf@webshell:~/drop-in$ git status
On branch master
nothing to commit, working tree clean
giselle_maz-picoctf@webshell:~/drop-in$ git log

giselle_maz-picoctf@webshell:~/drop-in$ git show <7d3aa557ff7ba7d116badaf5307761efb3622249>
-bash: syntax error near unexpected token `newline'
giselle_maz-picoctf@webshell:~/drop-in$ git log

giselle_maz-picoctf@webshell:~/drop-in$ git show <7d3aa557ff7ba7d116badaf5307761efb3622249>:message.txt
-bash: 7d3aa557ff7ba7d116badaf5307761efb3622249: No such file or directory
giselle_maz-picoctf@webshell:~/drop-in$ ^C
giselle_maz-picoctf@webshell:~/drop-in$ git show 7d3aa557ff7ba7d116badaf5307761efb362224
9:message.txt



de aqui tomamos el num de commit 
commit 144fdc44b09058d7ea7f224121dfa5babadddbb9 (HEAD, master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:25 2024 +0000

    remove sensitive info

commit 7d3aa557ff7ba7d116badaf5307761efb3622249
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:25 2024 +0000

    create flag

```
### Notas adicionales 
picoCTF{s@n1t1z3_be3dd3da}
### Referencias