import pandas as pd

MIN_CLUTCH_PLAYS = 30 

print("Loading multi-season QB dropback data...")
df = pd.read_parquet(f"data/qb_dropbacks_all_seasons.parquet")

df = df.dropna(subset=["passer_player_name"])

df["completion"] = df["complete_pass"].fillna(0)

df["td"] = df["touchdown"].fillna(0)
df["int"] = df["interception"].fillna(0)

grouped = (
    df
    .groupby(["season", "passer_player_name", "is_clutch"])
    .agg(
        plays=("epa", "count"),
        epa_per_play=("epa", "mean"),
        completion_pct=("completion", "mean"),
        td_rate=("td", "mean"),
        int_rate=("int", "mean")
    )
    .reset_index()
)

clutch = grouped[grouped["is_clutch"] == True]
normal = grouped[grouped["is_clutch"] == False]

clutch = clutch.rename(columns={
    "plays": "clutch_plays",
    "epa_per_play": "clutch_epa",
    "completion_pct": "clutch_comp_pct",
    "td_rate": "clutch_td_rate",
    "int_rate": "clutch_int_rate"
})

normal = normal.rename(columns={
    "plays": "normal_plays",
    "epa_per_play": "normal_epa",
    "completion_pct": "normal_comp_pct",
    "td_rate": "normal_td_rate",
    "int_rate": "normal_int_rate"
})

qb_stats = pd.merge(
    clutch,
    normal,
    on=["season", "passer_player_name"],
    how="inner"
)

qb_stats["clutch_factor"] = qb_stats["clutch_epa"] - qb_stats["normal_epa"]

qb_stats = qb_stats[qb_stats["clutch_plays"] >= MIN_CLUTCH_PLAYS]

qb_stats = qb_stats.sort_values(["season", "clutch_factor"], ascending=[True, False])

output_path = f"data/qb_clutch_factors_all_seasons.parquet"
qb_stats.to_parquet(output_path)

print(f"Saved multi-season QB clutch factors to {output_path}")
print(qb_stats.head(10))
