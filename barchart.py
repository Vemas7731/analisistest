import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

skyscrapers = ('Jakarta','KL','Bangkok','Manila','Singapore','Hanoi')
heights = (125, 167, 115, 116, 99, 35)

df_skyscrapers = pd.DataFrame({
    'Skyscrapers' : skyscrapers,
    'Heights' : heights,
})

#variabel di sumbu x
#plt.bar(x=skyscrapers, height=heights)
#plt.xticks(rotation=45)

#sort
df_skyscrapers.sort_values(by='Heights', inplace=True)

#variabel di sumbu y
#plt.barh(y=df_skyscrapers["Skyscrapers"], width=df_skyscrapers["Heights"])

#visualisasi pake tool seaborn
sns.barplot(y=df_skyscrapers["Skyscrapers"], x=df_skyscrapers["Heights"], orient="h", color='teal')

plt.xlabel("Height (Meters)")
plt.title("Number of Skyscraper on Southeast Asian Cities")


plt.show()