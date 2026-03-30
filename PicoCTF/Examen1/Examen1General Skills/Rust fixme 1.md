## **Descripcion**
Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!Download the Rust code [here](https://challenge-files.picoctf.net/c_verbal_sleep/3f0e13f541928f420d9c8c96b06d4dbf7b2fa18b15adbd457108e8c80a1f5883/fixme1.tar.gz).
## **Solucion**cd 
picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}

## **Notas adicionales**
Paso 1: Se descomprime el archivo descargado
Paso 2: Se ingresa a la carpeta fixme1 y luego a src
```
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/rf1]
└─$ cd fixme1 
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/rf1/fixme1]
└─$ cd src
```
Paso 3: Al archivo main.rs le tienes que modificar el codigo para que asi te de la bandera.
Paso 4: Teniendolo modificado lo correras y te saldria esto y ahi esta la bandera
```
┌──(kali㉿kali)-[~/…/Fundamentos8A/rf1/fixme1/src]
└─$ cargo run   
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.02s
     Running `/home/kali/Documents/Fundamentos8A/rf1/fixme1/target/debug/rust_proj`
picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}:?

```
