
import pandas as pd
import matplotlib.pyplot as plt

data = {
             "Ay": ["Oca", "Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl", "Eki","Kas","Ara","Oca'26"],
             "Aylık": [5.03, 2.27, 2.46, 3.00, 1.53, 1.37, 2.06, 2.04, 3.23, 2.55, 0.87, 0.89, 4.84],
             "Yıllık": [42.12, 39.05, 38.10, 37.86, 35.41, 35.05, 33.52, 32.95, 33.29, 32.87, 31.07, 30.89, 30.65]
          }
df = pd.DataFrame(data)

fig, (ust_grafik, alt_grafik) = plt.subplots(2, 1, figsize=(13, 9))
arka_plan = '#f8f9fa'
fig.set_facecolor(arka_plan)


ust_grafik.set_facecolor(arka_plan)
ust_grafik.plot(df["Ay"], df["Aylık"], color = "blue", marker = "o", markersize = 8, linewidth =3)
ust_grafik.set_title("2025-2026 Aylık Enflasyon Değişimi", fontsize = 13, fontweight = "bold", color = "black")
ust_grafik.set_ylabel("Değişim (%)", color = "black")
ust_grafik.grid(axis = "y", linestyle = "--", alpha = 0.7)

for i, deger in enumerate(df["Aylık"]):
    ust_grafik.text(i, deger+ 0.2, f"{deger}", ha = 'center', fontsize = 10, fontweight = 'bold', color = "black")




alt_grafik.set_facecolor(arka_plan)
alt_grafik.plot(df["Ay"], df["Yıllık"], color = "red", marker = "s", markersize = 8, linewidth = 3)
alt_grafik.set_title("2025-2026 Yıllık Enflasyon Trendi", fontsize = 13, fontweight = "bold", color = "black")
alt_grafik.set_ylabel("Değişim (%)", color ="black", fontweight ="bold")
alt_grafik.grid(axis ="y", linestyle ="--", alpha =0.7)

for i, deger in enumerate(df["Yıllık"]):
    alt_grafik.text(i, deger + 0.5, f"{deger}", ha ='center', fontsize =10, fontweight ='bold', color ="black")




plt.tight_layout(pad =3)
plt.show()