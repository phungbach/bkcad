import requests


data = requests.get('https://637f75cb5b1cc8d6f946181e.mockapi.io/api/v1/quanlyhocvien').json()

print(data)