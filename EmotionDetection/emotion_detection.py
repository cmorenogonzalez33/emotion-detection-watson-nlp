import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analiza el texto y maneja errores de entrada (código 400).
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Manejo del código de estado 400 (Error del cliente/Entrada inválida)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Si la respuesta es exitosa (200), procesamos normalmente
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    emotion_list = [anger, disgust, fear, joy, sadness]
    emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant_emotion = emotion_keys[emotion_list.index(max(emotion_list))]
    
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
