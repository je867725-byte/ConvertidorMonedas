
tipo_cambio = 20.00 


pesos = float(input("Ingresa la cantidad en pesos mexicanos: "))

euros = pesos / tipo_cambio


print(f"${pesos:.2f} MXN equivalen a €{euros:.2f} EUR")
