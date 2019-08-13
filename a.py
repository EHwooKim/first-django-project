import requests

response = requests.get('http://artii.herokuapp.com/make?text=TAEWOO&font=acrobatic')
x = response.text


print(x)