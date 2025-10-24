# 🛡️ ChapuzaliaPRL

Este es un pequeño juego para la terminal educativo. Se trata de una aventura de texto sobre llamada Chapuzalia -PRL en entornos informáticos.

## 📋 Descripción

Aventura interactiva basada en la **Ley 31/1995 de PRL de España** donde eres un Técnico de Prevención de Riesgos Laborales en una empresa de desarrollo de software. Tus decisiones afectarán la seguridad de 50 trabajadores.

## 🎯 Características

- ✅ **12 Capítulos interactivos** con múltiples decisiones
- 🎮 **Sistema de puntuación** (puntos positivos y negativos)
- 📊 **Estadísticas en tiempo real** (riesgos detectados, situaciones críticas resueltas)
- 🏆 **Múltiples finales** según tu desempeño
- 📚 **Basado en normativa real** española de PRL
- 🎨 **Interfaz colorida** en terminal
- 💾 **Guardado automático** de puntuaciones en JSON
- 🏅 **Ranking de mejores inspectores**
- 📈 **Estadísticas globales** de todas las partidas
- 📜 **Créditos con arte ASCII**

## 🗂️ Estructura Modular

El proyecto está organizado en módulos por funcionalidad:

```
JUEGOPRL/
│
├── main.py           # Punto de entrada y lógica principal del juego
├── utilidades.py     # Funciones auxiliares y de interfaz
├── escenarios.py     # Todos los capítulos y escenarios del juego
├── final.py          # Gestión del final y resultados
├── puntuaciones.py   # Sistema de guardado y ranking de puntuaciones
├── puntuaciones.json # Archivo JSON con historial (generado automáticamente)
└── README.md         # Este archivo
```

### 📄 Módulos

#### `main.py`
- Clase principal `JuegoPRL`
- Control del flujo del juego
- Gestión de estadísticas del jugador

#### `utilidades.py`
- Clase `Colors`: Definición de colores para terminal
- Clase `Utilidades`: Funciones helper
  - `limpiar_pantalla()`: Limpia la terminal
  - `escribir_lento()`: Efecto de máquina de escribir
  - `pausa()`: Espera input del usuario
  - `mostrar_titulo()`: Muestra el título del juego
  - `mostrar_estadisticas()`: Muestra stats del jugador
  - `obtener_decision()`: Valida las decisiones del usuario

#### `escenarios.py`
- Clase `Escenarios`: Contiene todos los capítulos
  - **Capítulo 1**: Primer día (riesgos en instalaciones)
  - **Capítulo 2**: Evaluación ergonómica
  - **Capítulo 3**: Emergencia (incendio)
  - **Capítulo 4**: Temperatura extrema (climatización)
  - **Capítulo 5**: Riesgos psicosociales (acoso laboral)
  - **Capítulo 6**: Salud visual (pantallas PVD)
  - **Capítulo 7**: Riesgo biológico (COVID-19)
  - **Capítulo 8**: Burnout y estrés laboral
  - **Capítulo 9**: Riesgos del teletrabajo
  - **Capítulo 10**: Riesgo químico (productos de limpieza)
  - **Capítulo 11**: Protección de la maternidad
  - **Capítulo 12**: Presentación final a dirección
- Métodos `procesar_*()` para cada escenario

#### `final.py`
- Clase `FinalJuego`: Gestión del final del juego
  - Cálculo de valoración final
  - Generación de mensajes personalizados
  - Resumen de decisiones
  - Estadísticas finales
  - Consejos de PRL

#### `puntuaciones.py`
- Clase `GestorPuntuaciones`: Sistema de puntuaciones
  - `guardar_puntuacion()`: Guarda partida en JSON
  - `cargar_puntuaciones()`: Lee el historial
  - `obtener_mejores_puntuaciones()`: Top 10 ranking
  - `obtener_estadisticas_globales()`: Stats generales
  - `mostrar_ranking()`: Visualiza el ranking
  - `mostrar_estadisticas()`: Muestra estadísticas

#### `puntuaciones.json`
Archivo JSON generado automáticamente con el historial:
```json
[
  {
    "nombre": "Inspector Pro",
    "puntuacion": 200,
    "valoracion": "EXCELENTE",
    "riesgos_detectados": 45,
    "decisiones_correctas": 10,
    "trabajadores_salvados": 12,
    "capitulos_completados": 12,
    "partida_completa": true,
    "fecha": "2025-10-24 20:45:30"
  }
]
```

