print("Hola, soy Akira, la asistente de Ana en su cafetería, por favor ingresa los datos que se te piden. ")
temperatura = float(input("Cuál es la temperatura en Celsius de tu bebida? "))
print("")
horadia = int(input("Ingresa la hora del día en formato 24 horas sin minutos, redondealos a la hora entera. "))
print("")
print("Que tipo de bebida quieres:")
print("1. Café")
print("2. Té")
print("3. Chocolate caliente")
print("")
seleccionbebida = int(input("Escribe el número de la bebida que gustas. "))
print("")
if temperatura <= 50:
  print("Debe esperar a que se caliente la bebida")
elif temperatura <=70 and temperatura >= 50:
  print("Se puede servir de inmediato")
elif temperatura > 70:
  print("Bebida muy caliente, debe esperar a que se enfríe")
else:
  print("Temperatura no valida")
print("")
if horadia >= 6 and horadia <= 11:
  print("Las bebidas calientes se sirven más rápido")
else:
  print("Debe esperar su turno")
print("")
if seleccionbebida == 1 or seleccionbebida == 2 and   horadia >= 7 and horadia <=9 :
  print("Te recomendamos una bebida caliente.")
elif seleccionbebida == 2 or seleccionbebida == 3 and horadia >= 12 and horadia <=14:
  print("Te recomendamos una bebida fría")
else:
  print("Seleccion de bebidas no valida para recomendaciones.")
