# Candles Miner Prediction Uploader

A simple CLI tool for Candles miners to paste in prediction CSVs generated from [candlestao.com](https://candlestao.com) and save them to the correct location for hourly, daily, or weekly submissions.

- 📁 Automatically creates the `.candles/data/` directory  
- 🔍 Validates prediction format  
- 🟢 Supports hourly, daily, and weekly uploads  
- 🔁 Lets you continue uploading in a loop

---

## 🚀 Quick Start

### 1. Clone the Repo

```
git clone https://github.com/TidalWavesNode/Candles_Miner_Prediction_Uploader.git
cd Candles_Miner_Prediction_Uploader
```

2. Run the Script
```
python3 candles_prediction_uploader.py
```

📋 How to Use

Choose a prediction type from the menu:

<img width="297" height="115" alt="image" src="https://github.com/user-attachments/assets/536d577b-e10b-48a1-994b-a9e9dab655aa" />

Paste your CSV (including the header), then hit *Enter twice* to submit.

<img width="509" height="78" alt="image" src="https://github.com/user-attachments/assets/c3b870b7-2d1f-4cfe-ab20-ef789bdef060" />

If your predictions are valid, they'll be saved, and you'll return to the main menu.


🧾 CSV Format Requirements:

timestamp,color,confidence,price

1704067200,red,0.85,45.50

1704070800,green,0.92,46.20

1704074400,red,0.78,44.90

🔍 Column Rules

timestamp: Unix timestamp for the start of the prediction interval (must be in the future)
- color: red or green
- confidence: Float between 0.0 and 1.0
- price: Decimal (e.g., 45.50)

📂 File Save Locations

Predictions are	saved To

- Hourly	~/.candles/data/hourly_predictions.csv
- Daily	~/.candles/data/daily_predictions.csv
- Weekly	~/.candles/data/weekly_predictions.csv

❓ Troubleshooting

Double Enter Required: After pasting, press Enter twice to submit.

Validation Errors? Make sure:

Your timestamps are in the future

Colors are only red or green

Confidence is between 0.0 and 1.0

The file includes the header row

Join the [Candles Community Discord](https://discord.gg/XZfAzkmy)and make your predictions count 🕯

