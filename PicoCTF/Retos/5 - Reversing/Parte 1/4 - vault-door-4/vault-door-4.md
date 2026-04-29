### Descripción
This vault uses ASCII encoding for the password.The source code for this vault is here: [VaultDoor4.java](https://challenge-files.picoctf.net/c_fickle_tempest/5a242afc9022df976b1c18fe9364788579431217536fca41006714b29d8931e1/VaultDoor4.java)
### Solución
```
giselle_maz-picoctf@webshell:~$ wget -q https://challenge-files.picoctf.net/c_fickle_tempest/5a242afc9022df976b1c18fe9364788579431217536fca41006714b29d8931e1/VaultDoor4.java
giselle_maz-picoctf@webshell:~$ cat ^C
giselle_maz-picoctf@webshell:~$ cat VaultDoor4.java
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 040 , 063 ,
            '0' , 'd' , 'c' , '8' , '5' , 'b' , 'e' , 'd' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}

import java.util.*;

  

class VaultDoor4 {

    public static void main(String args[]) {

        VaultDoor4 vaultDoor = new VaultDoor4();

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

  

    // I made myself dizzy converting all of these numbers into different bases,

    // so I just *know* that this vault will be impenetrable. This will make Dr.

    // Evil like me better than all of the other minions--especially Minion

    // #5620--I just know it!

    //

    //  .:::.   .:::.

    // :::::::.:::::::

    // :::::::::::::::

    // ':::::::::::::'

    //   ':::::::::'

    //     ':::::'

    //       ':'

    // -Minion #7781

    public boolean checkPassword(String password) {

        byte[] passBytes = password.getBytes();

        byte[] myBytes = {

            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,

            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,

            0142, 0131, 0164, 063 , 0163, 0137, 040 , 063 ,

            '0' , 'd' , 'c' , '8' , '5' , 'b' , 'e' , 'd' ,

        };

  

       /* for (int i=0; i<32; i++) {

            if (passBytes[i] != myBytes[i]) {

                return false;

            }

        }*/

  

       String flag = new String(myBytes);

       System.out.println(flag);

        return true;

    }

}

entonces tomamos el codigo original y le hacemos estas modificaciones
       /* for (int i=0; i<32; i++) {

            if (passBytes[i] != myBytes[i]) {

                return false;

            }

        }*/

  

       String flag = new String(myBytes);

       System.out.println(flag);

PS C:\Users\Giselle MO\Documents\S26\FUN_SEG_INF\giselle_maz\PicoCTF\Retos\5 - Reversing\Parte 1\4 - vault-door-4> javac VaultDoor4.java
PS C:\Users\Giselle MO\Documents\S26\FUN_SEG_INF\giselle_maz\PicoCTF\Retos\5 - Reversing\Parte 1\4 - vault-door-4> java VaultDoor4      
Enter vault password: picoCTF{cdncsl}
jU5t_4_bUnCh_0f_bYt3s_ 30dc85bed
Access granted.
```
### Notas adicionales 
picoCTF{jU5t_4_bUnCh_0f_bYt3s_ 30dc85bed}
### Referencias