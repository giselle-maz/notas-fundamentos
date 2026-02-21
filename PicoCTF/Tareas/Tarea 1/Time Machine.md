### Descripción
What was I last working on? I remember writing a note to help me remember...You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/68/challenge.zip)
### Solución
### Solución 1 - Python
```
giselle_maz-picoctf@webshell:~/drop-in$ wget -q https://artifacts.picoctf.net/c_titan/68/challenge.zip
giselle_maz-picoctf@webshell:~/drop-in$ ls
challenge.zip  drop-in
giselle_maz-picoctf@webshell:~/drop-in$ unzip challenge.zip
Archive:  challenge.zip
replace drop-in/message.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
  inflating: drop-in/message.txt     
  inflating: drop-in/.git/description  
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
  inflating: drop-in/.git/info/exclude  
 extracting: drop-in/.git/refs/heads/master  
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
 extracting: drop-in/.git/objects/43/246218ab4fc7b30e9a9dff073e012316851469  
 extracting: drop-in/.git/objects/25/16effb8d70e33bdd0023629b164a77225e1ec2  
 extracting: drop-in/.git/objects/70/5ff639b7846418603a3272ab54536e01e3dc43  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
  inflating: drop-in/.git/logs/HEAD  
  inflating: drop-in/.git/logs/refs/heads/master  
giselle_maz-picoctf@webshell:~/drop-in$ cat drop-in/message.txt
This is what I was working on, but I'd need to look at my commit history to know why...giselle_maz-picoctf@webshell:~/drop-in$ cat message.txt
cat: message.txt: No such file or directory
giselle_maz-picoctf@webshell:~/drop-in$ cd
giselle_maz-picoctf@webshell:~$ ls
Addadshashanammu  README.txt  drop-in  files  home
giselle_maz-picoctf@webshell:~$ cd drop-in
giselle_maz-picoctf@webshell:~/drop-in$ git log
giselle_maz-picoctf@webshell:~/drop-in$ 


commit 705ff639b7846418603a3272ab54536e01e3dc43 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:36 2024 +0000

    picoCTF{t1m3m@ch1n3_b476ca06}
```
### Notas adicionales 
picoCTF{t1m3m@ch1n3_b476ca06}
### Referencias