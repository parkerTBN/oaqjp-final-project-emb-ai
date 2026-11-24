# Final project

This Flask application uses IBM Watson NLP to score anger, disgust, fear, joy,
and sadness in English text and report the dominant emotion.

In the course lab, run the following commands from the repository root.

```sh
python3 -m pip install -r requirements.txt
python3 -m unittest -v test_emotion_detection
python3 -m pylint server.py
python3 server.py
```

Open port 5000 in the lab preview. Predictions and model tests require access
to the Skills Network Watson emotion service.
