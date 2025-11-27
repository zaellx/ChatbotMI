"""
Utilidades de WordNet para español (OMW)
"""

from nltk.corpus import wordnet as wn

def obtener_sinonimos_es(texto):
    """
    Devuelve un set con palabras del texto y sus sinónimos en español (spa).
    """
    palabras = texto.split()
    sinonimos = set(palabras)

    for palabra in palabras:
        # obtener synsets en español
        synsets = wn.synsets(palabra, lang='spa')
        for syn in synsets:
            try:
                lemma_names = syn.lemma_names(lang='spa')
            except TypeError:
                # compatibilidad con versiones de NLTK
                lemma_names = [l for l in syn.lemma_names() if isinstance(l, str)]
            for lemma in lemma_names:
                sinonimos.add(lemma.replace("_", " ").lower())

    return sinonimos


def expandir_palabras_clave(PALABRAS_CLAVE):
    """
    Expande las listas de PALABRAS_CLAVE con sinónimos de WordNet (devuelve dict con sets).
    """
    nuevas = {}
    for categoria, palabras in PALABRAS_CLAVE.items():
        nuevas[categoria] = set()
        for palabra in palabras:
            nuevas[categoria].add(palabra.lower())
            synsets = wn.synsets(palabra, lang='spa')
            for syn in synsets:
                try:
                    lemma_names = syn.lemma_names(lang='spa')
                except TypeError:
                    lemma_names = [l for l in syn.lemma_names() if isinstance(l, str)]
                for lemma in lemma_names:
                    nuevas[categoria].add(lemma.replace("_", " ").lower())
    return nuevas
