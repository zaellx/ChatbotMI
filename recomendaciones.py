"""
Módulo de Recomendaciones
Contiene las estrategias y técnicas por estado emocional
"""


def recomendar_estrategia(estado):
    """
    Devuelve una recomendación personalizada según el estado emocional.
    
    Args:
        estado (str): Estado emocional detectado
        
    Returns:
        dict: Recomendación con título, descripción y técnicas
    """
    recomendaciones = {
        'ansiedad': obtener_recomendacion_ansiedad(),
        'estrés': obtener_recomendacion_estres(),
        'depresión': obtener_recomendacion_depresion(),
        'neutral': obtener_recomendacion_neutral()
    }
    
    return recomendaciones.get(estado, recomendaciones['neutral'])


def obtener_recomendacion_ansiedad():
    """
    Recomendaciones para estado de ansiedad.
    
    Returns:
        dict: Recomendación estructurada
    """
    return {
        'titulo': 'Técnicas para Reducir la Ansiedad',
        'mensaje': 'Entiendo que te sientes ansioso/a. Es normal sentirse así, especialmente durante la universidad.',
        'tecnicas': [
            '**Respiración 4-7-8**: Inhala por 4 segundos, mantén 7 segundos, exhala por 8 segundos. Repite 4 veces.',
            '**Técnica de los 5 sentidos**: Identifica 5 cosas que ves, 4 que tocas, 3 que oyes, 2 que hueles, 1 que saboreas.',
            '**Mindfulness**: Concéntrate en el momento presente. Observa tus pensamientos sin juzgarlos.',
            '**Ejercicio físico**: Una caminata de 10-15 minutos puede reducir significativamente la ansiedad.',
            '**Visualización**: Imagina un lugar seguro y tranquilo. Visualiza cada detalle con tus sentidos.'
        ],
        'recordatorio':  'Recuerda: La ansiedad es temporal. Tú eres más fuerte de lo que crees.'
    }


def obtener_recomendacion_estres():
    """
    Recomendaciones para estado de estrés.
    
    Returns:
        dict: Recomendación estructurada
    """
    return {
        'titulo': 'Estrategias para Manejar el Estrés',
        'mensaje': 'Noto que estás bajo mucho estrés. Es importante que tomes un momento para ti.',
        'tecnicas': [
            '**Respiración diafragmática**: Coloca una mano en tu pecho y otra en tu abdomen. Respira profundo haciendo que solo se mueva el abdomen.',
            '**Técnica Pomodoro**: Trabaja 25 minutos, descansa 5. Cada 4 ciclos, descansa 15-30 minutos.',
            '**Priorización**: Haz una lista de tareas y ordénalas por urgencia e importancia (Matriz de Eisenhower).',
            '**Pausas activas**: Cada hora, levántate, estira y camina 2-3 minutos.',
            '**Desconexión digital**: Apaga notificaciones por 30 minutos mientras estudias o trabajas.',
            '**Organización**: Divide proyectos grandes en tareas pequeñas y manejables.'
        ],
        'recordatorio': 'Recuerda: No puedes llenar de una jarra vacía. Cuídate primero.'
    }


def obtener_recomendacion_depresion():
    """
    Recomendaciones para estado de depresión.
    
    Returns:
        dict: Recomendación estructurada
    """
    return {
        'titulo': 'Apoyo para Momentos Difíciles',
        'mensaje': 'Veo que estás pasando por un momento difícil. Quiero que sepas que no estás solo/a.',
        'tecnicas': [
            '**Rutina matutina**: Establece una hora fija para despertar y una actividad placentera (música, ducha, desayuno).',
            '**Gratitud diaria**: Escribe 3 cosas por las que estás agradecido/a cada día, por pequeñas que sean.',
            '**Conexión social**: Contacta a un amigo o familiar. Un mensaje simple puede hacer la diferencia.',
            '**Actividad física suave**: Yoga, estiramientos o una caminata corta pueden mejorar tu ánimo.',
            '**Pequeños logros**: Celebra cada tarea completada, sin importar cuán pequeña sea.',
            '**Luz natural**: Exponte a la luz del sol al menos 15 minutos al día.'
        ],
        'recordatorio': 'Recuerda: Está bien no estar bien. Considera hablar con un profesional si estos sentimientos persisten.',
        'recursos': 'Línea de apoyo psicológico universitario: Consulta en tu institución.'
    }


def obtener_recomendacion_neutral():
    """
    Recomendaciones para estado neutral.
    
    Returns:
        dict: Recomendación estructurada
    """
    return {
        'titulo': '¡Todo en Orden!',
        'mensaje': '¡Me alegra saber que te encuentras bien! Aquí estoy si necesitas algo.',
        'tecnicas': [
            '**Mantén el equilibrio**: Sigue con tus rutinas saludables de sueño, alimentación y ejercicio.',
            '**Prevención**: Practica técnicas de respiración regularmente, no solo en momentos de estrés.',
            '**Conexión social**: Mantén contacto con amigos y seres queridos.',
            '**Autocuidado**: Dedica tiempo a actividades que disfrutes.',
            '**Reflexión**: Lleva un diario de emociones para identificar patrones.'
        ],
        'recordatorio': 'Recuerda: El bienestar es un proceso continuo. Sigue cuidándote.'
    }


def formatear_respuesta(recomendacion):
    """
    Formatea la recomendación en un mensaje legible.
    
    Args:
        recomendacion (dict): Diccionario con la recomendación
        
    Returns:
        str: Mensaje formateado
    """
    mensaje = f"\n{recomendacion['titulo']}\n\n"
    mensaje += f"{recomendacion['mensaje']}\n\n"
    mensaje += "**Técnicas recomendadas:**\n\n"
    
    for i, tecnica in enumerate(recomendacion['tecnicas'], 1):
        mensaje += f"{i}. {tecnica}\n\n"
    
    mensaje += f"\n{recomendacion['recordatorio']}\n"
    
    if 'recursos' in recomendacion:
        mensaje += f"\n{recomendacion['recursos']}\n"
    
    return mensaje
