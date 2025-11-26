"""
Módulo de Análisis de Texto
Contiene funciones para preprocesar y analizar texto de entrada
"""

import re
from config import PALABRAS_CLAVE


def analizar_texto(texto):
    """
    Preprocesa y analiza el texto de entrada.
    
    Args:
        texto (str): Texto escrito por el estudiante
        
    Returns:
        dict: Diccionario con texto original, texto limpio y características
    """
    # Convertir a minúsculas
    texto_limpio = texto.lower().strip()
    
    #LOS CAMBIOS SE REALIZARON AQUI
    # Eliminar caracteres especiales pero mantener puntuación básica
    texto_limpio = re.sub(r'[^\w\sáéíóúñ.,!?]', '', texto_limpio)
    
    # Eliminar espacios múltiples
    texto_limpio = re.sub(r'\s+', ' ', texto_limpio)
    
    # Contar palabras clave por categoría
    conteo_palabras = contar_palabras_clave(texto_limpio)
    
    return {
        'texto_original': texto,
        'texto_limpio': texto_limpio,
        'longitud': len(texto_limpio.split()),
        'conteo_palabras_clave': conteo_palabras
    }


def contar_palabras_clave(texto_limpio):
    """
    Cuenta las palabras clave por categoría emocional en el texto.
    
    Args:
        texto_limpio (str): Texto preprocesado en minúsculas
        
    Returns:
        dict: Conteo de palabras clave por categoría
    """
    conteo = {
        'ansiedad': 0,
        'estrés': 0,
        'depresión': 0
    }
    
    for categoria, palabras in PALABRAS_CLAVE.items():
        for palabra in palabras:
            conteo[categoria] += texto_limpio.count(palabra)
    
    return conteo


def limpiar_texto(texto):
    """
    Limpia el texto eliminando caracteres especiales y normalizando espacios.
    
    Args:
        texto (str): Texto a limpiar
        
    Returns:
        str: Texto limpio
    """
    texto = texto.lower().strip()
    texto = re.sub(r'[^\w\sáéíóúñ.,!?]', '', texto)
    texto = re.sub(r'\s+', ' ', texto)
    return texto


def extraer_estadisticas(texto):
    """
    Extrae estadísticas básicas del texto.
    
    Args:
        texto (str): Texto a analizar
        
    Returns:
        dict: Estadísticas del texto
    """
    palabras = texto.split()
    return {
        'num_palabras': len(palabras),
        'num_caracteres': len(texto),
        'palabras_promedio': len(texto) / len(palabras) if palabras else 0
    }
