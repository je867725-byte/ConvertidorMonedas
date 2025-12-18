# peso mexicano a euro
# Tipo de cambio actual (puedes actualizarlo según el momento)
tipo_cambio = 20.00  # 1 EUR = 20.00 MXN

# Pedir al usuario el monto en pesos
pesos = float(input("Ingresa la cantidad en pesos mexicanos: "))

# Convertir a euros
euros = pesos / tipo_cambio

# Mostrar el resultado
print(f"${pesos:.2f} MXN equivalen a €{euros:.2f} EUR")
