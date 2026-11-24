"""Serve the Watson emotion detection application."""

from flask import Flask, render_template, request
from requests.exceptions import RequestException

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Display the emotion detection form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def analyze():
    """Analyze the submitted text and describe the dominant emotion."""
    text = request.args.get("textToAnalyze", "").strip()
    if not text:
        return "Invalid text! Please try again!"
    try:
        result = emotion_detector(text)
    except RequestException:
        return "Emotion service unavailable. Please try again later.", 502
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    scores = ", ".join(f"'{name}': {result[name]}" for name in (
        "anger", "disgust", "fear", "joy", "sadness"
    ))
    return (f"For the given statement, the system response is {scores}. "
            f"The dominant emotion is {result['dominant_emotion']}.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