## 🚀 Cómo Jugar

```bash
python3 main.py
```

### Menú Principal

Al iniciar el juego verás:

```
MENÚ PRINCIPAL

1. 🎮 Jugar nueva partida
2. 🏆 Ver ranking de puntuaciones
3. 📊 Ver estadísticas globales
4. Ver créditos
5. Salir
```

### Opciones

1. **Jugar nueva partida**: Inicia una nueva aventura de 12 capítulos
2. **Ver ranking**: Muestra el top 10 de mejores inspectores
3. **Ver estadísticas**: Muestra datos globales de todas las partidas
4. **Ver créditos**: Información del proyecto y desarrolladores
5. **Salir**: Cierra el juego

## 🎮 Mecánicas del Juego

### Sistema de Puntuación
- Empiezas con **0 puntos**
- Las buenas decisiones **suman** puntos
- Las malas decisiones **restan** puntos
- Puntuación final puede ser positiva o negativa
- Los riesgos detectados y situaciones críticas resueltas se contabilizan
- Máximo de **12 situaciones críticas** (una por capítulo)

### Valoraciones Finales
- **EXCELENTE** (80+ puntos): Inspector Elite 🏆
- **ACEPTABLE** (50-79 puntos): Trabajo correcto pero mejorable ✅
- **MEJORABLE** (<50 puntos): Necesitas formación adicional ⚠️

### Guardado Automático
- ✅ **Al completar la partida**: Se guarda automáticamente
- 💾 **Al interrumpir (Ctrl+C)**: También se guarda marcada como interrumpida
- 📁 **Archivo**: `puntuaciones.json` (se crea automáticamente)
- 📊 **Información guardada**: 
  - Nombre del inspector
  - Puntuación final
  - Valoración obtenida
  - Riesgos detectados
  - Decisiones correctas
  - Situaciones críticas resueltas (máx. 12)
  - Capítulos completados
  - Fecha y hora de la partida

## 📖 Temas de PRL Cubiertos

### Riesgos Ergonómicos
- Pantallas de visualización de datos (PVD)
- Postura en el puesto de trabajo
- Trastornos musculoesqueléticos (TME)
- Regla 20-20-6 para fatiga visual
- Adaptación de puestos para embarazo
- Ergonomía en teletrabajo

### Seguridad en Instalaciones
- Riesgos de tropiezo y caída
- Señalización de emergencia
- Cables y cableado estructurado
- Instalaciones eléctricas
- Condiciones térmicas
- Iluminación adecuada

### Emergencias
- Evacuación en caso de incendio
- Uso de extintores
- Protocolos del 112
- Responsables de evacuación

### Riesgos Psicosociales
- Acoso laboral (protocolo de actuación)
- Burnout y estrés laboral
- Evaluación de riesgos psicosociales
- Desconexión digital
- Carga de trabajo y jornadas
- Apoyo psicológico

### Riesgos Biológicos y Químicos
- Protección frente a COVID-19
- Rastreo de contactos
- Productos químicos de limpieza
- Fichas de Datos de Seguridad 
- Equipos de Protección Individual (EPIs)

### Protección Especial
- Trabajadoras embarazadas (Ley 31/1995)
- Adaptación de puestos de trabajo
- Vigilancia de la salud específica
- Derecho a cambio de puesto

### Teletrabajo
- Evaluación de riesgos en domicilio
- Equipamiento ergonómico
- Derecho a desconexión digital
- Auditorías virtuales

### Marco Legal
- **Ley 31/1995** de Prevención de Riesgos Laborales
- **RD 486/1997**: Lugares de trabajo (temperatura, iluminación)
- **RD 488/1997**: Pantallas de visualización

## 🛠️ Requisitos

- Python 3.6+
- Terminal con soporte de colores ANSI

## 📝 Licencia

Proyecto educativo sobre Prevención de Riesgos Laborales.

## 👨‍💻 Autor

entreunosyceros

---

**⚠️ Nota**: Este juego tiene fines educativos. Para una implementación real de PRL, consulta a profesionales certificados del tema y la normativa vigente.
