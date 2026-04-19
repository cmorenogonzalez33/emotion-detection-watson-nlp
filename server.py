from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analiza el texto recibido y maneja casos de error o entradas vacías.
    """
    # Obtener el texto del parámetro de la URL
    text_to_analyze = request.args.get('textToAnalyze')

    # Ejecutar la función de detección
    response = emotion_detector(text_to_analyze)

    # Extraer la emoción dominante para validar
    dominant_emotion = response['dominant_emotion']

    # VALIDACIÓN DE ERROR: Si la emoción es None, el texto es inválido
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Si todo está bien, formatear la respuesta exitosa
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page()
