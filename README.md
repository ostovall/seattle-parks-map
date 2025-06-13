# Seattle Parks Interactive Map

An interactive map of Seattle's public parks built with Python and Folium, using open data from the Seattle Parks and Recreation dataset.

## What This Project Does

This app fetches live JSON data from Seattle's open data API and plots public parks on an interactive, zoomable map with clustered markers. Clicking a marker reveals the park's name. It makes it easier to visually explore parks across ZIP codes.

## How to Run It

1. Clone or download this repository.
2. Ensure you have Python 3 installed.
3. Install dependencies:

pip install folium requests

markdown
Copy
Edit

4. Run the script:

python Starting\ Point.py

markdown
Copy
Edit

5. Open the generated `seattle_parks_map.html` file in your web browser.

## Data Source

- API Endpoint: https://data.seattle.gov/resource/v5tj-kqhc.json  
- API Docs: https://dev.socrata.com/foundry/data.seattle.gov/v5tj-kqhc  
- No API key is required.

## Features

- Interactive Leaflet.js map via Folium
- Clustering for park markers
- Automatic map centering over Seattle
- Skips parks with missing or incomplete data

## Live Demo (if GitHub Pages is enabled)

If enabled, the site will be viewable at:

https://ostovall.github.io/seattle-parks-map/

markdown
Copy
Edit

## Acknowledgments

- Seattle Open Data Portal (data.seattle.gov)  
- Socrata API Tools  
- Folium + Leaflet.js
- Chatgpt asked to debugged but code content and ideas are my own. 
