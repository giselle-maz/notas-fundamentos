### Descripción
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?Access the server using `nc verbal-sleep.picoctf.net 54133`
### Solución
```
nos conectamos
giselle_maz-picoctf@webshell:~$ nc verbal-sleep.picoctf.net 54133
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: 
copimos el hash, pero en la shell de pico no se puede resolver, y mi entorno virtual de kali por el momento no funciona, entonces usmos una pagina que nos da le hash decifrado:
https://crackstation.net/
de ahi vemos que debemos decifrar varias hash para llegar a  la falg.


giselle_maz-picoctf@webshell:~$ nc verbal-sleep.picoctf.net 52702
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: password123
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: letmein
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: qwerty098
Correct! You've cracked the SHA-256 hash with a secret found. 
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4c95d69f}
```
### Notas adicionales 

### Referencias