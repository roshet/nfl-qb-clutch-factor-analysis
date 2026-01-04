import pandas as pd
import matplotlib.pyplot as plt

print("Loading multi-season clutch factors...")
df = pd.read_parquet("data/qb_clutch_factors_all_seasons.parquet")

qb_consistency = (
    df
    .groupby("passer_player_name")
    .agg(
        seasons_played = ("season", "nunique"),
        avg_clutch_factor = ("clutch_factor", "mean"),
        clutch_std = ("clutch_factor", "std")
    )
    .reset_index()
)

qb_consistency = qb_consistency[qb_consistency["seasons_played"] >= 2]

qb_consistency = qb_consistency.sort_values(
    "avg_clutch_factor",
    ascending = False
)

qb_consistency.to_parquet("data/qb_clutch_consistency.parquet")

print("Saved QB clutch consistency table")
print(qb_consistency.head(10))

TOP_QBS = qb_consistency.head(5)["passer_player_name"]

plt.figure()

for qb in TOP_QBS:
    qb_data = df[df["passer_player_name"] == qb]
    plt.plot(
        qb_data["season"],
        qb_data["clutch_factor"],
        marker = "o",
        label = qb
    )

plt.axhline(0, linestyle = "--")
plt.xlabel("Season")
plt.ylabel("Clutch Factor")
plt.title("QB Clutch Factor Trends Over Time")
plt.legend()
plt.tight_layout()
plt.savefig("screenshots/clutch_factor_trends.png")
plt.close()

print("Saved clutch factor trend plot")