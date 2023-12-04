import requests

url = 'http://127.0.0.1:8000/upload'
with open('dog_bike_car.jpg', 'rb') as f:
    byte_im = f.read()

x = requests.post(url, data = byte_im)

print(x.text)
