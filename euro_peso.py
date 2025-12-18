# euro a peso mexicano
# Tipo de cambio actual (puedes actualizarlo según el momento)
tipo_cambio = 20.00  # 1 EUR = 20.00 MXN

# Pedir al usuario el monto en euros
euros = float(input("Ingresa la cantidad en euros: "))

# Convertir a pesos
pesos = euros * tipo_cambio

# Mostrar el resultado
print(f"{euros:.2f} EUR equivalen a {pesos:.2f} MXN")
