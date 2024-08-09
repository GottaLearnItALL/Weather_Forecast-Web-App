import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select Data to View", options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

# Get the temperature/sky data
if place:
    try:
        filtered_data = get_data(place, days)

        # Create a temperature plot
        if option == "Temperature":
            temperature = [dict_["main"]["temp"]/10 for dict_ in filtered_data]
            dates = [dict_["dt"] for dict_ in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            sky_conditions = [dict_["weather"][0]["main"] for dict_ in filtered_data]
            print(sky_conditions)
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)
    except KeyError:
        st.info("Place entered does not Exist!")