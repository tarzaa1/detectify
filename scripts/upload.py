import requests
from decouple import config

url = config('ENDPOINT_URL', default='http://127.0.0.1:5000/upload')
image_path = config('IMAGE_PATH', default='data/dog_bike_car.jpg') 
with open(image_path, 'rb') as f:
    byte_im = f.read()

x = requests.post(url, data = byte_im)

print(x.text)
