import pandas as pd

SEASONS = [2021, 2022, 2023]

all_seasons = []

for season in SEASONS:
    print(f"\nProcessing season {season}...")
    
    pbp = pd.read_parquet(f"data/pbp_{season}.parquet")

    qb_dropbacks = pbp[
        (pbp["pass_attempt"] == 1) |
        (pbp["sack"] == 1) |
        (pbp["qb_scramble"] == 1)
    ].copy()

    print(f"QB dropbacks ({season}): {len(qb_dropbacks)}")

    qb_dropbacks["is_clutch"] = (
        (qb_dropbacks["qtr"] == 4) &
        (qb_dropbacks["game_seconds_remaining"] <= 300) &
        (qb_dropbacks["score_differential"].abs() <= 7)
    )
    
    qb_dropbacks["season"] = season
    
    all_seasons.append(qb_dropbacks)
    


df_all = pd.concat(all_seasons, ignore_index = True)

output_path = "data/qb_dropbacks_all_seasons.parquet"
df_all.to_parquet(output_path)

print(f"\nSaved multi-season QB dropbacks to {output_path}")
print(df_all[["season", "is_clutch"]].value_counts())