import os
import requests

# Ensure directory exists
os.makedirs("data/raw", exist_ok=True)

def fetch_previews(term="top", limit=200):
    """
    Query Apple iTunes API for songs matching `term`.
    Saves preview mp3s to data/raw/{trackId}.mp3
    """
    url = "https://itunes.apple.com/search"
    params = {
        "term": term,
        "media": "music",
        "limit": limit
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    for track in data.get("results", []):
        track_id = track.get("trackId")
        preview_url = track.get("previewUrl")
        if not track_id or not preview_url:
            continue

        try:
            audio = requests.get(preview_url, timeout=10).content
            file_path = f"data/raw/{track_id}.mp3"
            with open(file_path, "wb") as f:
                f.write(audio)
            print(f"✅ Saved: {file_path}")
        except Exception as e:
            print(f"⚠️ Failed for {track_id}: {e}")

# Example run: fetch 200 "top" songs
fetch_previews("top", limit=200)
