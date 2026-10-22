import streamlit as st
import requests

st.set_page_config(page_title="API + JSON Demo")
st.title("API Integration + JSON + Secrets")
st.write("This app calls the public Open-Meteo geocoding and forecast APIs; no API key is required.")
city = st.text_input("Enter city", "Chennai")
if st.button("Get Weather"):
    try:
        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1, "language": "en", "format": "json"},
            timeout=15,
        )
        geo.raise_for_status()
        locations = geo.json().get("results", [])
        if not locations:
            st.error("City not found. Check the spelling and try again.")
        else:
            place = locations[0]
            forecast = requests.get(
                "https://api.open-meteo.com/v1/forecast",
                params={"latitude": place["latitude"], "longitude": place["longitude"],
                        "current": "temperature_2m,relative_humidity_2m,apparent_temperature",
                        "timezone": "auto"},
                timeout=15,
            )
            forecast.raise_for_status()
            payload = {"location": f"{place['name']}, {place.get('country', '')}",
                       "current_weather": forecast.json().get("current", {})}
            st.subheader("JSON response")
            st.json(payload)
            current = payload["current_weather"]
            c1, c2, c3 = st.columns(3)
            c1.metric("Temperature", f"{current.get('temperature_2m', '—')} °C")
            c2.metric("Feels like", f"{current.get('apparent_temperature', '—')} °C")
            c3.metric("Humidity", f"{current.get('relative_humidity_2m', '—')}%")
    except requests.RequestException as exc:
        st.error(f"API request failed: {exc}")
st.divider()
st.subheader("Common HTTP methods")
st.markdown("- **GET** — retrieve data\n- **POST** — submit data\n- **PUT/PATCH** — update data\n- **DELETE** — remove data")
