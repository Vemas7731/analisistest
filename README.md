# Analisis Data Kualitas Udara Stasiun Beijing 

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir Git_repo_Test
cd Git_repo_Test
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run streamlitTA.py

```

## 👤 Author
- **Name**: Vemas Adi Pratama  
- **Email**: m254b4ky4405@bangkit.academy  
- **Dicoding ID**: vemasap  

---

## 📌 Project Overview
Proyek ini bertujuan untuk menganalisis kualitas udara di Beijing dengan fokus pada konsentrasi **PM2.5** serta faktor-faktor yang mempengaruhinya, seperti kecepatan angin, curah hujan, dan gas berbahaya (SO2, NO2, CO, O3).

Dataset yang digunakan merupakan gabungan dari beberapa stasiun pemantauan kualitas udara di Beijing.

---

## ❓ Business Questions
1. Kapan biasanya terjadi lonjakan polusi udara (PM2.5)?
2. Apakah kecepatan angin dan curah hujan berpengaruh terhadap PM2.5?
3. Apakah gas seperti SO2, NO2, CO, dan O3 meningkat saat PM2.5 tinggi?

---

## 🛠️ Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📂 Data Processing

### 🔹 Data Gathering
- Menggabungkan 12 dataset dari berbagai stasiun
- Memilih fitur relevan:
  - PM2.5, WSPM (angin), RAIN (hujan)
  - SO2, NO2, CO, O3
  - tanggal & lokasi

### 🔹 Data Wrangling
- Menggabungkan dataset menjadi satu dataframe
- Mengubah fitur `year`, `month`, `day` → `date`
- Total data awal: **420,768 rows**

---

## 🔍 Data Assessment

Ditemukan beberapa masalah:
- Missing values: **64,562**
- Duplicate data: **893**
- Outlier (PM2.5): **19,142**

---

## 🧹 Data Cleaning

Langkah yang dilakukan:
- Missing values → **interpolation (time series)**
- Duplicate → dihapus
- Outlier → dihapus menggunakan metode **IQR**

Hasil:
- Missing values: 0
- Duplicate: 0
- Data yang dihapus (outlier): ± **140,000 (~33%)**

---

## 📈 Exploratory Data Analysis (EDA)

### 🔹 Statistik PM2.5
- Mean: ~70
- Max: ~247
- Distribusi menunjukkan variasi polusi yang signifikan

### 🔹 Korelasi

| Faktor | Korelasi dengan PM2.5 |
|--------|------------------------|
| Angin (WSPM) | -0.117 (sangat lemah) |
| Hujan (RAIN) | -0.016 (tidak signifikan) |
| SO2 | 0.411 (cukup kuat) |
| NO2 | 0.508 (cukup kuat) |
| CO | 0.652 (kuat) |
| O3 | -0.048 (tidak signifikan) |

---

## 📊 Key Insights

### 📅 Pola Polusi
- PM2.5 tinggi di **awal & akhir tahun (Nov–Mar)**
- Lebih rendah di **pertengahan tahun (Agustus–September)**

### 🌬️ Angin & Hujan
- Tidak memiliki pengaruh signifikan terhadap penurunan polusi
- Korelasi mendekati 0

### ☣️ Gas Berbahaya
- **SO2, NO2, CO** meningkat saat PM2.5 tinggi
- **CO memiliki korelasi paling kuat**
- **O3 tidak berkorelasi signifikan**

---

## 📊 Visualization
Analisis divisualisasikan menggunakan:
- Line chart (tren tahunan)
- Bar chart (rata-rata bulanan)
- Heatmap (korelasi)

---

## 🌐 Interactive Dashboard
Dashboard interaktif tersedia di:
👉 https://airqualitystation.streamlit.app/

---

## 🧠 Conclusion

### 1. Lonjakan Polusi
Polusi udara tertinggi terjadi di awal dan akhir tahun.  
👉 Perlu tindakan preventif sebelum periode tersebut.

### 2. Pengaruh Angin & Hujan
Tidak signifikan dalam menurunkan PM2.5.  
👉 Solusi harus fokus ke sumber polusi, bukan faktor alam.

### 3. Gas Berbahaya
SO2, NO2, dan CO meningkat saat polusi tinggi.  
👉 Berpotensi menjadi indikator utama kualitas udara buruk.

---

## 🚀 Recommendation
- Pembatasan emisi kendaraan
- Transisi ke energi bersih
- Monitoring gas berbahaya secara real-time
- Edukasi penggunaan masker saat polusi tinggi

---

## ⚠️ Notes
- Dataset merupakan time series → interpolation digunakan untuk menjaga kontinuitas data
- Outlier dihapus untuk meningkatkan kualitas analisis

---

## 📎 Project Structure
