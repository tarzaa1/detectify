from flask import Flask, request
from inference import load_model, predict
from PIL import Image
import io
import json

app = Flask(__name__)

model = load_model()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload", methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        data = request.get_data()
        image = Image.open(io.BytesIO(data)).convert("RGB")
        boxes, labels, scores = predict(model, image)
        res = {
            'boxes': boxes.tolist(),
            'labels': labels.tolist(),
            'scores': scores.tolist()

        }
        return json.dumps(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

