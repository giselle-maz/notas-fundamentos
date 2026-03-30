# Cookie Monster Secret Recipe

## Descripcion

Cookie Monster 
has hidden his top-secret cookie recipe somewhere on his website. As an 
aspiring cookie detective, your mission is to uncover this delectable 
secret. Can you outsmart Cookie Monster and find the hidden recipe?
You can access the Cookie Monster [here](http://verbal-sleep.picoctf.net:51739/) and good luck

## Solucion

abrimos el link e inspeccionamos la pagina, vemos el trafico al intentar hacer login sin exito

entonces vamos a almacenamiento y copeamos informacion referente a la cookie

`value: cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzc4QjRDMzkwfQ%3D%3D`

encontramos una receta secreta pero esta en base 64, hay que decodificar usando CyberChef

[https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Y0dsamIwTlVSbnRqTURCck1XVmZiVEJ1YzNSbGNsOXNNSFpsYzE5ak1EQnJhV1Z6WHpjNFFqUkRNemt3ZlElM0QlM0Q&oeol=CR](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Y0dsamIwTlVSbnRqTURCck1XVmZiVEJ1YzNSbGNsOXNNSFpsYzE5ak1EQnJhV1Z6WHpjNFFqUkRNemt3ZlElM0QlM0Q&oeol=CR)

y la flag:

picoCTF{c00k1e_m0nster_l0ves_c00kies_78B4C390}

## Nots adicionales

picoCTF{c00k1e_m0nster_l0ves_c00kies_78B4C390}

## Referencias