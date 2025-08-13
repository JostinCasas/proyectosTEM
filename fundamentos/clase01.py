print("Hola mundo desde python")
#variable numericas
edad = 25 # Entero
altura = 1.75 #Flotante
bandera = True # Booleano
nombre = "Bruno Diaz" # String
print("\nPrint tradicional")
print("-----------------")
print ("Mi nombre es: ", nombre)
print("Mi edad es:", edad)
print("Mi altura es:", altura)
print("Estoy vivo", bandera)
#Entrada de Datos
print("\nEntrada de Datos")
print("------------------")
nombre = input("Ingresa tu nombre: ")
edad =int(input("Ingresaa tu edad: "))
altura = float(input("Ingresa tu Altura: "))
bandera =input("Estas vivo? (True/Flase): ")

# Segunda forma de imprimir
print("\n Print moderno")
print("-----------------")
print(f"Mi nombre es: {nombre}")
print(f"Mi edad es: {edad}")
print(f"Mi altura es: {altura}")
print(f"Estoy vivo: {bandera}")