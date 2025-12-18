
tipo_cambio = 18.50 


dolares = float(input("Ingresa la cantidad en dólares: "))


pesos = dolares * tipo_cambio

print(f"${dolares:.2f} USD equivalen a ${pesos:.2f} MXN")
