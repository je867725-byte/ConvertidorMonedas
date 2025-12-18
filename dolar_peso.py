# dólar a peso mexicano
# Tipo de cambio actual (puedes actualizarlo según el momento)
tipo_cambio = 18.50  # 1 USD = 18.50 MXN

# Pedir al usuario el monto en dólares
dolares = float(input("Ingresa la cantidad en dólares: "))

# Convertir a pesos
pesos = dolares * tipo_cambio

# Mostrar el resultado
print(f"${dolares:.2f} USD equivalen a ${pesos:.2f} MXN")
