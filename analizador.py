# ==========================================
# NOMBRE DEL ARCHIVO: analizador.py
# ==========================================
"""
Módulo de Análisis de Texto
Contiene funciones para preprocesar y analizar texto de entrada
usando NLTK y WordNet para sinónimos.
"""

import re
import nltk
from nltk.corpus import wordnet as wn

# Intentar importar la configuración
try:
    from config import PALABRAS_CLAVE
except ImportError:
    print("\n[ERROR CRÍTICO] No se encontró 'config.py'.")
    print("Asegúrate de tener el archivo con el diccionario PALABRAS_CLAVE.\n")
    exit()

# --- DESCARGA AUTOMÁTICA DE RECURSOS NLTK ---
# Verifica si los datos necesarios están presentes, si no, los descarga.
try:
    wn.ensure_loaded()
except LookupError:
    print("--- Descargando recursos necesarios de NLTK para español... ---")
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    print("--- Descarga completada. ---")


# --- función para obtener sinónimos en español ---
def obtener_sinonimos_es(palabra):
    """
    Devuelve una lista de sinónimos en español usando WordNet.
    """
    sinonimos = set()
    # Buscar synsets en español. Requiere omw-1.4 descargado.
    for synset in wn.synsets(palabra, lang='spa'):
        for lemma in synset.lemmas(lang='spa'):
            # Normalizar: minúsculas y cambiar guiones bajos por espacios
            sinonimos.add(lemma.name().lower().replace("_", " "))

    return list(sinonimos)


def limpiar_texto(texto):
    """
    Limpia el texto eliminando caracteres especiales y normalizando espacios.
    """
    # Convertir a minúsculas y quitar espacios al inicio/final
    texto = texto.lower().strip()
    
    # Eliminar caracteres especiales pero mantener puntuación básica, ñ y acentos
    texto = re.sub(r'[^\w\sáéíóúñ.,!?]', '', texto)
    
    # Eliminar espacios múltiples y dejar solo uno
    texto = re.sub(r'\s+', ' ', texto)
    
    return texto


def contar_palabras_clave(texto_limpio):
    """
    Cuenta las palabras clave por categoría emocional en el texto.
    Utiliza WordNet para incluir sinónimos en español.
    CORRECCIÓN IMPORTANTE: Usa tokenización para evitar falsos positivos.
    """
    # Inicializamos el conteo en 0 para todas las categorías del config
    conteo = {key: 0 for key in PALABRAS_CLAVE.keys()}
    
    # 1. TOKENIZAR: Dividir el texto en una lista de palabras
    # Esto es vital para que .count() funcione en palabras exactas
    tokens = texto_limpio.split()

    for categoria, palabras in PALABRAS_CLAVE.items():
        for palabra in palabras:
            # Obtenemos los sinónimos de esta palabra clave
            sinonimos = obtener_sinonimos_es(palabra)
            
            # Creamos un set con la palabra original Y sus sinónimos
            # Usamos set para evitar contar doble si la palabra ya estaba en los sinónimos
            palabras_a_buscar = set([palabra] + sinonimos)

            for palabra_buscada in palabras_a_buscar:
                 # 2. CONTAR EN LA LISTA (TOKENS):
                 # Ahora buscamos la palabra exacta en la lista de tokens.
                 # "ira" NO coincidirá con "mirar" aquí.
                 conteo[categoria] += tokens.count(palabra_buscada)
                 
    return conteo


def analizar_texto(texto):
    """
    Función principal que orquesta el preprocesamiento y análisis.
    """
    # 1. Limpiar el texto
    texto_limpio = limpiar_texto(texto)
    
    # 2. Contar palabras clave (usando la versión tokenizada)
    conteo_palabras = contar_palabras_clave(texto_limpio)
    
    # Calcular longitud en palabras
    tokens = texto_limpio.split()
    longitud = len(tokens)
    
    return {
        'texto_original': texto,
        'texto_limpio': texto_limpio,
        'longitud': longitud,
        'conteo_palabras_clave': conteo_palabras
    }

# (La función extraer_estadisticas es opcional, si no la usas puedes borrarla)
def extraer_estadisticas(texto):
    palabras = texto.split()
    return {
        'num_palabras': len(palabras),
        'num_caracteres': len(texto),
        'palabras_promedio': len(texto) / len(palabras) if palabras else 0
    }