import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

data_gedung = np.array([266,276,288,286,262,383,262,280,301,331])
rata = data_gedung.mean()
tengah = np.median(data_gedung)
modus = stats.mode(data_gedung)[0]
jarak = data_gedung.max() - data_gedung.min()
jarak_interkuartil = np.percentile(data_gedung, 75) - np.percentile(data_gedung, 25)
data_gedung_series = pd.Series(data_gedung)
varians = data_gedung_series.var()
standar_deviasi = data_gedung_series.std()
skewness = data_gedung_series.skew()


print('Rata-rata ketinggian : ', rata)
print('Nilai tengah ketinggian : ', tengah)
print('Modus ketinggian : ', modus)
print('Jarak ketinggian : ', jarak)
print('Jarak interkuartil ketinggian : ', jarak_interkuartil)
print('Varians ketinggian : ', varians)
print('Standar deviasi ketinggian : ', standar_deviasi)
print('Skewness ketinggiian : ', skewness)


plt.hist(data_gedung, bins=10)
plt.show()


#cek outlier dengan iqr
q1, q3 = np.percentile(data_gedung, 25), np.percentile(data_gedung, 75)
cut_off = jarak_interkuartil * 1.5
minimum, maximum = q1 - cut_off, q3 + cut_off

outliers = [x for x in data_gedung if x < minimum or x > maximum]

print(outliers)

#anjay