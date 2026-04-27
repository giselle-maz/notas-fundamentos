n = 22641736591898196020001528945685736821786038320165643579060676722778050919363835487755702470259320071388039503574355274318372601444679655046114013891336818 
e = 65537
c = 9132916083281900683759978534177981672159767876414781117353383651831557784208337123609652624517870778468493655977398402727802777851448582676763753480146089

# Los factores reales de tu N:
p = 2
q = n // 2

# 1. Calcular Phi correctamente
phi = (p - 1) * (q - 1)

# 2. Calcular d (Llave privada)
d = pow(e, -1, phi)

# 3. Descifrar el mensaje
m = pow(c, d, n)

# 4. Convertir a texto
hex_string = hex(m)[2:]
if len(hex_string) % 2 != 0:
    hex_string = '0' + hex_string

try:
    flag = bytes.fromhex(hex_string).decode('ascii')
    print(f"Tu Flag es: {flag}")
except:
    # Si no es ascii puro, intentamos ver el hex
    print(f"Resultado en hex: {hex_string}")