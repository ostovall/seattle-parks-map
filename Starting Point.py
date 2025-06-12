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
    # Fix: API field names based on actual dataset
    name = park.get("name", "").strip()
    zip_code = park.get("zip_code", "").strip()

    # Get coordinates
    loc = park.get("location_1", {})
    if not name or "latitude" not in loc or "longitude" not in loc:
        continue  # skip if required data is missing

    lat = float(loc["latitude"])
    lon = float(loc["longitude"])

    # Create popup
    popup_html = f"<b>{name}</b><br>ZIP Code: {zip_code if zip_code else 'N/A'}"
    popup = folium.Popup(popup_html, max_width=300)
    folium.Marker(location=[lat, lon], popup=popup).add_to(marker_cluster)

    if lat == 0 or lon == 0:
        continue  # Skip invalid coordinates

    popup = folium.Popup(f"<b>{name}</b><br>Type: {park_type}<br>Neighborhood: {neighborhood}", max_width=300)
    folium.Marker(location=[lat, lon], popup=popup).add_to(marker_cluster)

# Save map
output_path = "seattle_parks_map.html"
seattle_map.save(output_path)
print(f"Map saved to {output_path}")
# checking the commit works ugh
