#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de escenarios del juego
Contiene los diferentes escenarios de la arventura
"""

import time
from utilidades import Colors, Utilidades


class Escenarios:
    """Clase que contiene todos los escenarios del juego"""
    
    @staticmethod
    def escenario_llegada():
        """Primera escena - Llegada a la oficina"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 1: PRIMER DÍA ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Es lunes por la mañana. Llegas a las oficinas de Chapuzalia M.L.,")
        Utilidades.escribir_lento("ubicadas en el segundo piso de un edificio de oficinas en Alcafrán.")
        time.sleep(0.3)
        Utilidades.escribir_lento("\nEl director de RRHH, Carlos, te recibe en la entrada:")
        time.sleep(0.5)
        print(f"\n{Colors.OKCYAN}Carlos:{Colors.ENDC} '¡Bienvenido/a! Te estábamos esperando. Tenemos muchas ganas de que empieces.'")
        print(f"{Colors.OKCYAN}Carlos:{Colors.ENDC} 'Hemos crecido muy rápido y... bueno, la seguridad los que mandan se la han dejado un poco de lado y necesitamos ponerle solución.'")
        print(f"{Colors.OKCYAN}Carlos:{Colors.ENDC} 'Hay algunas cosas que necesitan atención urgente antes de que alguien muera lamiendo enchufes o algo así ...'")
        
        time.sleep(0.5)
        Utilidades.escribir_lento("\nTras saludar a todo el mundo con los que te encuentras, vas caminando por el pasillo hacia tu oficina, y observas:")
        
        print(f"\n{Colors.WARNING}🔌 Cables de red cruzando el pasillo sin protección{Colors.ENDC}")
        print(f"{Colors.WARNING}🚪 Que la señal de salida de emergencia está parcialmente tapada por cajas{Colors.ENDC}")
        print(f"{Colors.WARNING}💡 Varios fluorescentes parpadeando en la zona de trabajo{Colors.ENDC}")
        
        print("\n¿Qué decides hacer PRIMERO?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Detenerte, y hablar con mantenimiento para exigir que se solucione inmediatamente (Enfoque estricto)")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Hacer un informe completo para presentar al jefe, antes de actuar (Enfoque metódico)")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Priorizar el riesgo de tropiezo con cables y actuar YA para que se solucione el peligro más inminente(Enfoque pragmático)")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Ignorarlo temporalmente y ir a tu oficina primero ... ya que es tu primer día y no quieres empezar amargándole el día a nadie (Enfoque pasivo)")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_llegada(decision, juego):
        """Procesa la decisión de la llegada"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Enfoque estricto
            Utilidades.escribir_lento("\n🛑 Detienes a Carlos y le informas de los riesgos INMEDIATOS.")
            time.sleep(0.3)
            print(f"\n{Colors.OKCYAN}Carlos:{Colors.ENDC} 'Pero... acabas de llegar. ¿No es un poco exagerado?'")
            Utilidades.escribir_lento(f"\n{Colors.BOLD}Tú:{Colors.ENDC} 'Según la Ley 31/1995, la prevención debe integrarse")
            Utilidades.escribir_lento("en todas las actividades. Un trabajador podría tropezar AHORA MISMO. Y si alguien se rompe la crisma ... se te caerá el pelo a ti y a mi.'")
            time.sleep(0.5)
            print(f"\n{Colors.WARNING}Carlos parece molesto pero accede a llamar a mantenimiento.{Colors.ENDC}")
            juego.puntuacion -= 5
            juego.riesgos_detectados += 3
            juego.decisiones_correctas += 1
            print(f"\n{Colors.FAIL}❌ Puntuación -5 (enfoque muy agresivo para el primer día){Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +3 Riesgos detectados{Colors.ENDC}")
            
        elif decision == 2:
            # Enfoque metódico
            Utilidades.escribir_lento("\n📋 Decides documentar todo profesionalmente antes de actuar.")
            time.sleep(0.3)
            Utilidades.escribir_lento("Sacas tu tablet y comienzas a tomar fotos y notas...")
            time.sleep(0.5)
            Utilidades.escribir_lento("\n⏰ Mientras documentas, escuchas un grito:")
            print(f"\n{Colors.FAIL}💥 '¡AY!' - Un empleado tropieza con los cables y cae de morros contra el suelo.{Colors.ENDC}")
            time.sleep(0.5)
            Utilidades.escribir_lento("No hay lesiones graves, pero tiene un esguince de muñeca.")
            print(f"\n{Colors.FAIL}❌ Puntuación -15 (podrías haberlo evitado){Colors.ENDC}")
            print(f"{Colors.WARNING}⚠️  Se ha producido un accidente laboral en tu primer día ... Te has metido en un buen lío.{Colors.ENDC}")
            juego.puntuacion -= 15
            juego.riesgos_detectados += 3
            
        elif decision == 3:
            # Enfoque pragmático - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n✅ Priorizas el riesgo inmediato de tropiezo.")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}Tú:{Colors.ENDC} 'Carlos, disculpa. Necesito que alguien de mantenimiento")
            print("venga ahora a asegurar estos cables. Es un riesgo de caída.'")
            time.sleep(0.5)
            print(f"\n{Colors.OKCYAN}Carlos:{Colors.ENDC} 'Por supuesto, enseguida llamo a mantenimiento. ¡Gracias por detectarlo! Ves como necesitamos ayuda.'")
            time.sleep(0.3)
            Utilidades.escribir_lento("\n🔧 En 10 minutos, los cables están asegurados con canaletas.")
            Utilidades.escribir_lento("Los empleados te lo agradecen con magdalenas. Has evitado un accidente.")
            print(f"\n{Colors.OKGREEN}✅ +10 Puntuación (decisión acertada){Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +3 Riesgos detectados{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +1 Situación crítica resuelta (toda la empresa protegida){Colors.ENDC}")
            juego.puntuacion += 10
            juego.riesgos_detectados += 3
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        else:
            # Enfoque pasivo - PEOR OPCIÓN
            Utilidades.escribir_lento("\n😐 Decides ir primero a tu oficina y organizarte el día...")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nA los 20 minutos, escuchas un fuerte ruido en el pasillo.")
            print(f"\n{Colors.FAIL}💥 ¡CRASH! Una empleada embarazada tropieza con los cables.{Colors.ENDC}")
            time.sleep(0.5)
            print(f"{Colors.FAIL}🚑 Necesita atención médica urgente. Está en shock.{Colors.ENDC}")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nEl director te llama inmediatamente a su despacho.")
            print(f"\n{Colors.FAIL}Director:{Colors.ENDC} '¿Viste esos cables y NO hiciste nada? ¿Para qué se suponen que estás aquí?'")
            print(f"\n{Colors.FAIL}❌ Puntuación -30 (negligencia grave){Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Has perdido credibilidad en la empresa y vas a tener que devolver tu PIN de master de la seguridad.{Colors.ENDC}")
            juego.puntuacion -= 30
        
        Utilidades.pausa()
    
    @staticmethod
    def escenario_puesto_trabajo():
        """Segunda escena - Inspección de puestos de trabajo"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 2: ZONA DE DESARROLLO ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Llega un momento del día en el que vas a buscar la cocina para comerte el Chucrut que has traido de cada, pero te pierdes por la empresa y entras en la sala principal donde trabajan 30 programadores.")
        Utilidades.escribir_lento("Es una sala diáfana con muchas estaciones de trabajo...")
        time.sleep(0.5)
        
        Utilidades.escribir_lento("\n🔍 Tu tercer ojo de observador te hacen ver varios problemas de ERGONOMÍA en la zona:")
        time.sleep(0.3)
        
        print(f"\n{Colors.WARNING}👨‍💻 Varios desarrolladores con el monitor demasiado bajo (usan portátiles){Colors.ENDC}")
        print(f"{Colors.WARNING}🪑 Sillas de oficina básicas sin regulación lumbar{Colors.ENDC}")
        print(f"{Colors.WARNING}💡 Reflejos en pantallas por ventanas sin cortinas{Colors.ENDC}")
        print(f"{Colors.WARNING}🖱️ Varios trabajadores con la muñeca en mala posición{Colors.ENDC}")
        print(f"{Colors.WARNING}❄️ El aire acondicionado apunta directo a algunas mesas{Colors.ENDC}")
        
        time.sleep(0.5)
        Utilidades.escribir_lento("\nTe acercas a un desarrollador que lleva auriculares.")
        Utilidades.escribir_lento("Está encorvado sobre su portátil. Parece incómodo.")
        
        print(f"\n{Colors.OKCYAN}Desarrollador (Miguel):{Colors.ENDC} 'Hola, ¿tú eres el nuevo de prevención?'")
        print(f"{Colors.OKCYAN}Miguel:{Colors.ENDC} 'Me duele mucho el cuello últimamente. ¿Es normal?'")
        
        print("\n¿Qué haces?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Evaluar su puesto ahora y darle recomendaciones inmediatas para que no acabe como una alcayata")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Pedirle que rellene un formulario de solicitud de evaluación de su zona de trabajo")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Hacer una evaluación ergonómica completa de TODA la sala")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Decirle que consulte al médico de empresa primero ... que tú no eres fisioterapeuta")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_puesto_trabajo(decision, juego):
        """Procesa la decisión del puesto de trabajo"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Evaluación inmediata - BUENA OPCIÓN
            Utilidades.escribir_lento("\n✅ Te sientas con Miguel y evalúas su puesto de trabajo.")
            time.sleep(0.3)
            Utilidades.escribir_lento("\nIdentificas los problemas:")
            print(f"\n• Monitor a 25 cm por debajo del nivel de los ojos")
            print(f"• Silla sin soporte lumbar adecuado")
            print(f"• Teclado y ratón demasiado altos (tensión en hombros)")
            print(f"• Sin reposapiés (Miguel mide 1,45m)")
            time.sleep(0.5)
            Utilidades.escribir_lento("\n📝 Le das recomendaciones según el RD 488/1997 (pantallas de visualización):")
            time.sleep(0.3)
            print(f"\n✓ Solicitas un soporte elevador para el portátil de Miguel")
            print(f"✓ También pides un teclado y un ratón USB para el portátil de Miguel")
            print(f"✓ Además le consigues un reposapiés regulable")
            print(f"✓ Le enseñas la regla 20-20-6 (cada 20 min, mirar 20 seg a 6 metros de distancia)")
            time.sleep(0.5)
            print(f"\n{Colors.OKCYAN}Miguel:{Colors.ENDC} '¡Gracias! Nadie me había explicado esto antes.'")
            print(f"\n{Colors.OKGREEN}✅ +15 Puntuación (atención personalizada y técnica){Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +1 Riesgo detectado y solucionado{Colors.ENDC}")
            juego.puntuacion += 15
            juego.riesgos_detectados += 1
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 2:
            # Burocracia
            Utilidades.escribir_lento("\n📄 Le das un formulario de 3 páginas para rellenar...")
            time.sleep(0.5)
            print(f"\n{Colors.OKCYAN}Miguel:{Colors.ENDC} 'Oh... ¿En serio? Estoy en medio de un problema gordisimo...'")
            Utilidades.escribir_lento("\nMiguel parece frustrado. Deja el formulario en la mesa.")
            time.sleep(0.3)
            Utilidades.escribir_lento("Probablemente nunca lo rellene.")
            print(f"\n{Colors.FAIL}❌ Puntuación -5 (exceso de burocracia innecesaria){Colors.ENDC}")
            juego.puntuacion -= 5
            
        elif decision == 3:
            # Evaluación completa - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n🎯 Decides hacer una evaluación ergonómica sistemática de toda la sala.")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}Tú:{Colors.ENDC} 'Miguel, voy a ayudarte, pero primero necesito")
            print("hacer una evaluación completa de todos los puestos para priorizar.'")
            time.sleep(0.5)
            Utilidades.escribir_lento("\n📊 Pasas las siguientes 3 horas evaluando los 30 puestos.")
            Utilidades.escribir_lento("Documentas todo con fotos y mediciones.")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nResultados:")
            print(f"\n• 25 puestos con riesgo ergonómico ALTO")
            print(f"• 5 puestos con riesgo MEDIO")
            print(f"• 0 puestos conformes con el RD 488/1997")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nPrepararas un informe detallado con presupuesto:")
            print(f"\n💰 Inversión necesaria: 10.000€ en equipamiento ergonómico")
            print(f"📉 Ahorro estimado en bajas: INCALCULABLE")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ +25 Puntuación (evaluación profesional y completa){Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +30 Riesgos detectados{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +30 Situación crítica resuelta{Colors.ENDC}")
            juego.puntuacion += 25
            juego.riesgos_detectados += 30
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        else:
            # Derivar al médico
            Utilidades.escribir_lento("\n🏥 Le dices a Miguel que vaya al médico de empresa... que tú no eres fisioterapeuta")
            time.sleep(0.5)
            print(f"\n{Colors.OKCYAN}Miguel:{Colors.ENDC} '¿El médico? Pero si es mi puesto de trabajo el problema...'")
            time.sleep(0.3)
            Utilidades.escribir_lento("\nMiguel se siente ignorado. El problema no se soluciona y Miguel ya no te va a ajuntar para jugar al Chinchón en la fiesta de Navidad de la empresa.")
            print(f"\n{Colors.WARNING}⚠️  No has abordado la causa raíz del problema{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Puntuación -10 (derivación inadecuada){Colors.ENDC}")
            juego.puntuacion -= 10
        
        Utilidades.pausa()
    
    @staticmethod
    def escenario_emergencia():
        """Tercera escena - Situación de emergencia"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 3: EMERGENCIA ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Es tu tercer día en la empresa. Son las 11:30 de la mañana... La hora punta de trabajo.")
        time.sleep(0.5)
        Utilidades.escribir_lento("\nDe repente...")
        time.sleep(1)
        
        print(f"\n{Colors.FAIL}{Colors.BOLD}🔥🔥🔥 ¡¡¡BEEP BEEP BEEP!!! 🔥🔥🔥{Colors.ENDC}")
        print(f"\n{Colors.FAIL}¡ALARMA DE INCENDIOS!{Colors.ENDC}")
        time.sleep(0.5)
        
        Utilidades.escribir_lento("\nVes humo saliendo del cuarto de servidores... y tú sabes que allí solo cocinan los martes.")
        Utilidades.escribir_lento("La gente empieza a levantarse confusa. Algunos siguen trabajando con los auriculares puestos.")
        time.sleep(0.5)
        
        print(f"\n{Colors.WARNING}📱 Varios empleados están cogiendo sus móviles y mochilas.{Colors.ENDC}")
        print(f"{Colors.WARNING}🚪 La gente va hacia el ascensor.{Colors.ENDC}")
        print(f"{Colors.WARNING}😰 Hay nerviosismo pero no pánico... todavía.{Colors.ENDC}")
        
        time.sleep(0.5)
        Utilidades.escribir_lento("\nRecuerdas que la empresa NO tiene plan de evacuación implementado.")
        Utilidades.escribir_lento("No hay responsables de evacuación. No hay punto de encuentro definido.")
        
        print(f"\n{Colors.BOLD}¿QUÉ HACES?{Colors.ENDC}")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Gritar 'EVACUACIÓN' y dirigir a la gente hacia las escaleras")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Ir al cuarto de servidores a ver qué está pasando ... y si alguien está cocinando algo rico, pedirle un poco")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Llamar al 112 primero y luego coordinar evacuación")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Buscar extintores e intentar apagar el fuego como el héroe que eres")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_emergencia(decision, juego):
        """Procesa la decisión de emergencia"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Evacuar directamente - BUENA
            Utilidades.escribir_lento(f"\n📢 Gritas con autoridad: '¡EVACUACIÓN! ¡ESCALERAS, NO ASCENSOR! ¡LAS MUJERES Y YO PRIMERO!'")
            time.sleep(0.5)
            Utilidades.escribir_lento("\n🏃 Diriges a la gente hacia las salidas de emergencia.")
            Utilidades.escribir_lento("Impides que usen el ascensor... Es el momento de hacer cardio por las escaleras.")
            Utilidades.escribir_lento("Revisas rápidamente que no quede nadie en los baños.")
            time.sleep(0.5)
            Utilidades.escribir_lento("\n✅ En 4 minutos, las 50 personas están fuera del edificio. Es posible que tengáis un récord de tiempo al sacar a tanta gente tan rápido.")
            time.sleep(0.3)
            Utilidades.escribir_lento("Los bomberos llegan a los 8 minutos.")
            Utilidades.escribir_lento("Era un fallo eléctrico en un SAI. El fuego comenzó en el rack. Pero la merienda de la gente se ha salvado. Nadie ha resultado herido.")
            print(f"\n{Colors.OKGREEN}✅ +20 Puntuación (evacuación efectiva){Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +50 Trabajadores salvados{Colors.ENDC}")
            juego.puntuacion += 20
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 2:
            # Ir a investigar - PELIGROSO
            Utilidades.escribir_lento("\n🏃 Corres hacia el cuarto de servidores...")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nAbres la puerta y entra una bocanada de humo negro.")
            print(f"\n{Colors.FAIL}💨 Empiezas a toser violentamente. La visibilidad es casi nula.{Colors.ENDC}")
            time.sleep(0.5)
            Utilidades.escribir_lento("Ves llamas en uno de los racks de servidores.")
            time.sleep(0.3)
            print(f"\n{Colors.FAIL}⚠️  GRAVE ERROR: Estás poniendo tu vida en riesgo.{Colors.ENDC}")
            print(f"{Colors.FAIL}Según la Ley 31/1995: Solo personal formado y equipado{Colors.ENDC}")
            print(f"{Colors.FAIL}puede intervenir en situaciones de riesgo grave e inminente. El resto tiene que sacarse de enmedio.{Colors.ENDC}")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nUn compañero te saca de allí antes de que inhales más humo. Por que ese humo no es de la marca de tabaco que fumas a escondidas en el baño de la empresa.")
            print(f"\n{Colors.FAIL}❌ Puntuación -20 (imprudencia grave){Colors.ENDC}")
            print(f"{Colors.WARNING}🏥 Necesitas atención médica por inhalación de humo. Te vas 4 días de baja.{Colors.ENDC}")
            juego.puntuacion -= 20
            
        elif decision == 3:
            # Llamar 112 y evacuar - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n📞 Marcas el 112 mientras caminas hacia la zona de trabajo.")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}Tú:{Colors.ENDC} '112, incendio en oficinas, 2º piso Calle Más Mayor 45.'")
            print(f"{Colors.BOLD}Tú:{Colors.ENDC} '50 personas, humo en sala de servidores. Evacuando ahora.'")
            time.sleep(0.5)
            Utilidades.escribir_lento("\n📢 Mientras hablas, indicas a la gente que evacue por escaleras haciendo signos con las manos.")
            Utilidades.escribir_lento("Delegas en dos personas para que cierren las puertas tras salir.")
            time.sleep(0.5)
            Utilidades.escribir_lento("\n✅ Evacuación coordinada en 5 minutos. Eres un crack!! ... te dice tu jefe.")
            Utilidades.escribir_lento("Los bomberos llegan en 6 minutos con todos los medios y la información necesaria.")
            Utilidades.escribir_lento("El fuego se controla rápidamente. No hay heridos.")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ +30 Puntuación (gestión ÓPTIMA de emergencia){Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +50 Trabajadores salvados{Colors.ENDC}")
            print(f"{Colors.OKGREEN}🏆 Has seguido el protocolo de emergencias correctamente ... aun que la empresa no lo tenga implementado ...{Colors.ENDC}")
            juego.puntuacion += 30
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        else:
            # Buscar extintor - ARRIESGADO
            Utilidades.escribir_lento("\n🧯 Buscas un extintor por los pasillos...")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nEncuentras uno. Es de CO2.")
            Utilidades.escribir_lento("Corres hacia el cuarto de servidores.")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nAbres la puerta... El humo es denso.")
            time.sleep(0.3)
            print(f"\n{Colors.WARNING}⚠️  Intentas apagar el fuego pero el humo te supera.{Colors.ENDC}")
            print(f"{Colors.WARNING}El extintor se vacía rápido debido a las carreras que algunos empleados realizan los vieres para salir antes del trabajo. El fuego no se apaga completamente.{Colors.ENDC}")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nMientras tanto, la gente evacua sin coordinación.")
            Utilidades.escribir_lento("Dos personas usan el ascensor (lo cual es un peligro si se queda sin luz). Podrían terminar cocinados como en un horno.")
            print(f"\n{Colors.FAIL}❌ Puntuación -15 (heroicidad innecesaria y descoordinación){Colors.ENDC}")
            print(f"{Colors.WARNING}⚠️  Los bomberos indican que pusiste tu vida en riesgo innecesariamente{Colors.ENDC}")
            juego.puntuacion -= 15
        
        Utilidades.pausa()
    
    @staticmethod
    def escenario_climatizacion():
        """Quinta escena - Problemas de climatización"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 4: TEMPERATURA EXTREMA ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Es pleno verano. Entras a la sala de desarrollo y hace un calor sofocante.")
        time.sleep(0.3)
        Utilidades.escribir_lento("El aire acondicionado lleva 3 días estropeado.")
        time.sleep(0.5)
        
        print(f"\n{Colors.WARNING}🌡️ El termómetro marca 35°C dentro de la oficina{Colors.ENDC}")
        print(f"{Colors.WARNING}💧 Varios empleados están sudando visiblemente{Colors.ENDC}")
        print(f"{Colors.WARNING}😰 Ana se queja de mareos y dolor de cabeza{Colors.ENDC}")
        
        time.sleep(0.5)
        print(f"\n{Colors.OKCYAN}Pedro (desarrollador):{Colors.ENDC} 'Llevamos así 3 días. Es insoportable.'")
        print(f"{Colors.OKCYAN}Ana:{Colors.ENDC} 'Me encuentro muy mal... creo que es un golpe de calor.'")
        
        print("\n¿Qué decides hacer?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Ordenar evacuación inmediata y ordenar el trabajo remoto hasta arreglarlo")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Llevar ventiladores y agua fría mientras se arregla")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Atender a Ana primero y luego evaluar la situación")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Hablar con mantenimiento para que aceleren la reparación")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_climatizacion(decision, juego):
        """Procesa la decisión de climatización"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Teletrabajo + apagar servicios - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n🏠 Ordenas teletrabajo inmediato y que se ejecute el protocolo de emergencia IT.")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}Tú:{Colors.ENDC} 'Según la LEY sobre lugares de trabajo,")
            print("la temperatura debe estar entre 15-25°C. Estamos a 35°C.'")
            time.sleep(0.5)
            Utilidades.escribir_lento("\n'Además, los servidores están en riesgo. Se debe realizar un migración urgente a la nube.'")
            time.sleep(0.3)
            print(f"\n{Colors.OKGREEN}✅ DevOps migran servicios críticos a AWS (si es que no está caido el servicio) temporalmente{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ El equipo agradece poder teletrabajar{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Ana se recupera en casa sin consecuencias{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +15 Puntuación (decisión correcta técnica y legal){Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +2 Riesgos detectados{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +50 Situación crítica resuelta{Colors.ENDC}")
            juego.puntuacion += 15
            juego.riesgos_detectados += 2
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 2:
            # Ventiladores
            Utilidades.escribir_lento("\n🌀 Compras ventiladores y agua de Valencia fría de urgencia.")
            time.sleep(0.3)
            Utilidades.escribir_lento("Reduces la temperatura a 29°C, pero sigue siendo excesiva para trabajar.")
            time.sleep(0.5)
            print(f"\n{Colors.WARNING}⚠️  Ana empeora y tiene que irse a urgencias{Colors.ENDC}")
            print(f"{Colors.WARNING}⚠️  El equipo sigue incómodo{Colors.ENDC}")
            time.sleep(0.3)
            print(f"\n{Colors.WARNING}⚠️  Puntuación +3 (solución insuficiente){Colors.ENDC}")
            juego.puntuacion += 3
            juego.riesgos_detectados += 2
            
        elif decision == 3:
            # Atender a Ana
            Utilidades.escribir_lento("\n🚑 Atiendes a Ana inmediatamente.")
            time.sleep(0.3)
            Utilidades.escribir_lento("Le das agua fría y la llevas a un lugar fresco.")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ Ana se recupera{Colors.ENDC}")
            print(f"\n{Colors.WARNING}⚠️  Pero el resto del equipo sigue sufriendo el calor{Colors.ENDC}")
            time.sleep(0.3)
            print(f"\n{Colors.WARNING}⚠️  Puntuación +8 (acción humana pero incompleta){Colors.ENDC}")
            juego.puntuacion += 8
            juego.riesgos_detectados += 1
            juego.trabajadores_salvados += 1
            
        else:
            # Hablar con mantenimiento
            Utilidades.escribir_lento("\n📞 Llamas a mantenimiento para presionar...")
            time.sleep(0.3)
            print(f"\n{Colors.OKCYAN}Mantenimiento:{Colors.ENDC} 'La pieza llega mañana de Alemania, no podemos hacer más.'")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nMientras tanto, 3 empleados tienen que irse por malestar.")
            print(f"\n{Colors.FAIL}❌ Puntuación -5 (no has tomado medidas inmediatas){Colors.ENDC}")
            juego.puntuacion -= 5
            
        Utilidades.pausa()
    
    @staticmethod
    def escenario_acoso():
        """Sexta escena - Denuncia de acoso laboral"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 5: RIESGOS PSICOSOCIALES ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Laura, una desarrolladora junior, solicita hablar contigo en privado.")
        time.sleep(0.3)
        Utilidades.escribir_lento("Está visiblemente nerviosa y alterada.")
        time.sleep(0.5)
        
        print(f"\n{Colors.OKCYAN}Laura:{Colors.ENDC} 'No sé si debería decir esto pero...'")
        time.sleep(0.3)
        print(f"{Colors.OKCYAN}Laura:{Colors.ENDC} 'Mi jefe de equipo hace comentarios inapropiados constantemente.'")
        print(f"{Colors.OKCYAN}Laura:{Colors.ENDC} 'Me siento muy incómoda. Me afecta incluso fuera del trabajo.'")
        time.sleep(0.5)
        
        print(f"\n{Colors.WARNING}😰 Laura muestra signos de estrés severo{Colors.ENDC}")
        print(f"{Colors.WARNING}⚠️  Riesgo psicosocial grave{Colors.ENDC}")
        
        print("\n¿Cómo actúas?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Activar protocolo de acoso, documento formal y suspender al acusado")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Hablar informalmente con el jefe primero antes de escalar el problema a los superiores")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Documentarlo todo y elevar a RRHH inmediatamente")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Aconsejar a Laura que lo hable directamente con su jefe")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_acoso(decision, juego):
        """Procesa la decisión de acoso"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Protocolo formal - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n📋 Activas el protocolo de acoso laboral inmediatamente.")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}Acciones tomadas:{Colors.ENDC}")
            print("1. Documento formal de la denuncia con Laura")
            print("2. Comunicación inmediata a RRHH y Dirección")
            print("3. Suspensión cautelar del acusado mientras se investiga")
            print("4. Apoyo psicológico para Laura")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ Laura se siente protegida y apoyada{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Cumples con la Ley 31/1995 sobre riesgos psicosociales{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +20 Puntuación (gestión profesional y legal){Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ +3 Riesgos detectados{Colors.ENDC}")
            juego.puntuacion += 20
            juego.riesgos_detectados += 3
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 2:
            # Hablar informal - MALA OPCIÓN
            Utilidades.escribir_lento("\n🗣️ Decides hablar informalmente con el jefe acusado...")
            time.sleep(0.3)
            print(f"\n{Colors.OKCYAN}Jefe Tech:{Colors.ENDC} '¿Qué? ¡Solo bromeaba! Es parte de la cultura del equipo.'")
            print(f"{Colors.OKCYAN}Jefe Tech:{Colors.ENDC} 'Laura es muy sensible para trabajar en desarrollo.'")
            time.sleep(0.5)
            Utilidades.escribir_lento("\nEl jefe tech se entera de quién denunció y aumenta la presión sobre Laura.")
            print(f"\n{Colors.FAIL}❌ Laura se siente traicionada y presenta baja por ansiedad{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ El equipo de desarrollo pierde confianza en ti y ya no te traen café{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -20 (gestión totalmente inadecuada){Colors.ENDC}")
            juego.puntuacion -= 20
            
        elif decision == 3:
            # RRHH - BUENA OPCIÓN
            Utilidades.escribir_lento("\n📄 Documentas todo y elevas el caso a RRHH inmediatamente.")
            time.sleep(0.3)
            Utilidades.escribir_lento("RRHH activa el protocolo de investigación.")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ El caso se gestiona correctamente{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +15 Puntuación (procedimiento correcto){Colors.ENDC}")
            juego.puntuacion += 15
            juego.riesgos_detectados += 3
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        else:
            # Derivar a Laura - PEOR OPCIÓN
            Utilidades.escribir_lento("\n😔 Le aconsejas a Laura que lo hable con su jefe directamente...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ Laura se siente desprotegida y abandona la empresa{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Pierdes una desarrolladora con gran potencial{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Laura presenta denuncia legal contra la empresa{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -25 (incumplimiento grave de PRL){Colors.ENDC}")
            juego.puntuacion -= 25
            
        Utilidades.pausa()
    
    @staticmethod
    def escenario_pantallas():
        """Séptima escena - Fatiga visual y pantallas"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 6: SALUD VISUAL ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Realizas una evaluación de los puestos con pantallas de visualización.")
        time.sleep(0.3)
        Utilidades.escribir_lento("El RD 488/1997 regula el trabajo con pantallas.")
        time.sleep(0.5)
        
        print(f"\n{Colors.WARNING}💻 El 80% del equipo trabaja más de 4h/día con pantallas{Colors.ENDC}")
        print(f"{Colors.WARNING}😫 Muchos se quejan de fatiga visual, ojos secos, dolores de cabeza{Colors.ENDC}")
        print(f"{Colors.WARNING}🕐 Nadie hace pausas reglamentarias{Colors.ENDC}")
        print(f"{Colors.WARNING}💡 La iluminación es inadecuada, con reflejos en pantallas{Colors.ENDC}")
        
        time.sleep(0.5)
        print(f"\n{Colors.OKCYAN}Miguel:{Colors.ENDC} 'Mis ojos arden al final del día. A veces veo borroso.'")
        
        print("\n¿Qué medidas implementas?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Solo recordatorio de hacer pausas cada 20 minutos")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Revisiones oftalmológicas gratuitas + pausas obligatorias")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Plan completo: revisiones + pausas + filtros + iluminación")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Nada por ahora, es responsabilidad individual del trabajador")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_pantallas(decision, juego):
        """Procesa la decisión de pantallas"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Solo pausas
            Utilidades.escribir_lento("\n⏰ Envías un email recordando hacer pausas cada 20 minutos.")
            time.sleep(0.3)
            Utilidades.escribir_lento("La mayoría lo ignora por presión de trabajo.")
            time.sleep(0.5)
            print(f"\n{Colors.WARNING}⚠️  Los problemas visuales continúan{Colors.ENDC}")
            print(f"\n{Colors.WARNING}⚠️  Puntuación +3 (medida insuficiente){Colors.ENDC}")
            juego.puntuacion += 3
            juego.riesgos_detectados += 1
            
        elif decision == 2:
            # Revisiones + pausas
            Utilidades.escribir_lento("\n👁️ Implementas un programa de salud visual:")
            time.sleep(0.3)
            print(f"\n• Revisiones oftalmológicas anuales gratuitas")
            print(f"• Implementas un software en cada equipo que fuerza pausas cada 20 min (regla 20-20-20)")
            print(f"• Buscas gafas de descanso cubiertas, si el oftalmólogo lo recomienda")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ El equipo lo valora positivamente{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +12 Puntuación (buenas medidas){Colors.ENDC}")
            juego.puntuacion += 12
            juego.riesgos_detectados += 4
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 3:
            # Plan completo - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n🏆 Implementas un plan integral de salud visual:")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}MEDIDAS TÉCNICAS:{Colors.ENDC}")
            print("• Filtros antirreflejos para todas las pantallas")
            print("• Mejora de iluminación eliminando reflejos")
            print("• Monitores ajustables en altura y distancia")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}MEDIDAS ORGANIZATIVAS:{Colors.ENDC}")
            print("• Software de pausas obligatorias cada 20 min")
            print("• Protocolo 20-20-6: cada 20 min, mirar 20 seg a 6 metros de distancia")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}VIGILANCIA DE LA SALUD:{Colors.ENDC}")
            print("• Revisiones oftalmológicas anuales")
            print("• Gafas específicas cubiertas al 100%")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ Cumplimiento total del RD que regula este problema{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Reducción del 70% en quejas de fatiga visual{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +20 Puntuación (plan excelente){Colors.ENDC}")
            juego.puntuacion += 20
            juego.riesgos_detectados += 4
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        else:
            # Nada
            Utilidades.escribir_lento("\n😐 Decides que es responsabilidad de cada empleado...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ Incumples el RD que regula este problema{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ 5 empleados desarrollan problemas visuales graves{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -15 (negligencia){Colors.ENDC}")
            juego.puntuacion -= 15
            
        Utilidades.pausa()
    
    @staticmethod
    def escenario_covid():
        """Octava escena - Brote de COVID en la oficina"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 7: RIESGO BIOLÓGICO ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Lunes por la mañana. Recibes 3 llamadas urgentes:")
        time.sleep(0.3)
        Utilidades.escribir_lento("Tres empleados que trabajaron juntos la semana pasada tienen COVID-19 por lamer la misma ventana.")
        time.sleep(0.5)
        
        print(f"\n{Colors.WARNING}🦠 Posible brote en la oficina{Colors.ENDC}")
        print(f"{Colors.WARNING}👥 15 personas estuvieron en contacto cercano{Colors.ENDC}")
        print(f"{Colors.WARNING}🏢 La oficina estuvo abierta toda la semana{Colors.ENDC}")
        
        time.sleep(0.5)
        print(f"\n{Colors.OKCYAN}CEO:{Colors.ENDC} 'Tenemos un deadline importante. ¿Podemos seguir trabajando?'")
        
        print("\n¿Cuál es tu decisión inmediata?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Cierre total 5 días + test a todos + desinfección profunda")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Solo los contactos directos a casa, el resto tendrá que seguir trabajando")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Teletrabajo obligatorio 2 semanas para todos")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Continuar de forma normal utilizando mascarillas obligatorias todo el mundo")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_covid(decision, juego):
        """Procesa la decisión de COVID"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Cierre total - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n🔒 Cierras la oficina completamente durante 5 días.")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}Plan de acción:{Colors.ENDC}")
            print("1. Test PCR a todos los empleados")
            print("2. Rastreo de contactos")
            print("3. Desinfección profesional de toda la oficina")
            print("4. Revisión del protocolo de prevención")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ Se detectan 2 positivos asintomáticos adicionales{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Se evita un brote mayor{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +25 Puntuación (gestión ejemplar){Colors.ENDC}")
            juego.puntuacion += 25
            juego.riesgos_detectados += 1
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 2:
            # Solo contactos
            Utilidades.escribir_lento("\n🏠 Envías a casa solo a los 15 contactos directos...")
            time.sleep(0.5)
            print(f"\n{Colors.WARNING}⚠️  3 días después, aparecen 4 nuevos positivos{Colors.ENDC}")
            print(f"{Colors.WARNING}⚠️  Uno de ellos tiene que ser hospitalizado{Colors.ENDC}")
            time.sleep(0.3)
            print(f"\n{Colors.FAIL}❌ Puntuación -10 (medida insuficiente){Colors.ENDC}")
            juego.puntuacion -= 10
            
        elif decision == 3:
            # Teletrabajo total - BUENA OPCIÓN
            Utilidades.escribir_lento("\n💻 Teletrabajo obligatorio para todos durante 2 semanas.")
            time.sleep(0.3)
            Utilidades.escribir_lento("Organizas tests y seguimiento remoto.")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ Se contiene el brote{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ No hay nuevos contagios laborales{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +18 Puntuación (buena gestión){Colors.ENDC}")
            juego.puntuacion += 18
            juego.riesgos_detectados += 1
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        else:
            # Continuar - PEOR OPCIÓN
            Utilidades.escribir_lento("\n😷 Decides continuar con mascarillas obligatorias...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ A la semana, 12 empleados están enfermos{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Uno de ellos con secuelas graves{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Inspección de Trabajo abre expediente{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -30 (negligencia grave){Colors.ENDC}")
            juego.puntuacion -= 30
            
        Utilidades.pausa()
    
    @staticmethod
    def escenario_estres():
        """Novena escena - Burnout y estrés del equipo"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 8: QUEMADOS ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("El equipo lleva 3 meses en modo 'crisis permanente'.")
        time.sleep(0.3)
        Utilidades.escribir_lento("Jornadas de 10-12 horas, fines de semana trabajando, la presión es constante.")
        time.sleep(0.5)
        
        print(f"\n{Colors.WARNING}😫 4 empleados están de baja por ansiedad/depresión{Colors.ENDC}")
        print(f"{Colors.WARNING}💔 2 han dimitido en el último mes{Colors.ENDC}")
        print(f"{Colors.WARNING}⚡ Ambiente está tens. Los conflictos son frecuentes{Colors.ENDC}")
        print(f"{Colors.WARNING}😴 Se ven síntomas de agotamiento generalizado{Colors.ENDC}")
        
        time.sleep(0.5)
        print(f"\n{Colors.OKCYAN}Desarrolladora:{Colors.ENDC} 'No puedo más. Me despierto con ansiedad.'")
        print(f"{Colors.OKCYAN}PM:{Colors.ENDC} 'Si no entregamos, perdemos el cliente más grande.'")
        
        print("\n¿Cómo gestionas esta situación?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Evaluación de riesgos psicosociales + plan de acción urgente")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Contratar más personal para reducir carga inmediatamente")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Sesiones de mindfulness y apoyo psicológico")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Pedir que aguanten hasta entregar el proyecto")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_estres(decision, juego):
        """Procesa la decisión de estrés"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Evaluación formal - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n📊 Realizas una evaluación de riesgos psicosociales formal.")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}Acciones implementadas:{Colors.ENDC}")
            print("1. Utilizas algún método para evaluación del equipo técnico")
            print("2. Límite estricto: jornadas máx 8h, no deployments en fines de semana")
            print("3. Fuera del horario solo se corrigen los bug críticos")
            print("4. Contratación de 3 desarrolladores de refuerzo")
            print("5. Renegociación de plazos con cliente")
            print("6. Apoyo psicológico profesional especializado en IT")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ En 2 meses, el ambiente mejora drásticamente{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Bugs reducidos un 70%, velocidad de desarrollo estable{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Cero bajas nuevas por salud mental{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +30 Puntuación (intervención excelente){Colors.ENDC}")
            juego.puntuacion += 30
            juego.riesgos_detectados += 5
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 2:
            # Contratar
            Utilidades.escribir_lento("\n👥 Consigues aprobar la contratación de 4 desarrolladores nuevos.")
            time.sleep(0.3)
            Utilidades.escribir_lento("La carga se reduce, pero el ponerlos al día consume el tiempo del equipo que sigue quemado.")
            time.sleep(0.5)
            print(f"\n{Colors.WARNING}⚠️  3 seniors dimiten igualmente ('ya es tarde'){Colors.ENDC}")
            print(f"{Colors.WARNING}⚠️  Pérdida de conocimiento crítico en el desarrollo{Colors.ENDC}")
            print(f"\n{Colors.WARNING}⚠️  Puntuación +10 (medida necesaria pero tardía){Colors.ENDC}")
            juego.puntuacion += 10
            juego.riesgos_detectados += 2
            juego.trabajadores_salvados += 1
            
        elif decision == 3:
            # Mindfulness
            Utilidades.escribir_lento("\n🧘 Implementas sesiones de mindfulness y apoyo psicológico.")
            time.sleep(0.3)
            Utilidades.escribir_lento("Pero no reduces la carga de trabajo ni los deadlines imposibles...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ El equipo lo ve como 'lavado de cara'{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ 'No necesito yoga, necesito menos bugs que arreglar'{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ La rotación de desarrolladores sigue aumentando{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -5 (solución superficial){Colors.ENDC}")
            juego.puntuacion -= 5
            
        else:
            # Aguantar - PEOR OPCIÓN
            Utilidades.escribir_lento("\n😔 Pides al equipo que aguante 'un sprint más'...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ 6 desarrolladores dimiten en masa{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ El proyecto colapsa por falta de personal{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ 1 intento de suicidio (afortunadamente fallido){Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Inspección de Trabajo + denuncia pública en redes{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -40 (negligencia gravísima){Colors.ENDC}")
            juego.puntuacion -= 40
            
        Utilidades.pausa()
    
    @staticmethod
    def escenario_teletrabajo():
        """Décima escena - Riesgos del teletrabajo"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 9: TELETRABAJO ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Post-pandemia: 30 empleados trabajan permanentemente desde casa.")
        time.sleep(0.3)
        Utilidades.escribir_lento("Empiezas a recibir quejas sobre sus condiciones de trabajo en casa.")
        time.sleep(0.5)
        
        print(f"\n{Colors.WARNING}🏠 Muchos trabajan desde el sofá o la cama{Colors.ENDC}")
        print(f"{Colors.WARNING}💻 Usan portátiles sin equipamiento ergonómico{Colors.ENDC}")
        print(f"{Colors.WARNING}📶 Varios tienen mala conexión a internet{Colors.ENDC}")
        print(f"{Colors.WARNING}⏰ Dificultad para desconectar (disponibilidad 24/7){Colors.ENDC}")
        
        time.sleep(0.5)
        print(f"\n{Colors.OKCYAN}Carlos:{Colors.ENDC} 'Tengo dolores de espalda horribles desde que trabajo en casa.'")
        print(f"{Colors.OKCYAN}Ana:{Colors.ENDC} 'Trabajo más horas que en la oficina, estoy agotada.'")
        
        print("\n¿Qué programa implementas para el teletrabajo?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Auditorías virtuales + equipamiento ergonómico + derecho a desconexión")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Solo enviar una guía de buenas prácticas por email")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Volver a la oficina obligatoriamente")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Es su casa, es su responsabilidad")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_teletrabajo(decision, juego):
        """Procesa la decisión de teletrabajo"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Programa completo - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n🏆 Implementas un programa integral de teletrabajo seguro para desarrolladores:")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}1. AUDITORÍAS VIRTUALES:{Colors.ENDC}")
            print("• Videollamadas individuales para evaluar el home office")
            print("• Checklist de seguridad y ergonomía para desarrolladores")
            print("• Revisión del setup técnico (pantallas, conexión, etc.)")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}2. EQUIPAMIENTO TÉCNICO:{Colors.ENDC}")
            print("• Silla ergonómica Herman Miller")
            print("• Monitor 27' 4K + soporte para portátil")
            print("• Teclado mecánico ergonómico + ratón vertical")
            print("• Mejora conexión internet (100Mbps simétricos)")
            print("• Reembolso internet y electricidad (40€/mes)")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}3. ORGANIZACIÓN DEL TRABAJO:{Colors.ENDC}")
            print("• Sin emails después de las 19h")
            print("• Sin reuniones antes de las 9h ni después de las 18h")
            print("• Pausas obligatorias cada 90 min (Pomodoro)")
            print("• 1 día/semana opcional en oficina. Para no olvidarse de las caras de sus compañeros.")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ Satisfacción del equipo dev sube al 95%{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Productividad aumenta un 20%{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Cero quejas ergonómicas, mejor code quality{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +25 Puntuación (programa ejemplar){Colors.ENDC}")
            juego.puntuacion += 25
            juego.riesgos_detectados += 4
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 2:
            # Guía por email
            Utilidades.escribir_lento("\n📧 Envías una guía en PDF sobre ergonomía en casa...")
            time.sleep(0.3)
            Utilidades.escribir_lento("La mayoría ni la lee.")
            time.sleep(0.5)
            print(f"\n{Colors.WARNING}⚠️  Los problemas continúan{Colors.ENDC}")
            print(f"{Colors.WARNING}⚠️  5 bajas por problemas musculoesqueléticos{Colors.ENDC}")
            print(f"\n{Colors.WARNING}⚠️  Puntuación +2 (esfuerzo mínimo){Colors.ENDC}")
            juego.puntuacion += 2
            
        elif decision == 3:
            # Volver a oficina
            Utilidades.escribir_lento("\n🏢 Ordenas volver a la oficina a todos los desarrolladores...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ 10 desarrolladores senior dimiten (se van a empresas que priorizan el trabajo remoto){Colors.ENDC}")
            print(f"{Colors.FAIL}❌ 'Quiero trabajar desde casa, me voy a otra empresa'{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Pérdida de talento crítico y altos costes de contratación{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Los que se quedan están descontentos{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -15 (decisión contraproducente en IT){Colors.ENDC}")
            juego.puntuacion -= 15
            
        else:
            # Es su responsabilidad
            Utilidades.escribir_lento("\n😐 'Es su casa, su responsabilidad'...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ Incumples la Ley 31/1995 ( que también aplica en teletrabajo){Colors.ENDC}")
            print(f"{Colors.FAIL}❌ 3 empleados con lesiones graves{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Inspección de Trabajo: multa de 40.000€{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -25 (negligencia legal){Colors.ENDC}")
            juego.puntuacion -= 25
            
        Utilidades.pausa()
    
    @staticmethod
    def escenario_productos_quimicos():
        """Undécima escena - Productos de limpieza peligrosos"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 10: RIESGO QUÍMICO ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("La empresa de limpieza ha cambiado sus productos.")
        time.sleep(0.3)
        Utilidades.escribir_lento("Varios empleados reportan irritación de ojos, tos y dolor de cabeza.")
        time.sleep(0.5)
        
        print(f"\n{Colors.WARNING}🧪 Los productos están sin ficha de datos de seguridad{Colors.ENDC}")
        print(f"{Colors.WARNING}😷 Dejar un olor fuerte a químicos en la oficina{Colors.ENDC}")
        print(f"{Colors.WARNING}🤧 5 personas con síntomas respiratorios{Colors.ENDC}")
        print(f"{Colors.WARNING}⚠️ Botellas sin etiquetar correctamente{Colors.ENDC}")
        
        time.sleep(0.5)
        print(f"\n{Colors.OKCYAN}Empleada limpieza:{Colors.ENDC} 'Me pican las manos, pero me dijeron que son buenos productos.'")
        
        print("\n¿Qué haces?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Suspender uso inmediato + exigir Fichas de Datos de Seguridad + evaluación de riesgos")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Abrir las ventanas y mejorar la ventilación")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Pedir a limpieza que use menos producto")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Esperar a ver si los síntomas continúan")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_productos_quimicos(decision, juego):
        """Procesa la decisión de productos químicos"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Suspender - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n🛑 Suspiendes el uso de los productos inmediatamente.")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}Acciones:{Colors.ENDC}")
            print("1. Exigir Fichas de Datos de Seguridad")
            print("2. Análisis de composición química")
            print("3. Evaluación de riesgos por exposición")
            print("4. Cambio a productos ecológicos certificados")
            print("5. Proporcionas EPIs adecuados para personal de limpieza")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ Descubres que contenían amoníaco y lejía (mezcla tóxica){Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Has evitado intoxicaciones graves{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +20 Puntuación (actuación correcta y legal){Colors.ENDC}")
            juego.puntuacion += 20
            juego.riesgos_detectados += 3
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 2:
            # Ventilación
            Utilidades.escribir_lento("\n🪟 Abres las ventanas para mejorar la ventilación...")
            time.sleep(0.3)
            Utilidades.escribir_lento("Los síntomas mejoran temporalmente.")
            time.sleep(0.5)
            print(f"\n{Colors.WARNING}⚠️  Pero no has eliminado la causa raíz{Colors.ENDC}")
            print(f"{Colors.WARNING}⚠️  Una empleada desarrolla alergia química{Colors.ENDC}")
            print(f"\n{Colors.WARNING}⚠️  Puntuación +5 (paliativo, no solución){Colors.ENDC}")
            juego.puntuacion += 5
            juego.riesgos_detectados += 1
            
        elif decision == 3:
            # Menos producto
            Utilidades.escribir_lento("\n📉 Pides que usen menos cantidad de producto...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ Los síntomas continúan{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ 2 empleados tienen que ir a urgencias{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -8 (medida insuficiente){Colors.ENDC}")
            juego.puntuacion -= 8
            
        else:
            # Esperar
            Utilidades.escribir_lento("\n⏳ Decides esperar a ver la evolución...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ Una empleada sufre un shock anafiláctico{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Tiene que ser hospitalizada{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Inspección + sanción de 30.000€{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -30 (negligencia grave){Colors.ENDC}")
            juego.puntuacion -= 30
            
        Utilidades.pausa()
    
    @staticmethod
    def escenario_embarazo():
        """Duodécima escena - Trabajadora embarazada"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 11: PROTECCIÓN DE LA MATERNIDAD ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Sara, desarrolladora senior, te comunica que está embarazada de 3 meses.")
        time.sleep(0.3)
        Utilidades.escribir_lento("Su trabajo actual incluye:")
        time.sleep(0.5)
        
        print(f"\n{Colors.WARNING}💻 Jornadas de 9-10 horas diarias{Colors.ENDC}")
        print(f"{Colors.WARNING}🪑 Puesto de trabajo estándar (no adaptado){Colors.ENDC}")
        print(f"{Colors.WARNING}✈️  Viajes frecuentes a clientes (3-4/mes){Colors.ENDC}")
        print(f"{Colors.WARNING}📦 Ocasionalmente mueve equipos pesados (servidores){Colors.ENDC}")
        
        time.sleep(0.5)
        print(f"\n{Colors.OKCYAN}Sara:{Colors.ENDC} '¿Tengo que cambiar algo en mi trabajo? Quiero seguir siendo productiva.'")
        
        print("\n¿Qué plan implementas?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Evaluación riesgos + adaptación completa del puesto")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} Reducir solo los viajes y levantar peso")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} Dejarla decidir qué necesita")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} Nada, el embarazo no es una enfermedad")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_embarazo(decision, juego):
        """Procesa la decisión de embarazo"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Evaluación completa - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n👶 Realizas una evaluación de riesgos específica para embarazo en puesto IT:")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}ADAPTACIONES TÉCNICAS IMPLEMENTADAS:{Colors.ENDC}")
            print("• Silla ergonómica especial para embarazo")
            print("• Monitor a altura y distancia óptima")
            print("• Reposapiés y soporte lumbar ajustable")
            print("• Teclado y ratón ergonómicos")
            print("• Filtro antirreflejos en pantalla")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}ADAPTACIONES ORGANIZATIVAS:{Colors.ENDC}")
            print("• Jornada reducida a 7h con descansos cada hora")
            print("• Eliminación total de viajes")
            print("• Trabajo 100% remoto (evitar desplazamientos)")
            print("• Horario flexible para citas médicas")
            print("• Pausas para caminar y estirar cada 90min")
            print("• Prohibición de levantar peso >3kg (no mover equipos)")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}VIGILANCIA DE LA SALUD:{Colors.ENDC}")
            print("• Revisiones médicas mensuales")
            print("• Línea directa con médico del trabajo")
            print("• Cambio inmediato si aparecen molestias")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ Sara tiene un embarazo saludable{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Mantiene su rol técnico y liderazgo{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ El equipo valora el apoyo mostrado{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Cumplimiento de la Ley 31/1995 Art. 26{Colors.ENDC}")
            print(f"\n{Colors.OKGREEN}✅ +25 Puntuación (protección ejemplar){Colors.ENDC}")
            juego.puntuacion += 25
            juego.riesgos_detectados += 4
            juego.decisiones_correctas += 1
            juego.trabajadores_salvados += 1
            
        elif decision == 2:
            # Solo viajes y peso
            Utilidades.escribir_lento("\n✈️ Eliminas viajes y guardias laborales...")
            time.sleep(0.3)
            Utilidades.escribir_lento("Pero no adaptas el puesto ergonómicamente ni reduces jornada.")
            time.sleep(0.5)
            print(f"\n{Colors.WARNING}⚠️  Sara desarrolla dolor lumbar severo por malas posturas{Colors.ENDC}")
            print(f"{Colors.WARNING}⚠️  Tiene que coger baja médica en el mes 7 del embarazo{Colors.ENDC}")
            print(f"\n{Colors.WARNING}⚠️  Puntuación +8 (medidas insuficientes){Colors.ENDC}")
            juego.puntuacion += 8
            juego.riesgos_detectados += 2
            
        elif decision == 3:
            # Dejarla decidir
            Utilidades.escribir_lento("\n🤷 Le dices que decida ella qué necesita...")
            time.sleep(0.3)
            Utilidades.escribir_lento("Sara, por compromiso, no pide cambios.")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ Problema en el mes 6 de embarazo: amenaza de parto prematuro{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Relacionado con estrés y condiciones laborales{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -15 (incumplimiento legal){Colors.ENDC}")
            juego.puntuacion -= 15
            
        else:
            # Nada
            Utilidades.escribir_lento("\n😐 'El embarazo no es una enfermedad, puede trabajar normal'...")
            time.sleep(0.5)
            print(f"\n{Colors.FAIL}❌ Incumplimiento grave de la ley que regula esta situación (31/1995){Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Sara sufre complicaciones serias{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Demanda judicial + sanción de 50.000€{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Daño reputacional grave{Colors.ENDC}")
            print(f"\n{Colors.FAIL}❌ Puntuación -35 (negligencia gravísima){Colors.ENDC}")
            juego.puntuacion -= 35
            
        Utilidades.pausa()

    @staticmethod
    def escenario_final():
        """Escena final - presentación ante dirección"""
        print(f"{Colors.BOLD}═══ CAPÍTULO 12: REUNIÓN FINAL CON DIRECCIÓN ═══{Colors.ENDC}\n")
        Utilidades.escribir_lento("Han pasado varias semanas desde tu llegada a Chapuzalia M.L.")
        Utilidades.escribir_lento("Has gestionado múltiples situaciones y riesgos en esta empresa IT.")
        time.sleep(0.5)
        Utilidades.escribir_lento("\nEl CTO y el CEO te han convocado a una reunión del comité de dirección")
        Utilidades.escribir_lento("para presentar tu informe completo sobre PRL en entornos tecnológicos.")
        time.sleep(0.5)
        Utilidades.escribir_lento("\nEstán presentes:")
        print(f"• CEO (Chief Executive Officer)")
        print(f"• CTO (Chief Technology Officer)")
        print(f"• CFO (Chief Financial Officer)")
        print(f"• CHRO (Director de RRHH)")
        print(f"• Tech Leads de los equipos de desarrollo")
        print(f"• Representantes sindicales de los trabajadores IT")
        time.sleep(0.5)
        
        print(f"\n{Colors.OKCYAN}CEO:{Colors.ENDC} 'Bueno, cuéntanos.'")
        print(f"{Colors.OKCYAN}CEO:{Colors.ENDC} '¿Qué has encontrado en nuestros equipos? ¿Cuánto nos va a costar esto?'")
        print(f"\n{Colors.OKCYAN}CTO:{Colors.ENDC} 'Sobre todo, ¿va a afectar a la productividad de desarrollo?'")
        
        time.sleep(0.5)
        Utilidades.escribir_lento("\nTienes que presentar tu informe de evaluación de riesgos en equipos IT.")
        
        print("\n¿Cómo enfocas tu presentación?")
        print(f"\n{Colors.OKBLUE}1.{Colors.ENDC} Enfoque TÉCNICO: Datos, legislación, riesgos específicos IT")
        print(f"\n{Colors.OKBLUE}2.{Colors.ENDC} Enfoque ECONÓMICO: ROI, costes de rotación, productividad dev")
        print(f"\n{Colors.OKBLUE}3.{Colors.ENDC} Enfoque HUMANO: Burnout, testimonios, salud mental")
        print(f"\n{Colors.OKBLUE}4.{Colors.ENDC} Enfoque MIXTO: Combinar datos, economía y factor humano")
        
        return Utilidades.obtener_decision(4)
    
    @staticmethod
    def procesar_final(decision, juego):
        """Procesa la decisión final"""
        Utilidades.limpiar_pantalla()
        
        if decision == 1:
            # Técnico
            Utilidades.escribir_lento("\n📊 Presentas un informe técnico exhaustivo:")
            time.sleep(0.3)
            print(f"\n• Incumplimientos del RD 486/1997 (lugares de trabajo)")
            print(f"• Incumplimientos del RD 488/1997 (pantallas de visualización)")
            print(f"• Falta de plan de emergencia")
            print(f"• 47 riesgos ergonómicos documentados")
            time.sleep(0.5)
            print(f"\n{Colors.OKCYAN}CFO:{Colors.ENDC} 'Muy completo, pero... ¿en cristiano?'")
            print(f"{Colors.OKCYAN}CFO:{Colors.ENDC} '¿Qué significa esto para el negocio?'")
            time.sleep(0.3)
            Utilidades.escribir_lento("\nTu informe es técnicamente correcto pero no conecta con dirección.")
            print(f"\n{Colors.WARNING}⚠️  Puntuación +5 (correcto pero poco efectivo){Colors.ENDC}")
            juego.puntuacion += 5
            
        elif decision == 2:
            # Económico - BUENO
            Utilidades.escribir_lento("\n💰 Presentas el caso de negocio:")
            time.sleep(0.3)
            print(f"\n📉 Situación actual:")
            print(f"• Absentismo por bajas: 15% (la media del sectores del: 8%)")
            print(f"• Coste anual en bajas: 65.000€")
            print(f"• Riesgo de sanciones: hasta 819.780€ (infracciones muy graves)")
            time.sleep(0.5)
            print(f"\n📈 Propuesta de inversión:")
            print(f"• Inversión: 35.000€ (equipamiento + formación)")
            print(f"• ROI esperado: 18 meses")
            print(f"• Ahorro anual: 45.000€ + reducción del 40% en absentismo")
            time.sleep(0.5)
            print(f"\n{Colors.OKCYAN}CFO:{Colors.ENDC} '¡Ahora sí! Esto tiene sentido.'")
            print(f"\n{Colors.OKGREEN}✅ +15 Puntuación (argumentación económica sólida){Colors.ENDC}")
            juego.puntuacion += 15
            juego.decisiones_correctas += 1
            
        elif decision == 3:
            # Humano
            Utilidades.escribir_lento("\n❤️ Compartes testimonios y situaciones personales:")
            time.sleep(0.3)
            print(f"\n'Miguel tiene 28 años y ya sufre dolores crónicos de cuello.'")
            print(f"'Laura, embarazada, podría haber tenido un accidente grave.'")
            print(f"'El equipo está estresado, quemado, y siente que no se les cuida.'")
            time.sleep(0.5)
            print(f"\n{Colors.OKCYAN}RRHH:{Colors.ENDC} 'Es verdad. Hemos tenido quejas...'")
            print(f"\n{Colors.OKCYAN}CEO:{Colors.ENDC} 'Entiendo, pero necesito números. ¿Qué inversión necesitas?'")
            time.sleep(0.3)
            Utilidades.escribir_lento("\nHas conectado emocionalmente pero falta concreción.")
            print(f"\n{Colors.WARNING}⚠️  Puntuación +5 (emotivo pero incompleto){Colors.ENDC}")
            juego.puntuacion += 5
            
        else:
            # Mixto - MEJOR OPCIÓN
            Utilidades.escribir_lento("\n🎯 Presentas un caso completo e integrado:")
            time.sleep(0.3)
            print(f"\n{Colors.BOLD}1. LA REALIDAD HUMANA:{Colors.ENDC}")
            print(f"'El 60% del equipo reporta molestias por el mal estado del equipamiento y las instalaciones.'")
            print(f"'Miguel, nuestro desarrollador senior, sufre dolores crónicos a los 28 años.'")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}2. EL MARCO LEGAL:{Colors.ENDC}")
            print(f"'Incumplimos el RD 486/1997 y RD 488/1997.'")
            print(f"'Las sanciones pueden llegar a 819.780€ por infracciones muy graves.'")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}3. EL IMPACTO EN EL NEGOCIO:{Colors.ENDC}")
            print(f"'Absentismo actual: 15% vs 8% del sector = 65.000€/año en pérdidas'")
            print(f"'Inversión propuesta: 35.000€'")
            print(f"'ROI: 18 meses | Ahorro: 45.000€/año'")
            time.sleep(0.5)
            print(f"\n{Colors.BOLD}4. PLAN DE ACCIÓN:{Colors.ENDC}")
            print(f"'Fase 1 (inmediata): Emergencias y riesgos graves - 5.000€'")
            print(f"'Fase 2 (3 meses): Ergonomía - 25.000€'")
            print(f"'Fase 3 (6 meses): Formación y cultura - 5.000€'")
            time.sleep(1)
            print(f"\n{Colors.OKCYAN}CEO:{Colors.ENDC} 'Impresionante. Aprobado.'")
            print(f"{Colors.OKCYAN}CFO:{Colors.ENDC} 'El análisis económico es sólido.'")
            print(f"{Colors.OKCYAN}RRHH:{Colors.ENDC} 'El equipo va a agradecer esto enormemente.'")
            time.sleep(0.5)
            print(f"\n{Colors.OKGREEN}✅ +25 Puntuación (presentación EXCELENTE){Colors.ENDC}")
            print(f"{Colors.OKGREEN}🏆 Has conseguido presupuesto completo aprobado{Colors.ENDC}")
            juego.puntuacion += 25
            juego.decisiones_correctas += 1
        
        Utilidades.pausa()