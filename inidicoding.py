import numpy as np
from scipy import stats
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
mode_jumlah_kucing = stats.mode(jumlah_kucing)
 
print(mode_jumlah_kucing)
