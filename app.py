from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
from sklearn.linear_model import LogisticRegression
import numpy as np

app = Flask(__name__)

# ---------------- AI MODEL (Dummy FRA Approval Predictor) ----------------
# Training data (claims, forest_area) → approval (1 = approved, 0 = rejected)
X = np.array([[10, 100], [50, 200], [30, 150], [80, 400]])
y = np.array([1, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    claims = data.get("claims", 0)
    area = data.get("area", 0)
    pred = model.predict_proba([[claims, area]])[0][1]
    return jsonify({"probability_of_approval": round(float(pred), 2)})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    feedback = data.get("feedback", "")
    polarity = TextBlob(feedback).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return jsonify({
        "feedback": feedback,
        "polarity": polarity,
        "sentiment": sentiment
    }) 

if __name__ == "__main__":
    app.run(debug=True)
