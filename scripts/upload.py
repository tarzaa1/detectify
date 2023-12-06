import requests

url = 'http://127.0.0.1:8000/upload'
image_path = 'data/dog_bike_car.jpg' 
with open(image_path, 'rb') as f:
    byte_im = f.read()

x = requests.post(url, data = byte_im)

print(x.text)