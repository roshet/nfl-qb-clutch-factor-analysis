import pandas as pd
import matplotlib.pyplot as plt

SEASON = 2023

print("Loading QB clutch factors...")
qb = pd.read_parquet(f"data/qb_clutch_factors_{SEASON}.parquet")

qb = qb.drop(columns=["is_clutch_x", "is_clutch_y"], errors="ignore")

top10 = qb.head(10)

plt.figure()
plt.barh(top10["passer_player_name"], top10["clutch_factor"])
plt.xlabel("Clutch Factor (Clutch EPA − Normal EPA)")
plt.title("Top 10 Clutch QBs (2023)")
plt.gca().invert_yaxis() 
plt.tight_layout()
plt.savefig("screenshots/top10_clutch_qbs_2023.png")
plt.close()

print("Saved top-10 clutch QB chart")

plt.figure()
plt.scatter(qb["normal_epa"], qb["clutch_epa"])
plt.axline((0, 0), slope=1)  

annotate_qbs = pd.concat([
    qb.nlargest(1, "clutch_factor"),
    qb.nsmallest(1, "clutch_factor")
])

for _, row in annotate_qbs.iterrows():
    plt.annotate(
        row["passer_player_name"],
        (row["normal_epa"], row["clutch_epa"]),
        textcoords = "offset points",
        xytext = (5, 5),
        fontsize = 9
    )
    
plt.xlabel("Normal EPA per Play")
plt.ylabel("Clutch EPA per Play")
plt.title("QB Performance: Normal vs Clutch (2023)")
plt.tight_layout()
plt.savefig("screenshots/normal_vs_clutch_epa_2023.png")
plt.close()

print("Saved normal vs clutch EPA scatter plot")
