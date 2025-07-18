import os
import csv
import time
from pathlib import Path

DATA_DIR = Path.home() / ".candles/data"
PREDICTION_PATHS = {
    "1": DATA_DIR / "hourly_predictions.csv",
    "2": DATA_DIR / "daily_predictions.csv",
    "3": DATA_DIR / "weekly_predictions.csv"
}

def ensure_data_dir():
    if not DATA_DIR.exists():
        print(f"📁 Creating data directory at {DATA_DIR}")
        DATA_DIR.mkdir(parents=True, exist_ok=True)

def print_menu():
    print("\n🕯️ Candles Miner Prediction Uploader")
    print("1. Add hourly predictions")
    print("2. Add daily predictions")
    print("3. Add weekly predictions")
    print("4. EXIT")

def parse_and_validate(csv_text):
    lines = csv_text.strip().splitlines()
    reader = csv.reader(lines)
    header = next(reader, None)

    if header != ['timestamp', 'color', 'confidence', 'price']:
        print("❌ Invalid header. Must be: timestamp,color,confidence,price")
        return None

    validated_rows = []
    now = int(time.time())

    for i, row in enumerate(reader, start=2):  # line 2 onwards
        if len(row) != 4:
            print(f"❌ Line {i} does not have exactly 4 columns: {row}")
            return None
        try:
            timestamp = int(row[0])
            if timestamp <= now:
                print(f"❌ Line {i} has past timestamp: {timestamp}")
                return None
            color = row[1].lower()
            if color not in ['red', 'green']:
                print(f"❌ Line {i} has invalid color: {color}")
                return None
            confidence = float(row[2])
            if not (0.0 <= confidence <= 1.0):
                print(f"❌ Line {i} has invalid confidence: {confidence}")
                return None
            price = float(row[3])
            validated_rows.append([timestamp, color, confidence, price])
        except Exception as e:
            print(f"❌ Line {i} parsing error: {e}")
            return None

    return validated_rows

def save_predictions(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'color', 'confidence', 'price'])
        writer.writerows(rows)
    print(f"✅ Predictions saved to {path}")

def main():
    ensure_data_dir()
    while True:
        print_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        if choice == "4":
            print("👋 Thank you, come again!")
            break
        elif choice in PREDICTION_PATHS:
            print("\n📋 Paste your predictions below. End input with a blank line: (hit enter 2x)")
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
            csv_text = "\n".join(lines)
            validated = parse_and_validate(csv_text)
            if validated is not None:
                save_predictions(PREDICTION_PATHS[choice], validated)
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
