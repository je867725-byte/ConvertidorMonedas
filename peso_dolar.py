import requests

datos = requests.get(url).json()
tasa = datos["rates"]["MXN"]

opcion = input("1: Dólar a Peso | 2: Peso a Dólar: ")
cantidad = float(input("Cantidad: "))

if opcion == "1":
    print(f"{cantidad} USD = {cantidad * tasa:.2f} MXN")
elif opcion == "2":
    print(f"{cantidad} MXN = {cantidad / tasa:.2f} USD")
else:
    print("Opción inválida")
