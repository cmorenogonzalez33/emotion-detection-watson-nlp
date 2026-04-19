from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Recibe el texto del frontend, lo analiza y devuelve una respuesta formateada.
    """
    # Obtener el texto a analizar desde los parámetros de la URL
    text_to_analyze = request.args.get('textToAnalyze')

    # Ejecutar la función de detección de emociones
    response = emotion_detector(text_to_analyze)

    # Extraer las puntuaciones y la emoción dominante
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Si no se encuentra una emoción dominante (en caso de error futuro)
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Retornar la respuesta formateada como pide la rúbrica
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página principal de la aplicación.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
