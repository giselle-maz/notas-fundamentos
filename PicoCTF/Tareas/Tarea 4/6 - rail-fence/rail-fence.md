### Descripción
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?Download the message [here](https://artifacts.picoctf.net/c/190/message.txt).Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.
### Solución
```
descragamos y vemos el mensaje cifrado
cat message.txt
Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA

luego deciframos meidante este codigo

python3 -c "
def decode_rail_fence(ct, rails):
    fence = [['\n'] * len(ct) for _ in range(rails)]
    rail, direction = 0, 1
    for i in range(len(ct)):
        fence[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1: direction *= -1
    
    idx = 0
    for r in range(rails):
        for c in range(len(ct)):
            if fence[r][c] == '*' and idx < len(ct):
                fence[r][c] = ct[idx]
                idx += 1
    
    result, rail, direction = [], 0, 1
    for i in range(len(ct)):
        result.append(fence[rail][i])
        rail += direction
        if rail == 0 or rail == rails - 1: direction *= -1
    return ''.join(result)

with open('message.txt', 'r') as f:
    ciphertext = f.read().strip()
    # Buscamos la flag dentro del mensaje descifrado
    decoded = decode_rail_fence(ciphertext, 4)
    print(f'\nMensaje descifrado: {decoded}')
    # Si el mensaje contiene la flag, la extraemos o la presentamos
    if 'is' in decoded:
        flag_content = decoded.split('is ')[1]
        print(f'\nTu Flag es: picoCTF{{{flag_content}}}')
    else:
        print(f'\nTu Flag es: picoCTF{{{decoded}}}')
"

giselle_maz-picoctf@webshell:~$ cat message.txt
giselle_maz-picoctf@webshell:~$ python3 sole.py

Mensaje descifrado: The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3



```
### Notas adicionales 
picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}
### Referencias