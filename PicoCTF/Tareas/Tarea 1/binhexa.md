### Descripción
How well can you perfom basic binary operations?Start searching for the flag here `nc titan.picoctf.net 61543`
### Solución
### Solución 1 -  Python
nos conectamos con el comando que proporciona y resolvemos las operaciones.
```
giselle_maz-picoctf@webshell:~$ nc titan.picoctf.net 61543

Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 00110010
Binary Number 2: 10011010


Question 1/6:
Operation 1: '>>'
Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 01001101
Correct!

Question 2/6:
Operation 2: '|'
Perform the operation on Binary Number 1&2.
Enter the binary result: 10111010
Correct!

Question 3/6:
Operation 3: '+'
Perform the operation on Binary Number 1&2.
Enter the binary result: 11001100
Correct!

Question 4/6:
Operation 4: '*'
Perform the operation on Binary Number 1&2.
Enter the binary result: 1111000010100
Correct!

Question 5/6:
Operation 5: '&'
Perform the operation on Binary Number 1&2.
Enter the binary result: 00010010
Correct!

Question 6/6:
Operation 6: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 

Enter the results of the last operation in hexadecimal: 64   

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_d9a7ddd2}
```
### Notas adicionales 
picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_d9a7ddd2}

### Referencias
