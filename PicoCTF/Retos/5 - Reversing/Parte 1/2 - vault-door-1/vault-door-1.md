### Descripción
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://challenge-files.picoctf.net/c_fickle_tempest/df83732fa379fb7cf3373e872748a40ec53c5baa532f3274e1ab499cd3d3b197/VaultDoor1.java)
### Solución
```
descargamos y vemos el contenido de codigo
giselle_maz-picoctf@webshell:~$ wget -q https://challenge-files.picoctf.net/c_fickle_tempest/df83732fa379fb7cf3373e872748a40ec53c5baa532f3274e1ab499cd3d3b197/VaultDoor1.java
giselle_maz-picoctf@webshell:~$ cat ^C
giselle_maz-picoctf@webshell:~$ cat VaultDoor1.java
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '2' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == 'e' &&
               password.charAt(30) == '6' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == 'f' &&
               password.charAt(26) == '1' &&
               password.charAt(31) == '6';
    }
}giselle_maz-picoctf@webshell:~$ nano VaultDoor1.java
giselle_maz-picoctf@webshell:~$ sort VaultDoor1.java

hay que editar con nano para ordenar la flag
            System.out.println("Access denied!");
            System.out.println("Access granted.");
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        String userInput = scanner.next();
        if (vaultDoor.checkPassword(input)) {
        }
        } else {
               password.charAt(00)  == 'd' &&
               password.charAt(01)  == '3' &&
               password.charAt(02)  == '5' &&
               password.charAt(03)  == 'c' &&
               password.charAt(04)  == 'r' &&
               password.charAt(05)  == '4' &&
               password.charAt(06)  == 'm' &&
               password.charAt(07)  == 'b' &&
               password.charAt(08)  == 'l' &&
               password.charAt(09)  == '3' &&
               password.charAt(10) == '_' &&
               password.charAt(11) == 't' &&
               password.charAt(12) == 'H' &&
               password.charAt(13) == '3' &&
               password.charAt(14) == '_' &&
               password.charAt(15) == 'c' &&
               password.charAt(16) == 'H' &&
               password.charAt(17) == '4' &&
               password.charAt(18) == 'r' &&
               password.charAt(19) == '4' &&
               password.charAt(20) == 'c' &&
               password.charAt(21) == 'T' &&
               password.charAt(22) == '3' &&
               password.charAt(23) == 'r' &&
               password.charAt(24) == '5' &&
               password.charAt(25) == '_' &&
               password.charAt(26) == '1' &&
               password.charAt(27) == 'e' &&
               password.charAt(28) == 'f' &&
               password.charAt(29) == '2' &&
               password.charAt(30) == '6' &&
               password.charAt(31) == '6';
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        VaultDoor1 vaultDoor = new VaultDoor1();
        return password.length() == 32 &&
    //
    // -Minion #8728
    // I came up with a more secure way to check the password without putting
    // UNHACKABLE!! I hope Dr. Evil agrees...
    // the password itself in the source code. I think this is going to be
    public boolean checkPassword(String password) {
    public static void main(String args[]) {
    }
    }
class VaultDoor1 {
import java.util.*;
}

 grep "password.charAt" VaultDoor1.java | sort | awk '{print $3}' | tr -d "'" | tr -d '\n'
d35cr4mbl3_tH3_cH4r4cT3r5_1ef266
```
### Notas adicionales 

picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_1ef266}
### Referencias