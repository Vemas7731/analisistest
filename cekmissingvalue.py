import pandas as pd

df_earthquake = pd.read_excel("C:\\Users\\MyBook Hype AMD\\Documents\\dataset\\Earthquake Dataset\\percobaan.xlsx")
print(df_earthquake.tail())

cek_missing = df_earthquake.isnull().sum()
print(cek_missing)

cek_duplikat = df_earthquake.duplicated().sum()
print('Jumlah duplikat : ', cek_duplikat)