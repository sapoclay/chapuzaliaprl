#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHAPUZALIAPRL
Aventura de texto sobre Prevención de Riesgos Laborales en entornos informáticos  
Ley 31/1995 de PRL de España
"""

import time
from utilidades import Colors, Utilidades
from escenarios import Escenarios
from final import FinalJuego
from puntuaciones import GestorPuntuaciones


class JuegoPRL:
    def __init__(self):
        self.puntuacion = 0
        self.riesgos_detectados = 0
        self.decisiones_correctas = 0
        self.trabajadores_salvados = 0
        self.nombre_jugador = ""
        self.historial_decisiones = []
    
    def introduccion(self):
        """Introducción al juego"""
        Utilidades.mostrar_titulo()
        print(f"{Colors.OKGREEN}¡Bienvenido/a al mundo del PRL (Para, Reza y Llora)!{Colors.ENDC}\n")
        self.nombre_jugador = input("Por favor, introduce tu nombre: ").strip()
        
        if not self.nombre_jugador:
            self.nombre_jugador = "Inspector Anónimo"
        
        Utilidades.limpiar_pantalla()
        Utilidades.mostrar_titulo()
        
        Utilidades.escribir_lento(f"\nBienvenido/a, {self.nombre_jugador}.")
        time.sleep(0.5)
        Utilidades.escribir_lento("\nHas sido contratado/a como Técnico de Prevención de Riesgos Laborales")
        Utilidades.escribir_lento("en Chapuzalia M.L., una empresa de desarrollo software con 50 empleados.")
        time.sleep(0.5)
        Utilidades.escribir_lento("\nTu misión: Inspeccionar las instalaciones, identificar riesgos")
        Utilidades.escribir_lento("y tomar decisiones que garanticen la seguridad de los trabajadores y hacer así que no acabes en la calle.")
        time.sleep(0.5)
        Utilidades.escribir_lento(f"\n{Colors.WARNING}⚠️  Cada decisión importa. La salud de tus compañeros y tu sueldo dependen de tus decisiones.{Colors.ENDC}")
        
        Utilidades.pausa()
    
    def _guardar_partida(self, partida_completa=True):
        """Guarda la partida en el archivo de puntuaciones"""
        if not self.nombre_jugador:
            return
        
        exito = GestorPuntuaciones.guardar_puntuacion(
            nombre=self.nombre_jugador,
            puntuacion=self.puntuacion,
            riesgos_detectados=self.riesgos_detectados,
            decisiones_correctas=self.decisiones_correctas,
            trabajadores_salvados=self.trabajadores_salvados,
            capitulos_completados=len(self.historial_decisiones),
            partida_completa=partida_completa
        )
        
        if exito and partida_completa:
            print(f"{Colors.OKGREEN}✅ Puntuación guardada correctamente!!{Colors.ENDC}\n")
    
    def final_juego(self):
        """Pantalla final con resultados"""
        Utilidades.limpiar_pantalla()
        
        FinalJuego.mostrar_pantalla_final(
            self.nombre_jugador,
            self.puntuacion,
            self.riesgos_detectados,
            self.decisiones_correctas,
            self.trabajadores_salvados,
            self.historial_decisiones
        )
        
        # Guardar puntuación
        self._guardar_partida(partida_completa=True)
    
    def jugar(self):
        """Función principal del juego"""
        try:
            self.introduccion()
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion, 
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision1 = Escenarios.escenario_llegada()
            self.historial_decisiones.append(("llegada", decision1))
            Escenarios.procesar_llegada(decision1, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision2 = Escenarios.escenario_puesto_trabajo()
            self.historial_decisiones.append(("puesto_trabajo", decision2))
            Escenarios.procesar_puesto_trabajo(decision2, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision3 = Escenarios.escenario_emergencia()
            self.historial_decisiones.append(("emergencia", decision3))
            Escenarios.procesar_emergencia(decision3, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision4 = Escenarios.escenario_climatizacion()
            self.historial_decisiones.append(("climatizacion", decision4))
            Escenarios.procesar_climatizacion(decision4, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision5 = Escenarios.escenario_acoso()
            self.historial_decisiones.append(("acoso", decision5))
            Escenarios.procesar_acoso(decision5, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision6 = Escenarios.escenario_pantallas()
            self.historial_decisiones.append(("pantallas", decision6))
            Escenarios.procesar_pantallas(decision6, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision7 = Escenarios.escenario_covid()
            self.historial_decisiones.append(("covid", decision7))
            Escenarios.procesar_covid(decision7, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision8 = Escenarios.escenario_estres()
            self.historial_decisiones.append(("estres", decision8))
            Escenarios.procesar_estres(decision8, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision9 = Escenarios.escenario_teletrabajo()
            self.historial_decisiones.append(("teletrabajo", decision9))
            Escenarios.procesar_teletrabajo(decision9, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision10 = Escenarios.escenario_productos_quimicos()
            self.historial_decisiones.append(("productos_quimicos", decision10))
            Escenarios.procesar_productos_quimicos(decision10, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision11 = Escenarios.escenario_embarazo()
            self.historial_decisiones.append(("embarazo", decision11))
            Escenarios.procesar_embarazo(decision11, self)
            
            Utilidades.limpiar_pantalla()
            Utilidades.mostrar_estadisticas(self.nombre_jugador, self.puntuacion,
                                           self.riesgos_detectados, self.decisiones_correctas,
                                           self.trabajadores_salvados)
            decision12 = Escenarios.escenario_final()
            self.historial_decisiones.append(("final", decision12))
            Escenarios.procesar_final(decision12, self)
            
            self.final_juego()
            
        except KeyboardInterrupt:
            # Mostrar estadísticas al interrumpir
            print(f"\n\n{Colors.WARNING}⚠️  Juego interrumpido por el usuario.{Colors.ENDC}\n")
            
            if self.nombre_jugador:
                print(f"{Colors.BOLD}Estadísticas al momento de la interrupción:{Colors.ENDC}\n")
                print(f"👤 Nombre del inspector: {self.nombre_jugador}")
                print(f"⭐ Puntuación: {self.puntuacion}/100")
                print(f"🔍 Riesgos detectados: {self.riesgos_detectados}")
                print(f"✅ Decisiones correctas: {self.decisiones_correctas}")
                print(f"�️  Situaciones críticas resueltas: {self.trabajadores_salvados}/12")
                print(f"📊 Capítulos completados: {len(self.historial_decisiones)}/12\n")
                
                # Guardar partida interrumpida
                self._guardar_partida(partida_completa=False)
                print(f"{Colors.OKCYAN}💾 Partida guardada en el historial{Colors.ENDC}\n")
            else:
                print("No llegaste a comenzar la partida.\n")
                
        except Exception as e:
            print(f"\n{Colors.FAIL}❌ Error inesperado: {e}{Colors.ENDC}\n")


def mostrar_creditos():
    """Muestra los créditos del juego con efecto de máquina de escribir"""
    print("\n")
    
    # Arte ASCII grande para "CRÉDITOS"
    creditos_ascii = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║    ██████╗██████╗ ███████╗██████╗ ██╗████████╗ ██████╗ ███████╗
║   ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔═══██╗██╔════╝
║   ██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ██║   ██║███████╗
║   ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ██║   ██║╚════██║
║   ╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ╚██████╔╝███████║
║    ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚══════╝
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
    
    # Mostrar el título con efecto de escritura
    for linea in creditos_ascii.split('\n'):
        print(f"{Colors.HEADER}{Colors.BOLD}{linea}{Colors.ENDC}")
        time.sleep(0.1)
    
    print("\n")
    time.sleep(0.3)
    
    # Información de créditos con efecto de máquina de escribir
    Utilidades.escribir_lento(f"{Colors.OKGREEN}{Colors.BOLD}Chapuzeando EntreunosYCeros{Colors.ENDC}")
    print("\n")
    time.sleep(0.3)
    Utilidades.escribir_lento(f"{Colors.OKCYAN}🔗 https://github.com/sapoclay/chapuzaliaprl{Colors.ENDC}")
    print("\n\n")
    time.sleep(0.3)
    Utilidades.escribir_lento(f"{Colors.WARNING}Proyecto para educar a los lobos. Basado en ParaRezaYLlora (PRL) ... o como le llaman algunos ... Prevención de Riesgos Laborales{Colors.ENDC}")
    print()
    time.sleep(0.2)
    Utilidades.escribir_lento(f"{Colors.WARNING}en entornos de tecnología y desarrollo software.{Colors.ENDC}")
    print("\n\n")
    time.sleep(0.3)
    Utilidades.escribir_lento(f"{Colors.OKBLUE}Basado en lo poco que conozco la Ley 31/1995 de PRL de España{Colors.ENDC}")
    Utilidades.escribir_lento(f"{Colors.OKBLUE}... Cuando salga la película, lo haré más curioso.{Colors.ENDC}")
    print("\n\n")
    time.sleep(0.5)
    print(f"{Colors.BOLD}¡Gracias por jugar!{Colors.ENDC}\n")


def main():
    """Función principal"""
    while True:
        Utilidades.limpiar_pantalla()
        Utilidades.mostrar_titulo()
        
        print(f"{Colors.BOLD}MENÚ PRINCIPAL{Colors.ENDC}\n")
        print(f"{Colors.OKBLUE}1.{Colors.ENDC} 🎮 Jugar nueva partida")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} 🏆 Ver ranking de puntuaciones")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} 📊 Ver estadísticas globales")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} 🎬 Ver créditos")
        print(f"{Colors.OKBLUE}5.{Colors.ENDC} Salir")
        
        try:
            opcion = Utilidades.obtener_decision(5)
            
            if opcion == 1:
                # Jugar
                juego = JuegoPRL()
                juego.jugar()
                input(f"\n{Colors.OKBLUE}Presiona INTRO para volver al menú...{Colors.ENDC}")
                
            elif opcion == 2:
                # Ver ranking
                Utilidades.limpiar_pantalla()
                GestorPuntuaciones.mostrar_ranking()
                input(f"{Colors.OKBLUE}Presiona INTRO para volver al menú...{Colors.ENDC}")
                
            elif opcion == 3:
                # Ver estadísticas
                Utilidades.limpiar_pantalla()
                GestorPuntuaciones.mostrar_estadisticas()
                input(f"{Colors.OKBLUE}Presiona INTRO para volver al menú...{Colors.ENDC}")
                
            elif opcion == 4:
                # Ver créditos
                Utilidades.limpiar_pantalla()
                mostrar_creditos()
                input(f"{Colors.OKBLUE}Presiona INTRO para volver al menú...{Colors.ENDC}")
                
            elif opcion == 5:
                # Salir
                print(f"\n{Colors.OKGREEN}¡Gracias por jugar! Hasta pronto, y vuelve con dinero!!.{Colors.ENDC}\n")
                break
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.OKGREEN}¡Hasta más ver!{Colors.ENDC}\n")
            break


if __name__ == "__main__":
    main()
