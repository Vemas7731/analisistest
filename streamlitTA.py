import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('output_buatdashboard.csv', parse_dates=['date'])
    return df

# Load data
df_allstation = load_data()

# Streamlit dashboard title
st.title('Analisis Kualitas Udara di Semua Stasiun')

# Sidebar for date filtering
with st.sidebar:
    st.header('Pilih Rentang Tanggal')
    start_date = st.date_input("Start Date", value=pd.to_datetime('2013-03-01').date())
    end_date = st.date_input("End Date", value=pd.to_datetime('2017-03-01').date())

# Filter data based on selected dates
filtered_data = df_allstation[(df_allstation['date'] >= pd.to_datetime(start_date)) & (df_allstation['date'] <= pd.to_datetime(end_date))]

# Visualization: Trend of PM2.5 concentration
st.subheader('Kapan Biasanya Terjadi Lonjakan Polusi Udara (PM 2.5)')
df_lonjakanpolusi = filtered_data.groupby('date')[['PM2.5']].mean().reset_index()

# Create the PM2.5 trend plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='PM2.5', data=df_lonjakanpolusi, marker='o', color='blue', label='PM2.5')
plt.title('Tingkat Polusi Udara Tahunan (2013-2017)', fontsize=14)
plt.xlabel('Tanggal', fontsize=12)
plt.ylabel('Konsentrasi PM2.5', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Display the PM2.5 trend plot in Streamlit
st.pyplot(plt)


# Heatmap of correlation between Wind Speed, Rainfall, and PM2.5
st.subheader('Apakah Kecepatan Angin dan Hujan Mempengaruhi Konsentrasi PM 2.5 di Udara')
correlation_matrix = df_allstation[['WSPM', 'RAIN', 'PM2.5']].corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True, linewidths=0.5, cbar_kws={"shrink": .8})
plt.title('Heatmap Korelasi Kecepatan Angin, Hujan, dan PM2.5', fontsize=14)
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()

# Display the heatmap in Streamlit
st.pyplot(plt)
st.write('Keterangan : ')
st.write(' 1 = korelasi linear (Hujan atau angin membuat konsentrasi PM 2.5 meningkat) ')
st.write('-1 = korelasi berlawanan (Hujan atau angin membuat konsentrasi PM 2.5 menurun) ')
st.write(' 0 = tanpa korelasi (Hujan atau angin tidak memiliki korelasi sama sekali terhadap jumlah konsentrasi PM 2.5 di udara) ')
st.write('')

# Mengambil fitur yang relevan untuk korelasi gas
df_korelasi_gas = df_allstation[['PM2.5', 'SO2', 'NO2', 'CO', 'O3']]

# Menghitung korelasi
korelasi_gas = df_korelasi_gas.corr()

# Visualisasi heatmap korelasi
st.subheader('Apakah Gas Seperti SO2, NO2, CO, O3 Selalu Muncul Saat Konsentrasi PM 2.5 Meningkat')
plt.figure(figsize=(8, 6))
sns.heatmap(korelasi_gas, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap Korelasi PM2.5 dengan Gas (SO2, NO2, CO, O3)', fontsize=14)
plt.tight_layout()

# Display the heatmap in Streamlit
st.pyplot(plt)

# Geospatial visualization with Folium
st.subheader('Peta Stasiun Kualitas Udara Berdasarkan Rata-rata PM2.5')

# Koordinat stasiun
stations = {
    "aotizhongxin": [39.9758, 116.4821],
    "changping": [40.2186, 116.1945],
    "dingling": [40.2410, 116.2202],
    "dongsi": [39.9293, 116.4179],
    "guanyuan": [39.9296, 116.3472],
    "gucheng": [39.9149, 116.1822],
    "huairou": [40.3636, 116.6382],
    "nongzhanguan": [39.9351, 116.4613],
    "shunyi": [40.1289, 116.6546],
    "tiantan": [39.8820, 116.4109],
    "wanliu": [39.9936, 116.3039],
    "wanshouxigong": [39.8783, 116.3397]
}

if len(filtered_data) == 0:
    st.write("No data available for the selected date range.")
else:

    # Calculate mean PM2.5 for each station
    station_mean_pm25 = filtered_data.groupby('station')['PM2.5'].mean()

    # Replace NaN values or missing data with a message 'No Data' for easier handling
    station_mean_pm25 = station_mean_pm25.fillna('No Data')


# Clean the station names in filtered_data to ensure they match the dictionary
filtered_data['station'] = filtered_data['station'].str.lower().str.strip()

# Recalculate mean PM2.5 for each station with cleaned names
station_mean_pm25 = filtered_data.groupby('station')['PM2.5'].mean()

# Debugging: Output the recalculated means
st.write(station_mean_pm25)

# Debugging: Check if stations in the dictionary match with the data
matched_stations = [station for station in stations if station in station_mean_pm25.index]
unmatched_stations = [station for station in stations if station not in station_mean_pm25.index]

# Proceed with folium map if stations match
if len(matched_stations) > 0:
    m = folium.Map(location=[39.9042, 116.4074], zoom_start=10)

    for station, coord in stations.items():
        if station in station_mean_pm25.index:
            mean_pm25 = station_mean_pm25[station]
            
            # Determine color based on PM2.5 value
            color = 'green' if mean_pm25 < 100 else 'red'
            mean_pm25_display = f'{mean_pm25:.2f}'
        else:
            mean_pm25_display = 'No Data'
            color = 'gray'

        # Add a marker for each station
        folium.Marker(
            location=coord,
            popup=f'Station: {station}<br>Mean PM2.5: {mean_pm25_display}',
            icon=folium.Icon(color=color)
        ).add_to(m)

    # Display the map in Streamlit
    folium_static(m)
else:
    st.write("No stations matched.")
