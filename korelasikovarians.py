import pandas as pd

data_gedung = {
    'gedung' : ['Autograph', 'Luminary', 'Treasury', 'BNI', 'Astra'],
    'ketinggian' : [383, 301, 280, 262, 261],
    'lantai' : [75, 64, 57, 47, 46],
    'lama' : [10, 9, 3, 3, 4]
}

df = pd.DataFrame(data_gedung)

korelasi = df.corr(numeric_only=True)
kovarian = df.cov(numeric_only=True)

print(korelasi)
print(kovarian)