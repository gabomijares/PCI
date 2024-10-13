    """
    MI BMW Y YO
    Este programa tiene como objetivo un test, donde un posible comprador de BMW ingresará sus preferencias en un vehículo,
    y este le devolverá el BMW perfecto para él/ella. Así como un plan de financiamiento a meses si este lo desea.
    """
    
    # Función que imprime el modelo ideal y sus características
    def printModelBMW(x):
        model = ['BMW Serie 1 128ti','BMW Serie 2 Coupé','BMW Serie 3','BMW Serie 4 Gran Coupé','BMW i4 eDrive40','BMW Z4 M40i Roadster','BMW X3 M','BMW X4 M Competition','BMW X6 M Competition','BMW iX M60']
        description = ['El compacto deportivo perfecto para quienes buscan un auto ágil y divertido de manejar. Con un diseño dinámico y un rendimiento mejorado, ofrece una experiencia de conducción emocionante.','El BMW Serie 2 Coupé ofrece un diseño compacto y elegante con un rendimiento deportivo mejorado. Es perfecto para aquellos que desean un manejo ágil y dinámico en un paquete sofisticado.','El Serie 3 de BMW sigue siendo un referente en su categoría, combinando elegancia, tecnología avanzada y un rendimiento que se adapta tanto a la ciudad como a la carretera.','Con un diseño aerodinámico y mejoras en su rendimiento, el BMW Serie 4 Gran Coupé es una opción versátil para quienes buscan lujo y deportividad con mayor espacio interior.','El i4 eDrive40 continúa siendo una referencia en el segmento de autos eléctricos, ofreciendo una autonomía notable y un manejo deportivo que mantiene el ADN de BMW.','El BMW Z4 M40i se renueva para ofrecer una experiencia de conducción al aire libre aún más emocionante, con un rendimiento superior y tecnología actualizada.','El BMW X3 M se posiciona como un SUV deportivo con un rendimiento extraordinario, perfecto para quienes buscan potencia y versatilidad sin sacrificar el lujo.','El BMW X4 M Competition se destaca por su combinación única de diseño coupé y capacidades de SUV, brindando una experiencia de conducción emocionante en cualquier terreno.','El BMW X6 M Competition 2025 es una máquina impresionante, combinando un diseño agresivo y una potencia abrumadora para quienes buscan el máximo rendimiento en un SUV.','El BMW iX M60 2025 es un SUV eléctrico de alta gama que combina tecnología de punta, lujo y sostenibilidad, ofreciendo una experiencia única tanto en carretera como en la ciudad.']
        aspects = [' - Tracción delantera precisa.\n - Suspensión deportiva M con ajuste revisado.\n - Diferencial autoblocante mecánico mejorado.',' - Suspensión M adaptativa mejorada.\n - Control de tracción xDrive disponible.\n - Nuevos sistemas de asistencia al conductor.',' - Sistema de infoentretenimiento iDrive 9.\n - Opción de motores híbridos enchufables.\n - Nueva generación de suspensión adaptativa.',' - Nueva tecnología híbrida suave.\n - Puertas sin marco con mejor acústica.\n - Sistema de sonido premium Harman Kardon.',' - Autonomía extendida hasta 580 km.\n - Carga rápida mejorada.\n - Tecnología de asistencia de conducción avanzada.',' - Capota suave retráctil mejorada para más aislamiento acústico.\n - Sistema de escape deportivo M ajustado.\n - Configuración de chasis adaptada para mejor manejo.',' - Suspensión M adaptativa mejorada.\n - Tracción integral M xDrive optimizada.\n - Asientos deportivos en cuero premium.',' - Diseño exterior renovado con líneas más aerodinámicas.\n - Frenos M de alto rendimiento.\n - Sistema de asistencia de estacionamiento automático.',' - Sistema de escape deportivo M renovado.\n - Tecnología de conducción semi-autónoma.\n - Tapicería en cuero Merino exclusivo.',' - Autonomía de hasta 590 km.\n - Tecnología de control por gestos mejorada.\n - Sistema de conducción autónoma nivel 3.']
        powPri = ['Potencia: 270 hP\nPrecio Base: $610,500 mx\nPrecio Equipado: $698,000 mxn','Potencia: 380 hP\nPrecio Base: $670,000 MXN\nPrecio Equipado: $890,000 MXN','Potencia: 190-510 hP\nPrecio Base: $750,000 MXN\nPrecio Equipado: $1,390,000 MXN','Potencia: 390 hP\nPrecio Base: $870,000 MXN\nPrecio Equipado: $1,170,000 MXN','Potencia: 350 hP\nPrecio Base: $980,000 MXN\nPrecio Equipado: $1,150,000 MXN','Potencia: 390 hP\nPrecio Base: $1,150,000 MXN\nPrecio Equipado: $1,320,000 MXN','Potencia: 480 hP\nPrecio Base: $1,320,000 MXN\nPrecio Equipado: $1,500,000 MXN','Potencia: 520 hP\nPrecio Base: $1,450,000 MXN\nPrecio Equipado: $1,650,000 MXN','Potencia: 630 hP\nPrecio Base: $2,200,000 MXN\nPrecio Equipado: $2,420,000 MXN','Potencia: 620 hP\nPrecio Base: $1,980,000 MXN\nPrecio Equipado: $2,150,000 MXN']
        if x < 10:
            print(model[x])
            print(description[x])
            print(aspects[x])
            print(powPri[x])
            return True
        else:
            print('No encontramos un BMW que cumpla con las especificaciones que nos pediste. :(\nPero no dudes en acudir a tu agencia BMW más cercana para que te asesoremos en la búsqueda de tu vehículo.\nHazlo tuyo!')
            return None
        # Esto verifica si hay resultado, ejecutar el financiamiento. Si no, detener el programa.
        
    # Matriz con los precios de los vehículos. [Versión base, Versión equipada]
    prices = [[610500,698000],[670000,890000],[750000,1390000],[870000,1170000],[980000,1150000],[1150000,1320000],[1320000,1500000],[1450000,1650000],[2200000,2420000],[1980000,2150000]]
       
       
    # Función que transforma los datos del usuario en valores numéricos
    def respuestasBMWIdeal(use,size,fuel,power,budget):
        if (use == 1 or use == 2) and size == 1 and fuel == 1 and (power == 1 or power == 2) and (budget == 1 or budget == 2):
            return 0
        elif (use == 1 or use == 2) and (size == 1 or size == 2) and fuel == 2 and (power == 1 or power == 2) and (budget == 1 or budget == 2):
            return 1
        elif (use == 1 or use == 2) and (size == 1 or size == 2) and fuel == 2 and (power == 1 or power == 2) and (budget == 2 or budget == 3):
            return 2
        elif (use == 1 or use == 2 or use == 3) and (size == 2 or size == 3) and (fuel == 2 or fuel == 3) and (power == 2 or power == 3) and (budget == 2 or budget == 3):
            return 3
        elif (use == 1 or use == 2 or use == 3) and (size == 2 or size == 3) and fuel == 1 and (power == 2 or power == 3) and (budget == 3 or budget == 4):
            return 4
        elif (use == 2 or use == 3) and size == 1 and (fuel == 2 or fuel == 3) and (power == 2 or power == 3) and (budget == 3 or budget == 4):
            return 5
        elif (use == 1 or use == 2 or use == 4) and (size == 2 or size == 3) and (fuel == 2 or fuel == 3) and (power == 1 or power == 2) and (budget == 3 or budget == 4):
            return 6
        elif size == 3 and fuel == 3 and (power == 2) and (budget == 4 or budget == 5):
            return 7
        elif size == 3 and fuel == 3 and power == 3 and budget == 5:
            return 8
        elif size == 3 and fuel == 1 and (power == 2 or power == 3) and budget == 5:
            return 9
        else:
            return 10
    
    
    # Función que realiza el financiamiento del auto
    def financing(price, perc, months):
        eng = price * (perc / 100)  
        debt = price - eng  
        yearInt = 0.15  
        intTotal = 0  
        years = months // 12
        if months > 12:
            for _ in range(years):
                intTotal += debt * yearInt
        monpay = (debt+intTotal)/months
        monpay = round(monpay, 2)
        
        # Modicicación de strings para que precios se impriman con formato moneda $, y porcentajes con %
        engPriceTag = f'${eng:,.2f}'
        debtPriceTag = f'${debt:,.2f}'
        yearIntPerc = f'{yearInt:.0%}'
        monpayPriceTag = f'${monpay:,.2f}'
        
        financingResult = (f'- Enganche ({perc}%): {engPriceTag}\n'f'- Monto a financiar: {debtPriceTag}\n'f'- Tasa de Interés Anual: {yearIntPerc}\n'f'- Mensualidades: {monpayPriceTag}\n')
        
        return financingResult
        return monpay
    
    # Función para casos de prueba
    def testFinancing():
        price = 1000000
        perc = 60
        months = 12
        expectedRes = 33333.33
        result = financing(price, perc, months)
        assert abs(result - expectedRes) < 0.01, f"Caso 1: False, obtenido {result}"
    
        price = 1500000
        perc = 40
        months = 24
        expectedRes = 48750.00
        result = financing(price, perc, months) 
        assert abs(result - expectedRes) < 0.01, f"Caso 2: False, obtenido {result}"
    
        print("Casos de prueba: True")
    
    
    # Menus de las opciones en el test
    def menuUse():
        print('1. Uso diario, prefiero la comodidad.')
        print('2. Carreteras, soy un nómada moderno.')
        print('3. Pista, todo un amante de la velocidad')
        print('4. Off-Road, me encanta la adrenalina.')
    
    def menuSize():
        print('1. Un auto pequeño, para uso individual.')
        print('2. Un auto mediano, para la comodidad de dos o tres personas.')
        print('3. Un auto grande, perfecto para la familia.')
    
    def menuFuel():
        print('1. Preferiría no consumir combustible en lo absoluto.')
        print('2. Un consumo promedio sería ideal.')
        print('3. El combustible no es problema en lo absoluto.')
    
    def menuPower():
        print('1. La potencia no es algo que este en mis prioridades.')
        print('2. Mi auto tiene que ser suficentemente potente. Por seguridad.')
        print('3. Quiero todos los caballos en mi cofre!')
        
    def menuBudget():
        print('1. > $600,000')
        print('2. > $800,000')
        print('3. > $1,000,000')
        print('4. > $1,500,000')
        print('5. > $2,000,000')
    
    
    def main():
        # Aqui comienza el test y la recolección de datos
        print('Hola! Bienvenido a tu test "Mi BMW Y YO". \nAquí podrás definir qué buscan en tu BMW, y te ayudaremos a encontrar el vehículo para ti. \n ¿Estás listo/a?')
        resp = input()
        print('\nExcelente! Empecemos por definir lo más importante. \n\n¿Cuál es el uso que le darás a tu BMW?')
        menuUse()
        opUse = int(input())
        print('Ya tenemos lo más importante. Ahora, ¿de qué tamaño buscas tu BMW?')
        menuSize()
        opSize = int(input())
        print('Muy bien! Ahora, ¿qué tanto planeas consumir combustible?')
        menuFuel()
        opFuel = int(input())
        print('Buena decisión. Vayamos a lo divertido, ¿qué tan potente quieres que sea tu BMW?')
        menuPower()
        opPow = int(input())
        print('Ya casi terminamos! Ahora, ¿cuál es tu presupuesto aproximado?')
        menuBudget()
        opBud = int(input())
        respuestas = respuestasBMWIdeal(opUse,opSize,opFuel,opPow,opBud)
        print('Terminamos. ¿Listo para conocer tu BMW ideal?')
        resp2 = input()
        print()
        booleanPrint = printModelBMW(respuestas)
        if booleanPrint is None:
            return
        # Si hay resultado, aquí comienza el programa de financiamiento
        print('\nAhora, hagamos posible que seas tú quién disfrute de este vehículo.\n ¿Deseas conocer un plan de financiamiento que se adapte a tu presupuesto?')
        print('1. Hagámoslo!\n2. Prefiero el pago de contado.')
        resp3 = int(input())
        if resp3 == 1:
            print('Volvámoslo realidad! ¿Qué versión de gustaría adquirir?\n1. Base\n2. Equipada')
            vers = int(input())
            if vers == 1:
                price = prices[respuestas][0]
            elif vers == 2:
                price = prices[respuestas][1]
            print('En el plan de financiamiento, el mínimo porcentaje de enganche es del 30%. ¿Con qué porcentaje quisieras iniciar?')
            while True:
                perceng = int(input())
                if perceng >= 30:
                    print('Muy bien. ¿A cuántos meses te gustaría financiarlo?')
                    print(' (El máximo son 48 meses)')
                    while True:
                        months = int(input())
                        if months > 48:
                            print('El máximo son 48 meses')
                        elif months < 2:
                            print('El mínimo son 2 meses')
                        else:
                            print('\nPerfecto! Este es el plan de financiamiento que mejor se adapta a tu presupuesto:')
                            financingResult = financing(price,perceng,months)
                            print(financingResult)
                            with open("plan_financiamiento.txt", "w") as file:
                                file.write("Plan de Financiamiento BMW\n")
                                file.write(financingResult)
                            print('Este plan ha sido guardado en "plan_financiamiento.txt". Llévalo a tu agencia BMW más cercana y ¡hazlo tuyo!')
                            break
                    break
                else:
                    print('Lo siento. El mínimo es 30.')
        elif resp3 == 2:
            print('Perfecto! Te esperamos en tu agencia BMW más cercana. Hazlo tuyo!')
    
    main()
    #testFinancing()
