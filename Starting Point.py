import requests
import folium
from folium.plugins import MarkerCluster
import os

# API endpoint
url = "https://data.seattle.gov/resource/v5tj-kqhc.json"

# Fetch data
response = requests.get(url)
parks = response.json()

# Initialize map
seattle_map = folium.Map(location=[47.6062, -122.3321], zoom_start=12)
marker_cluster = MarkerCluster().add_to(seattle_map)

# Categorize and add parks to map
for park in parks:
    name = park.get("park_name", "Unnamed Park")
    loc = park.get("location_1", {})
    lat = float(loc.get("latitude", 0))
    lon = float(loc.get("longitude", 0))
    neighborhood = park.get("neighborhood", "Unknown")
    park_type = park.get("park_type", "Unknown")

    if lat == 0 or lon == 0:
        continue  # Skip invalid coordinates

    popup = folium.Popup(f"<b>{name}</b><br>Type: {park_type}<br>Neighborhood: {neighborhood}", max_width=300)
    folium.Marker(location=[lat, lon], popup=popup).add_to(marker_cluster)

# Save map
output_path = "seattle_parks_map.html"
seattle_map.save(output_path)
print(f"Map saved to {output_path}")
# checking the commit works ugh
