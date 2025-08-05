from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

def format_emotion_response(emotion_dict):
    """
    Wandelt das Emotion Dictionary in den gewünschten String um
    """
    # Emotion Scores extrahieren (ohne dominant_emotion)
    emotions = {k: v for k, v in emotion_dict.items() if k != 'dominant_emotion'}
    
    # String für die Emotion Scores erstellen
    emotion_parts = []
    for emotion, score in emotions.items():
        emotion_parts.append(f"'{emotion}': {score}")
    
    emotion_string = ", ".join(emotion_parts)
    
    # Kompletten String zusammenbauen
    result = f"For the given statement, the system response is {emotion_string}. The dominant emotion is {emotion_dict['dominant_emotion']}."
    
    return result

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
      return "Error"        

    # Jetzt wandelst du das Dictionary in den gewünschten String um
    formatted_string = format_emotion_response(response)

    return formatted_string

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)