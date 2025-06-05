while True:
    op = input("Operación (+, -, *, /): ")
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))
    if op == "+":
        print (a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b != 0:
            print(a / b)
        else:
            print("No se puede dividir entre cero")
    import random
    secreto = random.randint(1, 100)
    intento = 0
    while True:
        intento = int(input("Adivina el número (1-100): "))
        if intento == secreto:
            print("¡Correcto!")
            break
        elif intento < secreto:
            print("Mayor")
        else:
            print("Menor")
