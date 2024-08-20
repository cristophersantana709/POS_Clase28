carrito = []
total = 0.0

def mostrar_menu():
    print("BIENVENIDO AL POS")
    print("1. Agregar producto al carrito")
    print("2. Ver total del carrito")
    print("3. Pagar")
    print("4. Salir")

def agregar_producto():
    global total 
    
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    carrito.append({"producto": producto , "precio": precio})
    total += precio
    print(f"Has agregado {producto} al carrito por {precio}.")
    
def ver_total():
    print(f"El total de tu carrito es: {total:.2f}")
  
def pagar():
    global total , carrito 
    if total == 0:
        print("Tu carrito esta vacio, no hay nada qu pagar.")
    else:
        print(f"El total a pagar es: {total}")
        pago = float(input("Ingesa la cantidad con la que vas a pagar: "))
        if pago >= total:
            cambio = pago - total
            print(f"Pago realizado con exito: Tu cambio es: {cambio}")
         
            carrito = []
            total = 0.0
        else:
            print("No tiene suficientes dinero para pagar.")
                
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleciona una opcion: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_total()
        elif opcion == "3":
            pagar()
        elif opcion == "4":
            print("Gracias por usar el POS, ¡Hasta luego!")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo.")
            
ejecutar()