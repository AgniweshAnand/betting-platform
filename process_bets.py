import csv
import random

SOURCE_CSV = "sports_betting_predictive_analysis.csv"
TARGET_CSV = "custom_bets.csv"
ROW_COUNT = 20


def get_random_bid(min_val=10.5, max_val=500.5):
    return round(random.uniform(min_val, max_val), 1)


headers = [
    "s.no", "user_id", "Match_ID", "Date", "Sport", "Home_Team", "Away_Team",
    "Home_Team_Odds", "Away_Team_Odds", "Draw_Odds",
    "Predicted_Winner", "Actual_Winner", "bid_amount"
]

selected_match = None

with open(SOURCE_CSV, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sport = row.get("Sport", "").strip().lower()
        actual_winner = row.get("Actual_Winner", "").strip().lower()
        pred_winner = row.get("Predicted_Winner", "").strip().lower()
        home_odds = row.get("Home_Team_Odds", "").strip()
        away_odds = row.get("Away_Team_Odds", "").strip()

        # Check conditions
        if sport == "football" and actual_winner != "draw" and pred_winner != "draw":
            if home_odds and away_odds:
                selected_match = row
                break

if not selected_match:
    print("No matching football row found without a draw.")
    exit()

print(f"Selected Match: {selected_match.get('Match_ID')} | "
      f"{selected_match.get('Home_Team')} vs {selected_match.get('Away_Team')} | "
      f"Winner: {selected_match.get('Actual_Winner')}")

with open(TARGET_CSV, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    for i in range(1, ROW_COUNT + 1):
        row = {col: selected_match.get(col, "") for col in headers if col not in ("s.no", "user_id", "bid_amount")}
        row["s.no"] = i
        row["user_id"] = f"u{i}"
        row["bid_amount"] = get_random_bid()
        writer.writerow(row)

print(f"Successfully generated {ROW_COUNT} rows in {TARGET_CSV}")