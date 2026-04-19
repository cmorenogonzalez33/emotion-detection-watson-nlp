import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analiza el texto y formatea la salida para extraer puntuaciones y la emoción dominante.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convertir la respuesta de texto a un diccionario de Python
    formatted_response = json.loads(response.text)
    
    # Extraer el conjunto de emociones (asumiendo la estructura de Watson NLP)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Encontrar la emoción con la puntuación más alta
    emotion_list = [anger, disgust, fear, joy, sadness]
    emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant_emotion = emotion_keys[emotion_list.index(max(emotion_list))]
    
    # Crear el diccionario de salida requerido por la rúbrica
    result = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
    
    return result
