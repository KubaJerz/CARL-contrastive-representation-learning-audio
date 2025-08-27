import requests

query = "Drake"
url = f"https://itunes.apple.com/search?term={query}&media=music&limit=5"
response = requests.get(url).json()

for result in response['results']:
    print(result['trackName'], "->", result['previewUrl'])


preview_url = result['previewUrl']
audio_data = requests.get(preview_url).content

with open("preview.mp3", "wb") as f:
    f.write(audio_data)
