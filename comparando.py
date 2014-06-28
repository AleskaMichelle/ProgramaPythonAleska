print("Esto es un comparador de numeros")

resp = 's'
while resp == "s":
    
    numero1 = int(input("Por favor, Escriba un numero: "))
    numero2 = int(input("Por favor, Escriba otro numero: "))

    if numero1 > numero2:
       print("El Menor:", numero2, "El Mayor:", numero1)
    if numero1 < numero2:
       print("El Menor:", numero1, "El Mayor:", numero2)
    if numero1 == numero2:
       print("Estos dos numeros son iguales")

    
    resp = raw_input("Quiere ingresar otros numeros?s/n: ")

    raw_input
