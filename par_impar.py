while True:
        numero = int(input("Introduce un número: "))
        if numero % 2 == 0:
                print("Es par")

        else:
                print("Es impar")




        lista = int(input("a cuantos numeros desea imprimir el cuadrado?   "))

        for n in range (lista):
                print(f"El cuadrado de {n} es {n**2}")

        respuesta = ""

        while respuesta.lower() != "ok":
                respuesta = input("Escribe 'ok' para continuar: ")