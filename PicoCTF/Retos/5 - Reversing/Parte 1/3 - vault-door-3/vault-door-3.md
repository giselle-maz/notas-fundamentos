### Descripción
This vault uses for-loops and byte arrays.The source code for this vault is here: [VaultDoor3.java](https://challenge-files.picoctf.net/c_fickle_tempest/4cff24ee8b551078be8c14758fae20ab4a2dca78746aef367bc854491b8ee465/VaultDoor3.java)
### Solución
```
descragamso y hacemos cat
giselle_maz-picoctf@webshell:~$ wget -q https://challenge-files.picoctf.net/c_fickle_tempest/4cff24ee8b551078be8c14758fae20ab4a2dca78746aef367bc854491b8ee465/VaultDoor3.java
giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ cat VaultDoor3.java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm1cg04e_u_4_m6rb42");
        
        vemos aparentementa la bandera, pero esta desordenada.
Entonces tomamos el codigo original y le agregamos dos lineas para que nos imprima la flag en orden        
       
al ejecutar nos arroja la flag ordenada
 Reversing\Parte 1\3 - vault-door-3> java VaultDoor3
Enter vault password: picoCTF{jU5t_a_sna_3lpm1cg04e_u_4_m6rb42}
jU5t_a_s1mpl3_an4gr4m_4_u_e60bc2
Access denied!

```
### Notas adicionales 
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_e60bc2}
### Referencias