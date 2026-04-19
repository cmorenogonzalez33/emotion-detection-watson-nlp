"""
Ejecución de un servidor de detección de emociones utilizando Flask.
Este módulo define las rutas para la interfaz web y la API de detección.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analiza el texto recibido a través de la interfaz web y devuelve
    las puntuaciones de las emociones y la emoción dominante.
    """
    # Obtener el texto a analizar desde los argumentos de la URL
    text_to_analyze = request.args.get('textToAnalyze')

    # Ejecutar la función de detección de emociones
    response = emotion_detector(text_to_analyze)

    # Extraer los valores de la respuesta
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Manejo de casos donde la entrada es inválida o vacía
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Retornar la respuesta formateada según los requisitos del proyecto
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página principal de la aplicación.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Ejecuta la aplicación en el host local en el puerto 5000
    app.run(host="0.0.0.0", port=5000)
