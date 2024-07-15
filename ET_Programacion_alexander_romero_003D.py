import random
import csv
import math

trabajadores = [
    "Juan Pérez", "María García", "Carlos lopez", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Días", "Elena Fernández"
]
sueldos = {}

def asignar_sueldo():
    global sueldos
    sueldos = {trabajador: random.randint (300000, 2500000) for trabajador in trabajadores}

def clasificar_sueldos():
    menores_800000 = [(nombre, sueldo) for nombre, sueldo in sueldos.items() if sueldo < 800000]
    entre_800k_y_2M= [(nombre, sueldo) for nombre, sueldo in sueldos.items() if 800000 <= sueldo <= 2000000]
    mayor_a_2M = [(nombre, sueldo) for nombre, sueldo in sueldos.items() if sueldo > 2000000]

    total_sueldos = sum(sueldo for sueldo in sueldos.values())

    print("\nSueldos menores a $800.000")
    print("TOTAL", len(menores_800000))
    for nombre, sueldo in menores_800000:
        print(f"{nombre} ${sueldo}")

    print("\n Sueldos entre 800k y 2m")
    print("TOTAL", len(entre_800k_y_2M))
    for nombre, sueldo in entre_800k_y_2M:
        print(f"{nombre} ${sueldo}")

    print("\n Sueldos mayor a 2M")
    print("TOTAL", len(mayor_a_2M))
    for nombre, sueldo in mayor_a_2M:
        print(f"{nombre} ${sueldo}")

    print("Total sueldos: $", total_sueldos)

def ver_estadisticas():
    if not sueldos:
        print("No se han asigando sueldos aún")
        return
    
    sueldos_lista = list(sueldos.values())
    sueldo_maximo = max(sueldos_lista)
    sueldo_minimo = min(sueldos_lista)
    promedio = sum(sueldos_lista)
    media_geometrica = math.exp(sum(math.log(sueldo) for sueldo in sueldos_lista) / len(sueldos_lista))

    print(f"\nEl sueldo mas alto es: ${sueldo_maximo}")
    print(f"\nEl sueldo mas bajo es: ${sueldo_minimo}")
    print(f"\nEl promedio de sueldo es: ${promedio:.2f}")
    print(f"\nLa media geometrica de sueldos es: ${media_geometrica:.2f}")

def reporte_sueldos():
    if not sueldos:
        print("No hay sueldos asignados para generar el reporte..")
        return
    
    try:
        with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
            fieldnames = [ 'Nombre empleado', 'Sueldo Base', 'Descuento salud', 'Descuento AFP', 'Sueldo liquido']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for nombre, sueldo in sueldos.items():
            descuento_salud = int(sueldo * 0.07)
            descuento_afp = int(sueldo * 0.12)
            sueldo_liquido = sueldo - descuento_salud - descuento_afp

            print({
                        
                'Nombre empleado': nombre,
                'Sueldo base': f"${sueldo:,}",
                'Descuento salud': f"${descuento_salud:,}",
                'Descuento AFP': f"${descuento_afp:,}",
                'Sueldo Liquido': f"${sueldo_liquido:,}"
            })

    except Exception as e:
        ("Print error en generar el reporte: {e}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir")

        opcion = input("selecione una opcion 1-5:")

        if opcion == '1':
            asignar_sueldo()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
             print("Finalizando programa, espere... \nDesarrollado por: Alexander Romero. \nRut: 21.878.881-5")
             break
        else:
            print("Opcion no valida.")

menu()