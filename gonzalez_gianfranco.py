# Zapatillas strike
stock_total = 20
reservas = []

def mostrar_menu():
    print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")

def reservar_zapatillas():
    global stock_total
    if stock_total == 20:
        print("No hay stock disponible.")
        return
    
    print("-- Reservar Zapatillas --")
    pedro = input("Nombre del comprador: ")
    clave = input("Digite la palabra secreta para confirmar la reserva: ")
    if clave == "EstoyEnListaDeReserva":
        reservas.append({'nombre': pedro 'pares': 1, 'vip': False})
        stock_total -= 1
        print(f"Reserva realizada exitosamente para {pedro}.")
    else:
        print("Error: palabra clave incorrecta. Reserva no realizada.")

def buscar_reserva():
    global stock_total
    print("-- Buscar Zapatillas Reservadas --")
    pedro = input("Nombre del comprador a buscar: ")
    for reserva in reservas:
        if reserva['pedro'].lower() == pedro.lower():
            tipo = "VIP" if reserva['vip'] else "estándar"
            print(f"Reserva encontrada: {reserva['pedro']} - {reserva['pares']} par(es) ({tipo}).")
            if not reserva['vip']:
                respuesta = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ")
                if respuesta.lower() == "s":
                    if stock_total > 0:
                        reserva['vip'] = True
                        stock_total -= 1
                        reserva['pares'] = 2
                        print(f"Reserva actualizada a VIP. Ahora {reserva['pedro']} tiene 2 pares reservados.")
                    else:
                        print("No hay stock suficiente para actualizar a VIP.")
                else:
                    print("Manteniendo reserva actual.")
            return
    print("No se encontró ninguna reserva con ese nombre.")

def ver_stock():
    pares_reservados = sum([r['pares'] for r in reservas])
    print("-- Ver Stock de Reservas --")
    print(f"Pares reservados: {pares_reservados}")
    print(f"Pares disponibles: {stock_total}")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        reservar_zapatillas()
    elif opcion == "2":
        buscar_reserva()
    elif opcion == "3":
        ver_stock()
    elif opcion == "4":
        print("Programa terminado.")
        break
    else:
        print("Debe ingresar una opción válida!!")
