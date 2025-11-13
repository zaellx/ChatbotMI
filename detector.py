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
    """
    Clase para detectar estados emocionales usando un modelo LLM.
    """
    
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
        Clasifica el texto en uno de los estados emocionales.
        
        Args:
            texto (str): Texto a clasificar
            
        Returns:
            str: Estado emocional detectado ['ansiedad', 'estrés', 'depresión', 'neutral']
        """
        # Analizar el texto primero
        analisis = analizar_texto(texto)
        texto_limpio = analisis['texto_limpio']
        conteo = analisis['conteo_palabras_clave']
        
        # si el texto es muy corto, devolver neutral
        if analisis['longitud'] < MIN_WORDS:
            return 'neutral'
        
        # usar el clasificador de sentimientos
        try:
            resultado = self.clasificador(texto_limpio[:MAX_LENGTH])[0]
            
            # Obtener el sentimiento predominante
            sentimiento = max(resultado, key=lambda x: x['score'])
            
            # Si el sentimiento es negativo, determinar el tipo específico
            if sentimiento['label'] in ETIQUETAS_NEGATIVAS:
                return self._clasificar_negativo(texto_limpio, conteo)
            
            # Si es positivo o neutral
            elif sentimiento['label'] in ETIQUETAS_POSITIVAS:
                return 'neutral'
            else:
                # Para sentimientos neutros, verificar palabras clave
                max_categoria = max(conteo, key=conteo.get)
                return max_categoria if conteo[max_categoria] > 0 else 'neutral'
                
        except Exception as e:
            print(f"[Error en clasificacion:] {e}")
            # Fallback: usar solo conteo de palabras clave
            return self._clasificar_por_palabras_clave(conteo)
    
    
    def _clasificar_negativo(self, texto_limpio, conteo):
        """
        Clasifica un sentimiento negativo en subcategoría específica.
        
        Args:
            texto_limpio (str): Texto preprocesado
            conteo (dict): Conteo de palabras clave por categoría
            
        Returns:
            str: Estado emocional específico
        """
        # Buscar el estado con mas palabras clave
        max_categoria = max(conteo, key=conteo.get)
        
        if conteo[max_categoria] > 0:
            return max_categoria
        else:
            # Si no hay palabras clave especificas, determinar por contexto
            if any(palabra in texto_limpio for palabra in CONTEXTO_ESTRES):
                return 'estrés'
            elif any(palabra in texto_limpio for palabra in CONTEXTO_ANSIEDAD):
                return 'ansiedad'
            else:
                return 'depresión'
    
    
    def _clasificar_por_palabras_clave(self, conteo):
        """
        Clasificación fallback usando solo palabras clave.
        
        Args:
            conteo (dict): Conteo de palabras clave por categoría
            
        Returns:
            str: Estado emocional
        """
        max_categoria = max(conteo, key=conteo.get)
        return max_categoria if conteo[max_categoria] > 0 else 'neutral'
