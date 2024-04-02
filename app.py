import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import pytz

# Set page config
st.set_page_config(page_title="Penguins Explorer & World Clock", page_icon="🐧", layout="wide")

# Title and introduction
st.title("🐧 Penguins Explorer & World Clock")
st.markdown("""
This app allows you to explore the Penguins dataset and view the current time in various cities around the world.
""")

# Load Penguins data
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv'
    df = pd.read_csv(url)
    return df

df = load_data()

# Data analysis and visualization
st.header("Penguins Data Analysis")
species = st.selectbox('Select species to visualize', df['species'].unique())
filtered_data = df[df['species'] == species]

if not filtered_data.empty:
    st.write(f"Displaying information for {species}")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['flipper_length_mm'], kde=True, ax=ax)
    ax.set_title(f'Flipper Length Distribution for {species}')
    st.pyplot(fig)

# World clock
st.header("World Clock")
cities = {'New York': 'America/New_York', 'London': 'Europe/London', 'Tokyo': 'Asia/Tokyo', 'Sydney': 'Australia/Sydney'}
selected_cities = st.multiselect('Select cities', list(cities.keys()), default=['New York'])

for city in selected_cities:
    timezone = pytz.timezone(cities[city])
    city_time = datetime.now(timezone)
    st.write(f"The current time in {city} is {city_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Explaining the app functionality
st.markdown("""
### Features
- **Penguins Data Analysis**: Select a species to view its flipper length distribution.
- **World Clock**: Select cities to view the current time in each.
""")
