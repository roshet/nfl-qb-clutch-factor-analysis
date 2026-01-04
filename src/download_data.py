import nfl_data_py as nfl
import pandas as pd

SEASONS = [2021, 2022, 2023]  

cols = [
    "game_id",
    "season",
    "week",
    "qtr",
    "game_seconds_remaining",
    "posteam",
    "defteam",
    "passer_player_name",
    "pass_attempt",
    "sack",
    "qb_scramble",
    "complete_pass",
    "yards_gained",
    "touchdown",
    "interception",
    "epa",
    "score_differential"
]

for season in SEASONS:
    print("Downloading play-by-play data for {season}...")
    pbp = nfl.import_pbp_data([season])

    pbp = pbp[cols]

    output_path = f"data/pbp_{season}.parquet"
    pbp.to_parquet(output_path)

    print(f"Saved data to {output_path} | rows = {len(pbp)}")

print("\nAll seasons downloaded successfully.")
