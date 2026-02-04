import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Ay": ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"],
    "İhracat": [21.16, 20.73, 23.41, 20.78, 24.82, 20.47, 24.91, 21.70, 22.55, 23.95, 22.51, 26.37],
    "İthalat": [28.67, 28.52, 30.60, 32.89, 31.46, 28.69, 31.38, 25.98, 29.47, 31.51, 30.52, 35.67]
}

df = pd.DataFrame(data)

#Karşılama oranı hesabı = (ihracat / ithalat) * 100
df["Karsilama"] = (df["İhracat"] / df["İthalat"]) * 100

cerceve, (ust_grafik, alt_grafik) = plt.subplots(2, 1, figsize = (12, 10))

ust_grafik.plot(df["Ay"], df["İthalat"], color = "red", linewidth = 3, marker = "o", label = "İthalat (Gider)")
ust_grafik.plot(df["Ay"], df["İhracat"], color = "blue", linewidth = 3, marker = "o", label = "İhracat (Gelir)")

ust_grafik.fill_between(df["Ay"], df["İhracat"], df["İthalat"], color = "red", alpha = 0.1, label = "Dış Ticaret Açığı")

ust_grafik.set_title("2025 Türkiye Dış Ticaret Dengesi: Makas Analizi", fontsize = 14, fontweight = "bold")
ust_grafik.set_ylabel("Milyar Dolar ($)")
ust_grafik.legend()
ust_grafik.grid(True, linestyle = "--", alpha =0.5)

alt_grafik.bar(df["Ay"], df["Karsilama"], color = "blue", alpha = 0.5, label = "Karşılama Oranı")

alt_grafik.axhline(75, color = "red", linestyle = "--", linewidth = 2, label = "Kritik Eşik (%75)")

alt_grafik.set_title("İhracatın İthalatı Karşılama Oranı (%)", fontsize = 13, fontweight = "bold")
alt_grafik.set_ylabel("Oran (%)")
alt_grafik.set_ylim(50, 100)
alt_grafik.legend()
alt_grafik.grid(True, linestyle = "--", alpha = 0.5)

for i, oran in enumerate(df["Karsilama"]):
    alt_grafik.text(i, oran + 1, f"%{oran:.0f}", ha = "center", fontweight = "bold")

plt.tight_layout()
plt.show()

