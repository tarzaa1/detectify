import torch
import torchvision
from torchvision.transforms import functional as F
from torchvision.models.detection import FasterRCNN_MobileNet_V3_Large_320_FPN_Weights as Weights
from PIL import Image


def load_model():
    # https://pytorch.org/vision/stable/models.html
    model = torchvision.models.detection.fasterrcnn_mobilenet_v3_large_320_fpn(weights=Weights.DEFAULT)
    model.eval()
    return model

def predict(model, image):
    image_tensor = F.to_tensor(image)
    image_tensor = image_tensor.unsqueeze(0)
    with torch.no_grad():
        outputs = model(image_tensor)

    boxes = outputs[0]['boxes']
    labels = outputs[0]['labels']
    scores = outputs[0]['scores']

    return boxes, labels, scores

if __name__ == '__main__':

    model = load_model() 

    image = Image.open('dog_bike_car.jpg').convert("RGB")

    boxes, labels, scores = predict(model, image)

    print(boxes)
    print(labels)
    print(scores)


# wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1KHg5NDAm1ZbVYBsCjLQI3yR8BONBuCBE' -O dog_bike_car.jpg