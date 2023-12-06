from flask import Flask, request
from detectify.inference import load_model, predict
from PIL import Image
import io
import json

from detectify.conf import (
    APP_ADDRESS,
    APP_PORT,
    DEBUG
)


app = Flask(__name__)

model = load_model()

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
    app.run(host=APP_ADDRESS, port=APP_PORT, debug=DEBUG)

