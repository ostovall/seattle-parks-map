# 🌲 Seattle Parks Interactive Map

**Author:** Olivia Stovall  
**Course:** HCDE 310  
**Date:** June 2025  

## 📍 Project Overview

This project was built to help Seattle residents and visitors explore local parks based on neighborhood and park location. The application fetches real-time data from a public API and generates an interactive map using Python.

The final output is a user-friendly HTML file (`seattle_parks_map.html`) where users can:

- View Seattle parks clustered on a map
- Hover or click to see the park and neighborhood, and more info if it is included in API. 
- Filter visually by clicking on neighborhoods in the city

---

## 🔧 Technologies Used

- `requests` – to fetch data from the Seattle Open Data API  
- `folium` – to create an interactive map with markers and clustering  
- `json` – to parse and manage API responses  
- No API key required  

---

## 🔗 API Details

**API Used:**  
[Seattle Parks and Recreation - Park Addresses API (JSON)](https://data.seattle.gov/resource/v5tj-kqhc.json)

**Key fields used from the dataset:**
- `park_name`
- `location_1` (latitude/longitude)
- `neighborhood`
- `park_type`

This API requires no authentication and returns structured JSON data suitable for mapping.

---

## ▶️ How to Run

1. **Clone or download this repo**
2. Make sure Python 3 is installed
3. Install required packages:

```bash
pip install requests folium
```

4. Run the Python script:

```bash
python Starting\ Point.py
```

5. Open the generated file `seattle_parks_map.html` in any browser.

---

## 📦 Output

The output is a static HTML file:
- **File:** `seattle_parks_map.html`
- **Type:** Interactive leaflet map
- **Features:** Clickable markers, category info, park names

---

## 🎯 Minimum Functionality Delivered

✅ Used a new API (Socrata/Seattle Open Data API)  
✅ Pulled real-time JSON data  
✅ Processed and filtered parks by coordinates and categories  
✅ Generated user-friendly HTML output  
✅ Used a new module (`folium`) not covered in class  

---

## 🚀 Stretch Goal (partial)

Implemented marker clustering to improve map readability with dense park distributions.

---

## 🎥 Video

See the project demo video [link goes here when uploaded].

---

## 👩‍💻 Instructor Access

This repo is public

## 📜 Acknowledgments

Project structure and problem-solving were supported by class materials and AI editing via ChatGPT (June 2025). All code and logic are original.
