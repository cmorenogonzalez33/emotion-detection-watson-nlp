import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analiza el texto proporcionado para detectar emociones utilizando el servicio Watson NLP.
    """
    # URL del servicio de detección de emociones de Watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Cabeceras requeridas por la API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Cuerpo de la solicitud en formato JSON
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Realizar la solicitud POST al servicio
    response = requests.post(url, json=input_json, headers=headers)
    
    # Retornar el texto de la respuesta (será procesado en la Tarea 3)
    return response.text
  
