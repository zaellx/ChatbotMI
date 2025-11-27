"""
Chatbot Emocional con LLM - Main
Sistema de análisis emocional para estudiantes universitarios
Detecta: ansiedad, estrés, depresión y estado neutral
"""

from chatbot_c import ChatbotEmocional


def main():
    """
    Funcion principal con ejemplos de uso del chatbot.
    """
    print("=" * 60)
    print("CHATBOT EMOCIONAL PARA ESTUDIANTES UNIVERSITARIOS")
    print("=" * 60)
    print()
    
    # inicializar
    chatbot = ChatbotEmocional()
    
    # ej. de mensajes de estudiantes
    ejemplos = [
        {
            'tipo': 'Ansiedad',
            'mensaje': 'Me siento muy nervioso por el examen de mañana. No puedo dejar de pensar en que voy a reprobar. Tengo mucha angustia y no puedo concentrarme.'
        },
        {
            'tipo': 'Estrés',
            'mensaje': 'Estoy completamente abrumado con todas las tareas y proyectos. Tengo 3 exámenes esta semana y no he dormido bien. Me siento muy presionado y agotado.'
        },
        {
            'tipo': 'Depresión',
            'mensaje': 'Últimamente me siento muy triste y sin energía. No tengo ganas de hacer nada y me siento solo. Todo parece vacío y sin sentido.'
        },
        {
            'tipo': 'Neutral',
            'mensaje': 'Hoy tuve un buen día en clases. Entendí los temas y pude terminar mis tareas a tiempo. Me siento bien.'
        }
    ]
    
    # procesar 
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"\n{'='*60}")
        print(f"EJEMPLO {i}: {ejemplo['tipo']}")
        print(f"{'='*60}")
        print(f"\n[Estudiante:] \"{ejemplo['mensaje']}\"\n")
        
        # respuesta del chatbot
        respuesta = chatbot.responder_usuario(ejemplo['mensaje'])
        
        # Mostrar respuesta formateada
        print(f"\n||Chatbot||:")
        print(respuesta['mensaje_completo'])
        
        # Mostrar analisis
        print(f"\n--Analisis:--")
        print(f"   - Palabras analizadas: {respuesta['analisis']['longitud']}")
        print(f"   - Palabras clave detectadas: {respuesta['analisis']['conteo_palabras_clave']}")
        print()
    
    print("=" * 60)
    print("Demostracion completada")
    print("=" * 60)
    
    # -------------------------
    #      MODO INTERACTIVO
    # -------------------------
    print("\n¿Deseas probar el chatbot de forma interactiva? (s/n): ", end='')
    
    respuesta_usuario = input().strip().lower()

    if respuesta_usuario == 's':
        print("\nEscribe 'salir' para terminar\n")
        while True:
            mensaje = input("Tú: ").strip()

            if mensaje.lower() == 'salir':
                print("¡Cuídate! Recuerda que tu bienestar es importante.")
                break

            if mensaje:
                respuesta = chatbot.responder_usuario(mensaje)
                print(f"\nChatbot: {respuesta['mensaje_completo']}\n")


if __name__ == "__main__":
    main()
