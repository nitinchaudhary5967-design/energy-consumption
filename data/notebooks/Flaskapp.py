# app/app.py
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import datetime

app = Flask(__name__)
artifact = joblib.load("models/model.pkl")
model = artifact["model"]
features = artifact["features"]

@app.route("/")
def index():
    return render_template("index.html")  # simple form or dashboard

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # expect keys: kwh, voltage, current, temperature, hour, dayofweek
    X = [data.get(f) for f in features]
    pred = model.predict([X])[0]
    return jsonify({"prediction_kwh_next": float(pred)})

@app.route("/gen_insight", methods=["POST"])
def gen_insight():
    # Here call your GenAI function (see above) with prepared summary
    summary = request.json.get("summary","")
    # resp = generate_insights(summary, api_key)
    # For demo:
    resp = {"insights":"Peak consumption at 18-21 hours. Consider shifting loads..."}
    return jsonify(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
