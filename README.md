# 🏈 NFL QB Clutch Factor Analyzer

A data-driven analytics project that quantifies quarterback performance under pressure using NFL play-by-play data.
This project introduces a custom Clutch Factor metric to measure how quarterbacks perform in high-leverage situations compared to normal game conditions, with both single-season and multi-season analysis.

---

## 📌 What Is “Clutch”?

A play is labeled as clutch if ALL of the following conditions are met:

- 4th quarter
- 5 minutes or less remaining
- Score differential within ±7 points
- The play is a QB dropback (pass attempt, sack, or QB scramble)

This definition focuses on moments where quarterback decision-making and execution have the highest impact on game outcomes.

---

## 📊 Clutch Factor Metric

Clutch Factor is defined as:

Clutch Factor = (Clutch EPA per play) − (Normal EPA per play)

Where:
- EPA (Expected Points Added) measures play efficiency
- A positive value indicates better performance under pressure
- A negative value indicates a decline in clutch situations

---

## 🔍 Project Pipeline

1. Download Data  
   - NFL play-by-play data from 2021–2023  
   - Stored efficiently using Parquet format  

2. Label Clutch Plays  
   - Filters to quarterback dropbacks  
   - Applies clutch conditions to each play  

3. Compute Clutch Factor  
   - Aggregates per quarterback and season  
   - Applies minimum sample-size thresholds  

4. Multi-Season Analysis  
   - Measures clutch consistency across seasons  
   - Distinguishes sustained performance from one-season spikes  

5. Visualization  
   - Top clutch quarterbacks (bar chart)  
   - Normal vs clutch EPA (scatter plot)  
   - Multi-season clutch trend analysis  

---

## 📈 Visualizations

Top 10 Clutch QBs (2023)  
screenshots/top10_clutch_qbs_2023.png

Normal vs Clutch EPA (2023)  
screenshots/normal_vs_clutch_epa_2023.png

Multi-Season Clutch Trends  
screenshots/clutch_factor_trends.png

---

## 🛠️ Tech Stack

- Python
- pandas
- nfl_data_py
- matplotlib
- Parquet (pyarrow / fastparquet)

---

## 🚀 How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run the pipeline:

python src/download_data.py  
python src/label_clutch_plays.py  
python src/compute_clutch_factor.py  
python src/analyze_clutch_trends.py  
python src/visualize_clutch_factor.py  

---

## 🎯 Key Takeaways

- Clutch performance varies significantly across quarterbacks
- Some QBs show consistent clutch efficiency across multiple seasons
- Others perform well in normal situations but decline under pressure
- Multi-season analysis helps separate noise from true performance trends

---

## 📂 Notes

- Raw play-by-play data is generated locally and excluded from version control
- All results are fully reproducible by running the pipeline
