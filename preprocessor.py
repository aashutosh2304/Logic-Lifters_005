import pandas as pd
import streamlit as st
import plotly.express as px


# Multiselect function
def multiselect(title,options_list):
    selected = st.sidebar.multiselect(title, options_list)
    select_all = st.sidebar.checkbox("Select all", value = True, key = title)
    if select_all:
        selected_options = options_list
    else:
        selected_options = selected
    return selected_options


def display(filtered_df):
    crime_rate = filtered_df.groupby("STATE/UT")["Total Crimes"].sum().reset_index()
    state_coordinates = {
        'Andhra pradesh': {'Lat': 15.9129, 'Lon': 79.7400},
        'Arunachal pradesh': {'Lat': 28.2180, 'Lon': 94.7278},
        'Assam': {'Lat': 26.2006, 'Lon': 92.9376},
        'Bihar': {'Lat': 25.0961, 'Lon': 85.3131},
        'Chhattisgarh': {'Lat': 21.2787, 'Lon': 81.8661},
        'Goa': {'Lat': 15.2993, 'Lon': 74.1240},
        'Gujarat': {'Lat': 22.2587, 'Lon': 71.1924},
        'Haryana': {'Lat': 29.0588, 'Lon': 76.0856},
        'Himachal pradesh': {'Lat': 31.1048, 'Lon': 77.1734},
        'Jammu & kashmir': {'Lat': 33.7782, 'Lon': 76.5762},
        'Jharkhand': {'Lat': 23.6102, 'Lon': 85.2799},
        'Karnataka': {'Lat': 15.3173, 'Lon': 75.7139},
        'Kerala': {'Lat': 10.8505, 'Lon': 76.2711},
        'Madhya pradesh': {'Lat': 22.9734, 'Lon': 78.6569},
        'Maharashtra': {'Lat': 19.7515, 'Lon': 75.7139},
        'Manipur': {'Lat': 24.6637, 'Lon': 93.9063},
        'Meghalaya': {'Lat': 25.4670, 'Lon': 91.3662},
        'Mizoram': {'Lat': 23.1645, 'Lon': 92.9376},
        'Nagaland': {'Lat': 26.1584, 'Lon': 94.5624},
        'Odisha': {'Lat': 20.9517, 'Lon': 85.0985},
        'Punjab': {'Lat': 31.1471, 'Lon': 75.3412},
        'Rajasthan': {'Lat': 27.0238, 'Lon': 74.2179},
        'Sikkim': {'Lat': 27.5330, 'Lon': 88.5122},
        'Tamil nadu': {'Lat': 11.1271, 'Lon': 78.6569},
        'Tripura': {'Lat': 23.9408, 'Lon': 91.9882},
        'Uttar pradesh': {'Lat': 26.8467, 'Lon': 80.9462},
        'Uttarakhand': {'Lat': 30.0668, 'Lon': 79.0193},
        'West bengal': {'Lat': 22.9868, 'Lon': 87.8550},
        'A & n islands': {'Lat': 11.7401, 'Lon': 92.6586},
        'Chandigarh': {'Lat': 30.7333, 'Lon': 76.7794},
        'D & n haveli': {'Lat': 20.3974, 'Lon': 72.8328},
        'Daman & diu': {'Lat': 20.3974, 'Lon': 72.8328},
        'Delhi': {'Lat': 28.7041, 'Lon': 77.1025},
        'Lakshadweep': {'Lat': 10.5667, 'Lon': 72.6417},
        'Puducherry': {'Lat': 11.9416, 'Lon': 79.8083},
        'Telangana': {'Lat': 17.1232, 'Lon': 79.2088}
    }

    # Map the coordinates to the DataFrame
    crime_rate['Lat'] = crime_rate['STATE/UT'].map(lambda x: state_coordinates.get(x, {}).get('Lat'))
    crime_rate['Lon'] = crime_rate['STATE/UT'].map(lambda x: state_coordinates.get(x, {}).get('Lon'))

    # Create the map using Plotly
    fig = px.scatter_mapbox(crime_rate, lat="Lat", lon="Lon", hover_name="STATE/UT", hover_data={"Total Crimes": True},
                    color_discrete_sequence=["fuchsia"], zoom=3, height=300)

    # Update the map layout to use OpenStreetMap
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # Display the map in Streamlit
    st.plotly_chart(fig)


# Satate-wise total number of crime upto year 2013 (front display)
def state_crime(data):
    st.title('Crime Distribution State/UT')
    df = data.groupby("STATE/UT")["Total Crimes"].sum().reset_index().sort_values(by="Total Crimes",ascending = False)
    fig_distribution = px.bar(df, x='Total Crimes', y='STATE/UT', title='Total Crimes by State/UT',color='STATE/UT')
    st.plotly_chart(fig_distribution)

# will give district wise crime rate for each state
def district_crime(data):
    st.title('Crime Distribution for District')
    df = data.sum().iloc[3:-3].reset_index()
    df.columns = ['Crime Type', 'Total']
    fig_distribution = px.bar(df, x='Crime Type', y='Total', title='Total Crimes by District',color='Total')
    st.plotly_chart(fig_distribution)

# gives the year,state and district wise distribution of crime
def Crime_year(data):
    st.title('Crime Distribution')
    composition_data = data.sum().iloc[3:-3].reset_index()
    composition_data.columns = ['Crime Type', 'Total']
    fig_composition = px.pie(composition_data, names='Crime Type', values='Total', title=f'Crime distribution for Selected Period')
    st.plotly_chart(fig_composition)




