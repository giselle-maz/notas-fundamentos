
### DESCRIPCIÓN

Can you conjure the right bytes? I will name four procedures hidden inside `spellbook`. Each round, send me their _raw_ 4-byte addresses in little-endian form. 3 correct answers unlock the flag.

`nc lonely-island.picoctf.net 63785`
### SOLUCIÓN

Este desafío es un ejercicio de **Análisis de Binarios** y **Automatización de Explotación**. A diferencia de los niveles anteriores, el servidor solicita direcciones de memoria que cambian aleatoriamente en cada sesión, lo que requiere el uso de scripts para interactuar con el binario `spellbook` en tiempo real.

1. **Análisis Estático del Binario:** Utilizamos la herramienta `objdump` o `nm` sobre el archivo suministrado para localizar las funciones "mágicas" dentro de la sección de símbolos del ELF. Las funciones objetivo identificadas en el binario son:
    
    - `ember_sigil`
        
    - `glyph_conflux`
        
    - `astral_spark`
        
    - `binding_word`
        
2. **Manejo de Endianness (Little-Endian):** El servidor requiere que las direcciones de 32 bits sean enviadas en formato **Little-Endian**. Esto significa que el byte menos significativo se envía primero.
    
    - _Ejemplo teórico:_ Si la dirección es `0x0804a040`, el payload debe ser `\x40\xa0\x04\x08`.
        
3. **Automatización con Pwntools:** Debido a que el servidor exige 3 respuestas correctas seguidas y elige las funciones al azar, se implementó un script en Python utilizando la librería `pwntools`. El script realiza lo siguiente:
    
    - Carga el binario local `spellbook` para mapear los símbolos a direcciones automáticamente.
        
    - Establece una conexión TCP con el servidor.
        
    - Lee el nombre de la función solicitada, busca su dirección y la empaqueta usando la función `p32()` (que convierte un entero a 4 bytes Little-Endian).
      
```
      from pwn import *

# Conexión al servidor
p = remote('lonely-island.picoctf.net', 63785)
elf = ELF('./spellbook')

for i in range(3):
    # Parsear el nombre de la función solicitada
    p.recvuntil(b"procedure '")
    func_name = p.recvuntil(b"'").decode().strip("'")

    # Obtener dirección y enviar
    target_addr = elf.symbols[func_name]
    p.send(p32(target_addr))

# Obtener la bandera
print(p.recvall().decode())
```
### NOTAS ADICIONALES


### REFERENCIAS