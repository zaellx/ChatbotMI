# 🤖 Chatbot Emocional con LLM

Sistema de análisis emocional para estudiantes universitarios que detecta señales de ansiedad, estrés o depresión y proporciona recomendaciones personalizadas.

## 📁 Estructura del Proyecto

```
ChatbotMINV/
│
├── chatbot.py              # Archivo principal (main)
├── chatbot_core.py         # Clase principal del chatbot
├── config.py               # Configuración y constantes
├── analizador.py           # Módulo de análisis de texto
├── detector.py             # Módulo de detección emocional
├── recomendaciones.py      # Módulo de recomendaciones
└── README.md              # Este archivo
```

## 📦 Módulos

### 1. `config.py`

Contiene todas las configuraciones y constantes:

- Nombre del modelo LLM
- Palabras clave por categoría emocional
- Estados emocionales posibles
- Parámetros de configuración

### 2. `analizador.py`

Funciones de preprocesamiento y análisis:

- `analizar_texto(texto)`: Preprocesa y analiza el texto
- `contar_palabras_clave(texto)`: Cuenta palabras clave emocionales
- `limpiar_texto(texto)`: Limpia y normaliza el texto
- `extraer_estadisticas(texto)`: Extrae métricas del texto

### 3. `detector.py`

Detección de estados emocionales:

- `DetectorEmocional`: Clase que usa el modelo BETO
- `detectar_estado(texto)`: Clasifica el texto en estados emocionales
- Combina análisis LLM con palabras clave

### 4. `recomendaciones.py`

Estrategias y técnicas por estado:

- `recomendar_estrategia(estado)`: Obtiene recomendación según estado
- `formatear_respuesta(recomendacion)`: Formatea el mensaje
- Funciones específicas por estado emocional

### 5. `chatbot_core.py`

Clase principal que integra todo:

- `ChatbotEmocional`: Clase principal
- `responder_usuario(mensaje)`: Función de flujo completo

### 6. `chatbot.py`

Archivo principal de ejecución:

- Función `main()` con ejemplos
- 4 casos de uso predefinidos
- Modo interactivo (opcional)

## 🚀 Uso

### Ejecución básica:

```powershell
# Activar entorno virtual
.\chatbotMI\Scripts\Activate.ps1

# Ejecutar el chatbot
python chatbot.py
```

### Uso en código:

```python
from chatbot_core import ChatbotEmocional

# Inicializar chatbot
chatbot = ChatbotEmocional()

# Analizar mensaje
mensaje = "Me siento muy estresado con los exámenes"
respuesta = chatbot.responder_usuario(mensaje)

# Acceder a resultados
print(f"Estado: {respuesta['estado_detectado']}")
print(respuesta['mensaje_completo'])
```

## 🎯 Estados Detectados

- **Ansiedad**: Nerviosismo, preocupación, angustia
- **Estrés**: Presión, sobrecarga, agotamiento
- **Depresión**: Tristeza, desmotivación, vacío
- **Neutral**: Estado equilibrado

## 📋 Funciones Principales

### `analizar_texto(texto)`

```python
resultado = {
    'texto_original': str,
    'texto_limpio': str,
    'longitud': int,
    'conteo_palabras_clave': dict
}
```

### `detectar_estado(texto)`

```python
estado = 'ansiedad' | 'estrés' | 'depresión' | 'neutral'
```

### `recomendar_estrategia(estado)`

```python
recomendacion = {
    'titulo': str,
    'mensaje': str,
    'tecnicas': list,
    'recordatorio': str,
    'recursos': str (opcional)
}
```

### `responder_usuario(mensaje)`

```python
respuesta = {
    'estado_detectado': str,
    'analisis': dict,
    'recomendacion': dict,
    'mensaje_completo': str
}
```

## 🔧 Dependencias

- Python 3.8+
- transformers
- torch
- re (built-in)

## 💡 Ejemplos de Salida

El sistema procesa 4 ejemplos automáticamente:

1. Caso de ansiedad
2. Caso de estrés
3. Caso de depresión
4. Caso neutral

Cada uno muestra:

- Mensaje del estudiante
- Estado detectado
- Recomendaciones personalizadas
- Técnicas específicas
- Análisis técnico

## 🤝 Características

✅ Arquitectura modular y escalable
✅ Separación de responsabilidades
✅ Fácil mantenimiento
✅ Código documentado
✅ Configuración centralizada
✅ Reutilización de componentes

## 📝 Notas

- El modelo BETO está optimizado para español
- Las recomendaciones están basadas en técnicas psicológicas validadas
- El sistema es una herramienta de apoyo, no sustituye ayuda profesional
