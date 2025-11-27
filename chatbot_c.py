# ==========================================
# NOMBRE DEL ARCHIVO: chatbot_c.py
# DESCRIPCIÓN: Define la clase principal que coordina el chatbot.
# ==========================================

# NOTA IMPORTANTE: Asegúrate de tener los archivos detector.py,
# analizador.py y recomendaciones.py en la misma carpeta.
try:
    from detector import DetectorEmocional
    from analizador import analizar_texto
    from recomendaciones import recomendar_estrategia, formatear_respuesta
except ImportError as e:
    print(f"\nERROR CRÍTICO DE IMPORTACIÓN EN chatbot_c.py:")
    print(f"Falta un archivo necesario: {e.name}.py")
    print("Asegúrate de que 'detector.py', 'analizador.py' y 'recomendaciones.py' existan.")
    exit()

class ChatbotEmocional:
    """
    Chatbot que analiza estados emocionales y proporciona recomendaciones.
    """
    
    def __init__(self):
        """
        Inicializa el chatbot con el detector emocional.
        """
        # Se asume que DetectorEmocional existe en detector.py
        self.detector = DetectorEmocional()
    
    
    def responder_usuario(self, mensaje):
        """
        Funcion principal que combina todo el flujo del chatbot.
        
        Args:
            mensaje (str): Mensaje del estudiante
            
        Returns:
            dict: Respuesta completa del chatbot con análisis y recomendaciones
        """
        print("="*60)
        print("Procesando mensaje...")
        
        # 1. Analizar el texto (Usa la función de analizador.py)
        analisis = analizar_texto(mensaje)
        
        # 2. Detectar estado emocional (Usa la clase de detector.py)
        # NOTA: Se asume que el método detectar_estado existe.
        # Si tu detector usa el resultado del análisis, podrías necesitar cambiar esto a:
        # estado = self.detector.detectar_estado(analisis['conteo_palabras_clave'])
        estado = self.detector.detectar_estado(mensaje)
        print(f"Estado detectado: {estado.upper()}")
        
        # 3. Obtener recomendación (Usa la función de recomendaciones.py)
        recomendacion = recomendar_estrategia(estado)
        
        # 4. Construir respuesta completa
        respuesta = {
            'estado_detectado': estado,
            'analisis': analisis,
            'recomendacion': recomendacion,
            # Usa la función de formateo de recomendaciones.py
            'mensaje_completo': formatear_respuesta(recomendacion)
        }
        
        return respuesta