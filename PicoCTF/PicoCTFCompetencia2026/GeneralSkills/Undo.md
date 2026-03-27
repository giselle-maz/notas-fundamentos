## **Descripcion**
Can you reverse a series of Linux text transformations to recover the original flag? Start searching for the flag here nc foggy-cliff.picoctf.net 64549 hint: For text translation and character replacement, see tr command documentation.
## **Solucion**

picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_3a939318}
## **Notas adicionales**
--- Step 1 ---  
Current flag: KTgxMzkzOW4zLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj  
Hint: Base64 encoded the string.  
Enter the Linux command to reverse it:
base64 -d
---Step 2----
Current flag: )813939n3-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc Hint: Reversed the text. Enter the Linux command to reverse it: Current flag:
rev
---Step 3--------
Current flag: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-3n939318) Hint: Replaced underscores with dashes. Enter the Linux command to reverse it
tr "-" " _"
-- Step 4 --- Current flag: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_3n939318) Hint: Replaced curly braces with parentheses. Enter the Linux command to reverse it:
tr "()" "{}
-- Step 5 --- Current flag: cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_3n939318} Hint: Applied ROT13 to letters.
tr 'A-Za-z' 'N-ZA-Mn-za-m
## **Referencias**
https://geekland.eu/uso-del-comando-tr-en-linux-y-unix-con-ejemplos/
https://es.wikipedia.org/wiki/ROT13
