#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de finalización del juego
Gestiona el final del juego y los resultados
"""

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


class FinalJuego:
    """Clase para gestionar el final del juego"""
    
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
    def obtener_valoracion(puntuacion):
        """Determina la valoración según la puntuación"""
        if puntuacion >= 80:
            return {
                'nivel': 'EXCELENTE',
                'color': Colors.OKGREEN,
                'titulo': '🏆 ¡EXCELENTE TRABAJO',
                'logros': [
                    'Inspector Elite de Seguridad IT',
                    'Campeón de la Ergonomía',
                    'Héroe de la Prevención'
                ],
                'desenlace': """Gracias a tu trabajo profesional, Chapuzalia M.L. se convierte
en una empresa referente en prevención de riesgos laborales.

El absentismo se reduce un 60% en 6 meses.
Los trabajadores te consideran parte esencial del equipo.
Recibes una oferta para dirigir el departamento de PRL.""",
                'mensaje': '¡La seguridad laboral no es un gasto, es una inversión!'
            }
        elif puntuacion >= 50:
            return {
                'nivel': 'ACEPTABLE',
                'color': Colors.OKBLUE,
                'titulo': '✅ TRABAJO ACEPTABLE',
                'logros': [
                    'Algunos aciertos importantes',
                    'Algunas decisiones cuestionables',
                    'Margen de mejora significativo'
                ],
                'desenlace': """Chapuzalia M.L. mejora sus condiciones de seguridad gradualmente.
Los trabajadores aprecian tus esfuerzos pero esperaban más.
Continúas en el puesto con oportunidad de mejorar. Ahora además de realizar tu trabajo, tendrás que llevar cafés a dirección.""",
                'mensaje': 'La prevención es un proceso de mejora continua.'
            }
        else:
            return {
                'nivel': 'MEJORABLE',
                'color': Colors.WARNING,
                'titulo': '⚠️  TRABAJO MEJORABLE',
                'logros': [
                    'Decisiones arriesgadas o negligentes',
                    'Falta de criterio profesional',
                    'Prioridades mal establecidas'
                ],
                'desenlace': """Chapuzalia M.L. tiene que contratar un consultor externo
para corregir los problemas que no resolviste adecuadamente.

Tu reputación profesional se ve afectada.
Necesitas formación adicional en PRL.""",
                'mensaje': 'Tienes que volver a la escuela. La prevención no es algo que se pueda improvisar.'
            }
    
    @staticmethod
    def mostrar_mensaje_final(nombre_jugador, valoracion):
        """Muestra el mensaje final según la valoración"""
        color = valoracion['color']
        
        mensaje = f"""
{color}{valoracion['titulo']}, {nombre_jugador.upper()}! 🏆{Colors.ENDC}

Has demostrado ser un/a Técnico de PRL {'excepcional' if valoracion['nivel'] == 'EXCELENTE' else 'con capacidad de mejora'}.

{'✨ LOGROS DESBLOQUEADOS:' if valoracion['nivel'] == 'EXCELENTE' else '📊 EVALUACIÓN:' if valoracion['nivel'] == 'ACEPTABLE' else '❌ PROBLEMAS DETECTADOS:'}
"""
        for logro in valoracion['logros']:
            mensaje += f"• {logro}\n"
        
        mensaje += f"""
📜 DESENLACE:
{valoracion['desenlace']}

{color}{valoracion['mensaje']}{Colors.ENDC}
        """
        
        return mensaje
    
    @staticmethod
    def mostrar_resumen_decisiones(historial_decisiones):
        """Muestra el resumen de las decisiones tomadas"""
        escenarios = {
            "llegada": "Capítulo 1 - Primer día (Cables en el pasillo)",
            "puesto_trabajo": "Capítulo 2 - Evaluación ergonómica",
            "emergencia": "Capítulo 3 - Incendio en sala de servidores",
            "climatizacion": "Capítulo 4 - Temperatura extrema",
            "acoso": "Capítulo 5 - Riesgos psicosociales (Acoso)",
            "pantallas": "Capítulo 6 - Salud visual",
            "covid": "Capítulo 7 - Riesgo biológico (COVID)",
            "estres": "Capítulo 8 - Burnout",
            "teletrabajo": "Capítulo 9 - Teletrabajo",
            "productos_quimicos": "Capítulo 10 - Riesgo químico",
            "embarazo": "Capítulo 11 - Protección de la maternidad",
            "final": "Capítulo 12 - Presentación a dirección"
        }
        
        print(f"\n{Colors.OKCYAN}═══ RESUMEN DE TUS DECISIONES ═══{Colors.ENDC}\n")
        for escena, decision in historial_decisiones:
            nombre_escena = escenarios.get(escena, escena)
            print(f"• {nombre_escena}: Opción {decision}")
    
    @staticmethod
    def mostrar_estadisticas_finales(puntuacion, riesgos_detectados, 
                                     decisiones_correctas, trabajadores_salvados, nivel):
        """Muestra las estadísticas finales"""
        print(f"\n{Colors.HEADER}═══ ESTADÍSTICAS FINALES ═══{Colors.ENDC}")
        print(f"\n⭐ Puntuación final: {puntuacion}/100")
        print(f"🔍 Riesgos detectados: {riesgos_detectados}")
        print(f"✅ Decisiones correctas: {decisiones_correctas}")
        print(f"�️  Situaciones críticas resueltas: {trabajadores_salvados}/12")
        print(f"🏆 Valoración: {nivel}")
    
    @staticmethod
    def mostrar_consejos():
        """Muestra consejos finales sobre PRL"""
        print(f"\n{Colors.OKGREEN}═══ RECUERDA ═══{Colors.ENDC}\n")
        print("📚 La Ley 31/1995 de PRL es tu mejor aliada")
        print("🎯 La prevención debe ser proactiva, no reactiva")
        print("💡 Los riesgos ergonómicos son invisibles pero muy dañinos")
        print("🚨 En emergencias: calma, protocolo, y seguridad primero")
        print("💰 La prevención bien hecha es rentable para la empresa")
        print("❤️  La salud de los trabajadores es lo primero\n")
    
    @staticmethod
    def mostrar_pantalla_final(nombre_jugador, puntuacion, riesgos_detectados,
                               decisiones_correctas, trabajadores_salvados,
                               historial_decisiones):
        """Muestra la pantalla final completa del juego"""
        print(f"{Colors.HEADER}{Colors.BOLD}")
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║                                                               ║")
        print("║                    🏁 FINAL DEL JUEGO 🏁                      ║")
        print("║                                                               ║")
        print("╚═══════════════════════════════════════════════════════════════╝")
        print(f"{Colors.ENDC}\n")
        
        # Mostrar estadísticas
        FinalJuego.mostrar_estadisticas(nombre_jugador, puntuacion, 
                                        riesgos_detectados, decisiones_correctas, 
                                        trabajadores_salvados)
        
        # Obtener valoración
        valoracion = FinalJuego.obtener_valoracion(puntuacion)
        
        # Mostrar mensaje final
        print(FinalJuego.mostrar_mensaje_final(nombre_jugador, valoracion))
        
        # Resumen de decisiones
        FinalJuego.mostrar_resumen_decisiones(historial_decisiones)
        
        # Estadísticas finales
        FinalJuego.mostrar_estadisticas_finales(puntuacion, riesgos_detectados,
                                                decisiones_correctas, trabajadores_salvados,
                                                valoracion['nivel'])
        
        # Consejos finales
        FinalJuego.mostrar_consejos()
        
        print(f"{Colors.BOLD}¡Gracias por jugar a ChapuzaliaPRL!{Colors.ENDC}\n")
