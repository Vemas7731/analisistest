import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca dua dataset
df_wanliu = pd.read_csv('PRSA_Data_Wanliu_20130301-20170228.csv')
df_gucheng = pd.read_csv('PRSA_Data_Gucheng_20130301-20170228.csv')

# Mengambil kolom yang diperlukan
df_wanliu = df_wanliu[['year', 'month', 'day', 'PM2.5']]
df_gucheng = df_gucheng[['year', 'month', 'day', 'PM2.5']]

# Menggabungkan kedua dataset
df_combined = pd.concat([df_wanliu, df_gucheng])

# Menggabungkan kolom year, month, dan day menjadi satu kolom tanggal
df_combined['date'] = pd.to_datetime(df_combined[['year', 'month', 'day']])

# Mengelompokkan data untuk menghitung rata-rata PM2.5 per bulan
df_monthly_avg = df_combined.groupby(df_combined['date'].dt.to_period('M')).agg({'PM2.5': 'mean'}).reset_index()

# Mengonversi periode kembali ke datetime untuk plotting
df_monthly_avg['date'] = df_monthly_avg['date'].dt.to_timestamp()

# Visualisasi dengan Matplotlib
plt.figure(figsize=(12, 6))
plt.plot(df_monthly_avg['date'], df_monthly_avg['PM2.5'], marker='o')
plt.title('Rata-rata Bulanan PM2.5 di Beijing (2013-2018)')
plt.xlabel('Tanggal')
plt.ylabel('Rata-rata PM2.5')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

# Menampilkan plot di Streamlit
st.title("Visualisasi Rata-rata PM2.5 Bulanan di Beijing")
st.pyplot(plt)
