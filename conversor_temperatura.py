# Programa para convertir una cantidad dada de grados centigrados a su equivalente en Farenheit y Kelvin

print("----------------------------------")
print("-----conversor de Temperatura-----")
print("----------------------------------")

#input
C = int(input (" digite el valor de C: "))

# processing
F = (C * 1.8 + 32)
K = (C + 273.15)

#output
print("----------------------------------")
print("------------RESULTADOS------------")
print("----------------------------------")
print("la conversion de " + str(C) + " grados celcius a grados farenheit es " + str(F))
print("la conversion de " + str(C) + " grados celcius a grados kelvin es" + str (K))
