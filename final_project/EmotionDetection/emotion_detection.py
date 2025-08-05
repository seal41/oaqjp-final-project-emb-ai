import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion detection  service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    data = json.loads(response.text)

    if response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    elif response.status_code == 200:

        # Emotionen extraction
        emotions = data['emotionPredictions'][0]['emotion']
    
        # find dominant emotion 
        dominant_emotion = max(emotions, key=emotions.get)
   
        # create Result Dictionary
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

    # Returning a dictionary containing emotion detection  results
    return result
    