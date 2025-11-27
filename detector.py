"""
Módulo de Detección de Estados Emocionales
Usa LLM para clasificar texto en estados emocionales
"""

from transformers import pipeline
import warnings
from config import (
    MODEL_NAME, MODEL_TASK, MAX_LENGTH, MIN_WORDS,
    ETIQUETAS_NEGATIVAS, ETIQUETAS_POSITIVAS,
    CONTEXTO_ESTRES, CONTEXTO_ANSIEDAD
)
from analizador import analizar_texto

warnings.filterwarnings('ignore')


class DetectorEmocional:
    
    def __init__(self):
        """
        Inicializa el clasificador de sentimientos.
        """
        print("[Cargando modelo de analisis emocional...]")
        self.clasificador = pipeline(
            MODEL_TASK,
            model=MODEL_NAME,
            top_k=None
        )
        print("[Modelo cargado correctamente]\n")
    
    
    def detectar_estado(self, texto):
        """
        Clasifica el texto en un estado emocional.
        """

        # Procesar texto
        analisis = analizar_texto(texto)
        texto_limpio = analisis['texto_limpio']
        conteo = analisis['conteo_palabras_clave']

        # Texto muy corto → neutral
        if analisis['longitud'] < MIN_WORDS:
            return 'neutral'
        
        # Modelo BETO
        try:
            resultado = self.clasificador(texto_limpio[:MAX_LENGTH])[0]

            sentimiento = max(resultado, key=lambda x: x['score'])

            if sentimiento['label'] in ETIQUETAS_NEGATIVAS:
                return self._clasificar_negativo(texto_limpio, conteo)

            elif sentimiento['label'] in ETIQUETAS_POSITIVAS:
                return 'neutral'

            else:
                max_categoria = max(conteo, key=conteo.get)
                return max_categoria if conteo[max_categoria] > 0 else 'neutral'
                
        except Exception as e:
            print(f"[Error en clasificacion:] {e}")
            return self._clasificar_por_palabras_clave(conteo)
    
    
    def _clasificar_negativo(self, texto_limpio, conteo):
        """
        Subclasificación del sentimiento negativo.
        """
        max_categoria = max(conteo, key=conteo.get)

        if conteo[max_categoria] > 0:
            return max_categoria

        if any(p in texto_limpio for p in CONTEXTO_ESTRES):
            return 'estrés'
        if any(p in texto_limpio for p in CONTEXTO_ANSIEDAD):
            return 'ansiedad'

        return 'depresión'
    
    
    def _clasificar_por_palabras_clave(self, conteo):
        max_categoria = max(conteo, key=conteo.get)
        return max_categoria if conteo[max_categoria] > 0 else 'neutral'
