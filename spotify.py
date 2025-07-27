from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

# Set up Client Credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='fb028a528f61413b9dd28acfd87dce93',  # Replace with your Client ID
    client_secret='8ad05c73316a464e8aa76d949016c7c4'  # Replace with your Client Secret
))

# Full track URL (example: Shape of You by Ed Sheeran)
track_url = "https://open.spotify.com/track/6sGhpvvg6vK31bj0Ji6p2f"

# Extract track ID directly from URL using regex
#track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)
if match := re.search(r'track/([A-Za-z0-9]+)', track_url):
    track_id = match.group(1)
else:
    raise ValueError("Invalid track URL")


# Fetch track details
track = sp.track(track_id)
print(track)
# Extract metadata
track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000
}

# Display metadata
print(f"\nTrack Name: {track_data['Track Name']}")
print(f"Artist: {track_data['Artist']}")
print(f"Album: {track_data['Album']}")
print(f"Popularity: {track_data['Popularity']}")
print(f"Duration: {track_data['Duration (minutes)']:.2f} minutes")

# Convert metadata to DataFrame
df = pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)

# Save metadata to CSV
df.to_csv('spotify_track_data.csv', index=False)

# Visualize track data
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

plt.figure(figsize=(8, 5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('Value')
plt.show()
