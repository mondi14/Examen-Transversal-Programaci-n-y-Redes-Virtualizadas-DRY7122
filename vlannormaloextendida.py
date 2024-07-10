# Definimos los rangos de VLAN
RANGO_NORMAL = range(1, 1006)
RANGO_EXTENDIDO = range(1006, 4096)

# Pedimos al usuario que ingrese el número de VLAN
numero_vlan = int(input("Ingrese el número de VLAN: "))

# Verificamos en qué rango se encuentra la VLAN
if numero_vlan in RANGO_NORMAL:
    print(f"La VLAN {numero_vlan} corresponde al rango normal.")
elif numero_vlan in RANGO_EXTENDIDO:
    print(f"La VLAN {numero_vlan} corresponde al rango extendido.")
else:
    print(f"El número de VLAN {numero_vlan} no es válido.")