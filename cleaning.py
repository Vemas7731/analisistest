import pandas as pd

df_earthquake = pd.read_excel("C:\\Users\\MyBook Hype AMD\\Documents\\dataset\\Earthquake Dataset\\percobaan.xlsx")

#drop value (hapus comment dibawah jika ingin digunakan)
#df_earthquake.dropna(axis=0, inplace=True)

#fill value (hapus comment dibawah jika ingin digunakan)
#df_earthquake['nilai1'].fillna(value=df_earthquake['nilai1'].mean(), inplace=True)

#interpolation value (hapus comment dibawah jika ingin digunakan)
df_earthquake.interpolate(method='linear', limit_direction='forward', inplace=True)

print(df_earthquake.tail())

cek_missing = df_earthquake.isnull().sum()
print(cek_missing)

cek_duplikat = df_earthquake.duplicated().sum()
print('Jumlah duplikat : ', cek_duplikat)

#hilangin outlier 
q1 = (df_earthquake['nilai1'].quantile(0.25))
q3 = (df_earthquake['nilai1'].quantile(0.75))
iqr = q3-q1

maximum = q3 + (1.5*iqr)
minimum = q1 - (1.5*iqr)

kondisi_lower_than = df_earthquake['nilai1'] < minimum
kondisi_more_than = df_earthquake['nilai1'] > maximum

#pake drop
df_earthquake.drop(df_earthquake[kondisi_lower_than | kondisi_more_than].index, inplace=True)
print(df_earthquake.tail())

#pake imputation
#mean_value = df_earthquake['nilai1'].mean()
#df_earthquake['nilai1'] = df_earthquake['nilai1'].mask(kondisi_lower_than | kondisi_more_than, mean_value)
#print(df_earthquake.tail())


#hilangin duplikat
df_earthquake.drop_duplicates(inplace=True)
print(df_earthquake.tail(10))

#nice, alhamdulillah