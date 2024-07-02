import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = Flask(__name__)
CORS(app, origins=["http://localhost", "http://localhost:3000"], supports_credentials=True)

model_path = os.path.join(os.path.dirname(__file__), '../models/1.keras')

MODEL = tf.keras.models.load_model(model_path)

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.route("/")
def welcome():
    return render_template("p2.html")

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        image = read_file_as_image(file.read())
        img_batch = np.expand_dims(image, 0)
        
        predictions = MODEL.predict(img_batch)

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        return jsonify({
            'class': predicted_class,
            'confidence': float(confidence)
        })
    else:
        return jsonify({'error': 'File processing failed'}), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)


