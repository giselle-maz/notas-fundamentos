### Descripción
Can you open this safe?
I forgot the key to my safe but this https://artifacts.picoctf.net/c/83/SafeOpener.java is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
Put the password you recover into the picoCTF flag format like:
picoCTF{password} 
### Solución
```
en el codigo encontramos con que se valida la flag, entonces basta con decodificar esta cadena y tenemos la flag.

asi que descargamos y vemos el codigo.

giselle_maz-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/83/SafeOpener.java
--2026-05-04 19:52:20--  https://artifacts.picoctf.net/c/83/SafeOpener.java
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.77, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1258 (1.2K) [application/octet-stream]
Saving to: 'SafeOpener.java'

SafeOpener.java        100%[============================>]   1.23K  --.-KB/s    in 0s      

2026-05-04 19:52:20 (261 MB/s) - 'SafeOpener.java' saved [1258/1258]

giselle_maz-picoctf@webshell:~$ cat SafeOpener.java
import java.io.*;
import java.util.*;  
public class SafeOpener {
    public static void main(String args[]) throws IOException {
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        int i = 0;
        boolean isOpen;
        

        while (i < 3) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();

            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
              
            isOpen = openSafe(encodedkey);
            if (!isOpen) {
                System.out.println("You have  " + (2 - i) + " attempt(s) left");
                i++;
                continue;
            }
            break;
        }
    }
    
    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
}

tomamos la cadena y la decodificamos
giselle_maz-picoctf@webshell:~$ echo "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" | base64 -d
pl3as3_l3t_m3_1nt0_th3_saf3

y listo, transformamos para que tenga el formato.


```
### Notas adicionales 
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
### Referencias