import pandas as pd
import matplotlib.pyplot as plt

building_name = ['Autograph Tower', 'Keangnam Hanoi Landmark Tower',
                  'Four Seasons KL', 'Baiyoke Tower', 'Luminary Tower', 
                  'Mahanakhon', 'Magnolias Waterfront Residence', 
                  'Federal Land Tower']
height = [383, 329, 343, 304, 301, 314, 315, 318]
floor_count = [75, 72, 77, 85, 64, 77, 70, 66]

df_supertall = pd.DataFrame({
    'Name' : building_name,
    'Height' : height,
    'Floor Count' : floor_count,
})

print(df_supertall.describe(include='all'))
df_supertall.hist()
plt.show()

korelasi = df_supertall[['Height', 'Floor Count']].corr()
print(korelasi)