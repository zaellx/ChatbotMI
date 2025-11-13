"""
Configuración del Chatbot Emocional
Contiene constantes, palabras clave y configuraciones del modelo
"""

# Configuración del modelo de análisis de sentimientos
MODEL_NAME = "finiteautomata/beto-sentiment-analysis"
MODEL_TASK = "text-classification"
MAX_LENGTH = 512  # Longitud máxima de texto para el modelo

# Umbral mínimo de palabras para análisis
MIN_WORDS = 3

# Estados emocionales posibles
ESTADOS = ['ansiedad', 'estrés', 'depresión', 'neutral']

# Palabras clave para detección de estados emocionales
PALABRAS_CLAVE = {
    'ansiedad': [
        'ansioso', 'ansiosa', 'preocupado', 'preocupada', 'nervioso', 'nerviosa',
        'angustia', 'miedo', 'pánico', 'inquieto', 'inquieta', 'intranquilo',
        'intranquila', 'tenso', 'tensa', 'agobiado', 'agobiada', 'temor',
        'inseguro', 'insegura', 'aterrado', 'aterrada'
    ],
    'estrés': [
        'estresado', 'estresada', 'presión', 'abrumado', 'abrumada', 'agotado',
        'agotada', 'cansado', 'cansada', 'sobrecargado', 'sobrecargada',
        'exámenes', 'examen', 'tareas', 'tarea', 'deadline', 'ocupado', 'ocupada',
        'saturado', 'saturada', 'colapsado', 'colapsada', 'proyecto', 'proyectos'
    ],
    'depresión': [
        'triste', 'deprimido', 'deprimida', 'solo', 'sola', 'vacío', 'vacía',
        'desesperanza', 'melancólico', 'melancólica', 'abatido', 'abatida',
        'desanimado', 'desanimada', 'apático', 'apática', 'sin energía',
        'desmotivado', 'desmotivada', 'inútil', 'sin sentido', 'ganas de nada'
    ]
}

# Palabras contextuales que ayudan a la clasificación
CONTEXTO_ESTRES = [
    'examen', 'tarea', 'proyecto', 'trabajo', 'entrega', 'deadline',
    'estudio', 'universidad', 'clase', 'profesor'
]

CONTEXTO_ANSIEDAD = [
    'preocupa', 'miedo', 'nervioso', 'nerviosa', 'temor', 'pánico',
    'angustia', 'inquieto', 'inquieta'
]

# Etiquetas del modelo de sentimientos
ETIQUETAS_NEGATIVAS = ['NEG', 'negative']
ETIQUETAS_POSITIVAS = ['POS', 'positive']
ETIQUETAS_NEUTRALES = ['NEU', 'neutral']
