print("=== CONTROLES DEL ROBOT ===")
print("A. Avanzar a la derecha")
print("B. Avanzar a la izquierda")
print("C. Avanzar hacia el frente")
print("D. Retroceder")
print("E. Apagar sistema")

while True:
    comando = input("Ingrese la opción deseada: ")

    match comando:
        case "A" | "a":
            print("Acción: El robot avanzó a la derecha")
        case "B" | "b":
            print("Acción: El robot avanzó a la izquierda")
        case "C" | "c":
            print("Acción: El robot avanzó hacia el frente")
        case "D" | "d":
            print("Acción: El robot retrocedió")
        case "E" | "e":
            print("Sistema apagado correctamente.")
            break
        case _:
            print("Opción no válida. Por favor, intente nuevamente.")
            