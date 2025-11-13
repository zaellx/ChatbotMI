from detector import DetectorEmocional
from analizador import analizar_texto
from recomendaciones import recomendar_estrategia, formatear_respuesta


class ChatbotEmocional:
    """
    Chatbot que analiza estados emocionales y proporciona recomendaciones.
    """
    
    def __init__(self):
        """
        Inicializa el chatbot con el detector emocional.
        """
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
        
        # 1. Analizar el texto
        analisis = analizar_texto(mensaje)
        
        # 2. Detectar estado emocional
        estado = self.detector.detectar_estado(mensaje)
        print(f"Estado detectado: {estado.upper()}")
        
        # 3. Obtener recomendación
        recomendacion = recomendar_estrategia(estado)
        
        # 4. Construir respuesta completa
        respuesta = {
            'estado_detectado': estado,
            'analisis': analisis,
            'recomendacion': recomendacion,
            'mensaje_completo': formatear_respuesta(recomendacion)
        }
        
        return respuesta
