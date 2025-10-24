#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de gestión de puntuaciones
Guarda y carga el historial de partidas en formato JSON
"""

import json
import os
from datetime import datetime
from utilidades import Colors


class GestorPuntuaciones:
    """Clase para gestionar el guardado y carga de puntuaciones"""
    
    ARCHIVO_PUNTUACIONES = "puntuaciones.json"
    
    @staticmethod
    def cargar_puntuaciones():
        """Carga las puntuaciones desde el archivo JSON"""
        if not os.path.exists(GestorPuntuaciones.ARCHIVO_PUNTUACIONES):
            return []
        
        try:
            with open(GestorPuntuaciones.ARCHIVO_PUNTUACIONES, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    
    @staticmethod
    def guardar_puntuacion(nombre, puntuacion, riesgos_detectados, decisiones_correctas, 
                          trabajadores_salvados, capitulos_completados, partida_completa=True):
        """
        Guarda una nueva puntuación en el archivo JSON
        
        Args:
            nombre (str): Nombre del jugador
            puntuacion (int): Puntuación obtenida
            riesgos_detectados (int): Número de riesgos detectados
            decisiones_correctas (int): Número de decisiones correctas
            trabajadores_salvados (int): Número de trabajadores protegidos
            capitulos_completados (int): Número de capítulos completados
            partida_completa (bool): Si terminó la partida o la interrumpió
        """
        # Cargar puntuaciones existentes
        puntuaciones = GestorPuntuaciones.cargar_puntuaciones()
        
        # Determinar valoración
        if puntuacion >= 80:
            valoracion = "EXCELENTE"
        elif puntuacion >= 50:
            valoracion = "ACEPTABLE"
        else:
            valoracion = "MEJORABLE"
        
        # Crear nueva entrada
        nueva_puntuacion = {
            "nombre": nombre,
            "puntuacion": puntuacion,
            "valoracion": valoracion,
            "riesgos_detectados": riesgos_detectados,
            "decisiones_correctas": decisiones_correctas,
            "trabajadores_salvados": trabajadores_salvados,
            "capitulos_completados": capitulos_completados,
            "partida_completa": partida_completa,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Añadir nueva puntuación
        puntuaciones.append(nueva_puntuacion)
        
        # Guardar en archivo
        try:
            with open(GestorPuntuaciones.ARCHIVO_PUNTUACIONES, 'w', encoding='utf-8') as f:
                json.dump(puntuaciones, f, ensure_ascii=False, indent=2)
            return True
        except IOError as e:
            print(f"{Colors.FAIL}Error al guardar puntuación: {e}{Colors.ENDC}")
            return False
    
    @staticmethod
    def obtener_mejores_puntuaciones(limite=10):
        """Obtiene las mejores puntuaciones ordenadas de mayor a menor"""
        puntuaciones = GestorPuntuaciones.cargar_puntuaciones()
        
        # Filtrar solo partidas completas para el ranking
        puntuaciones_completas = [p for p in puntuaciones if p.get('partida_completa', True)]
        
        # Ordenar por puntuación descendente
        puntuaciones_ordenadas = sorted(puntuaciones_completas, 
                                       key=lambda x: x['puntuacion'], 
                                       reverse=True)
        
        return puntuaciones_ordenadas[:limite]
    
    @staticmethod
    def obtener_estadisticas_globales():
        """Obtiene estadísticas globales de todas las partidas"""
        puntuaciones = GestorPuntuaciones.cargar_puntuaciones()
        
        if not puntuaciones:
            return None
        
        total_partidas = len(puntuaciones)
        partidas_completas = len([p for p in puntuaciones if p.get('partida_completa', True)])
        
        # Solo considerar partidas completas para estadísticas
        puntuaciones_completas = [p for p in puntuaciones if p.get('partida_completa', True)]
        
        if not puntuaciones_completas:
            return None
        
        puntuaciones_valores = [p['puntuacion'] for p in puntuaciones_completas]
        
        estadisticas = {
            'total_partidas': total_partidas,
            'partidas_completas': partidas_completas,
            'partidas_interrumpidas': total_partidas - partidas_completas,
            'puntuacion_maxima': max(puntuaciones_valores),
            'puntuacion_minima': min(puntuaciones_valores),
            'puntuacion_media': sum(puntuaciones_valores) / len(puntuaciones_valores),
            'excelentes': len([p for p in puntuaciones_completas if p['puntuacion'] >= 80]),
            'aceptables': len([p for p in puntuaciones_completas if 50 <= p['puntuacion'] < 80]),
            'mejorables': len([p for p in puntuaciones_completas if p['puntuacion'] < 50])
        }
        
        return estadisticas
    
    @staticmethod
    def mostrar_ranking():
        """Muestra el ranking de mejores puntuaciones"""
        mejores = GestorPuntuaciones.obtener_mejores_puntuaciones(10)
        
        if not mejores:
            print(f"\n{Colors.WARNING}Todavía no hay puntuaciones guardadas.{Colors.ENDC}\n")
            return
        
        print(f"\n{Colors.HEADER}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗{Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}║              🏆 RANKING DE MEJORES INSPECTORES 🏆             ║{Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}╚═══════════════════════════════════════════════════════════════╝{Colors.ENDC}\n")
        
        for i, partida in enumerate(mejores, 1):
            # Medalla según posición
            if i == 1:
                medalla = "🥇"
                color = Colors.OKGREEN
            elif i == 2:
                medalla = "🥈"
                color = Colors.OKCYAN
            elif i == 3:
                medalla = "🥉"
                color = Colors.OKBLUE
            else:
                medalla = f"{i}."
                color = Colors.ENDC
            
            # Color según valoración
            if partida['valoracion'] == "EXCELENTE":
                color_val = Colors.OKGREEN
            elif partida['valoracion'] == "ACEPTABLE":
                color_val = Colors.OKBLUE
            else:
                color_val = Colors.WARNING
            
            print(f"{color}{medalla:4} {partida['nombre']:20} {Colors.BOLD}{partida['puntuacion']:3}/100{Colors.ENDC} "
                  f"{color_val}[{partida['valoracion']}]{Colors.ENDC} "
                  f"- {partida['fecha']}")
        
        print()
    
    @staticmethod
    def mostrar_estadisticas():
        """Muestra estadísticas globales del juego"""
        stats = GestorPuntuaciones.obtener_estadisticas_globales()
        
        if not stats:
            print(f"\n{Colors.WARNING}No hay suficientes datos para mostrar estadísticas.{Colors.ENDC}\n")
            return
        
        print(f"\n{Colors.OKCYAN}{Colors.BOLD}═══ ESTADÍSTICAS GLOBALES ═══{Colors.ENDC}\n")
        print(f"📊 Total de partidas: {stats['total_partidas']}")
        print(f"✅ Partidas completas: {stats['partidas_completas']}")
        print(f"⏸️  Partidas interrumpidas: {stats['partidas_interrumpidas']}")
        print(f"\n{Colors.BOLD}Puntuaciones:{Colors.ENDC}")
        print(f"   🔝 Máxima: {stats['puntuacion_maxima']}/100")
        print(f"   📉 Mínima: {stats['puntuacion_minima']}/100")
        print(f"   📊 Media: {stats['puntuacion_media']:.1f}/100")
        print(f"\n{Colors.BOLD}Valoraciones:{Colors.ENDC}")
        print(f"   {Colors.OKGREEN}🏆 Excelentes: {stats['excelentes']}{Colors.ENDC}")
        print(f"   {Colors.OKBLUE}✅ Aceptables: {stats['aceptables']}{Colors.ENDC}")
        print(f"   {Colors.WARNING}⚠️  Mejorables: {stats['mejorables']}{Colors.ENDC}")
        print()
