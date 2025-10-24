#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de utilidades del juego
Contiene funciones auxiliares y de interfaz
"""

import os
import time
import sys


class Colors:
    """Colores para la terminal"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Utilidades:
    """Clase con utilidades generales del juego"""
    
    @staticmethod
    def limpiar_pantalla():
        """Limpia la pantalla de la terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    @staticmethod
    def escribir_lento(texto, velocidad=0.03):
        """Escribe texto con efecto de máquina de escribir"""
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(velocidad)
        print()
    
    @staticmethod
    def pausa():
        """Pausa para que el usuario continúe"""
        input(f"\n{Colors.OKBLUE}[Pulsa INTRO para continuar]{Colors.ENDC}")
    
    @staticmethod
    def mostrar_titulo():
        """Muestra el título del juego"""
        Utilidades.limpiar_pantalla()
        titulo = f"""
{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                  🛡️  CHAPUZALIAPRL   🛡️                        ║
║                                                              ║
║          Prevención de Riesgos Laborales en TI               ║
║              Basado en la Ley 31/1995 (España)               ║
║                     🛠️  Versión 1.0                           ║
╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}
        """
        print(titulo)
    
    @staticmethod
    def mostrar_estadisticas(nombre_jugador, puntuacion, riesgos_detectados, 
                            decisiones_correctas, trabajadores_salvados):
        """Muestra las estadísticas del jugador"""
        print(f"\n{Colors.OKCYAN}═══ ESTADÍSTICAS ═══{Colors.ENDC}")
        print(f"👤 Inspector: {nombre_jugador}")
        print(f"⭐ Puntuación: {puntuacion}/100")
        print(f"🔍 Riesgos detectados: {riesgos_detectados}")
        print(f"✅ Decisiones correctas: {decisiones_correctas}")
        print(f"�️  Situaciones críticas resueltas: {trabajadores_salvados}/12")
        print(f"{Colors.OKCYAN}{'═' * 25}{Colors.ENDC}\n")
    
    @staticmethod
    def obtener_decision(num_opciones):
        """Obtiene y valida la decisión del jugador"""
        while True:
            try:
                decision = input(f"\n{Colors.BOLD}Tu decisión (1-{num_opciones}): {Colors.ENDC}").strip()
                decision = int(decision)
                if 1 <= decision <= num_opciones:
                    return decision
                else:
                    print(f"{Colors.FAIL}Por favor, elige un número entre 1 y {num_opciones}{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}Por favor, introduce un número válido{Colors.ENDC}")
