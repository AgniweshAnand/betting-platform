import csv
import random

TARGET_CSV = "custom_bets.csv"

def get_random_bid(min_val=10.5, max_val=500.5):
    return round(random.uniform(min_val, max_val), 1)

headers = [
    "s.no", "user_id", "Match_ID", "Date", "Sport", "Home_Team", "Away_Team",
    "Home_Team_Odds", "Away_Team_Odds", "Draw_Odds",
    "Predicted_Winner", "Actual_Winner", "bid_amount"
]

base_match = {
    "Match_ID": "M00018",
    "Date": "2024-03-23",
    "Sport": "Football",
    "Home_Team": "Lake Corey Bears",
    "Away_Team": "Lorettaland Wolves",
    "Home_Team_Odds": "1.4",
    "Away_Team_Odds": "2.25",
    "Draw_Odds": "4.28",
    "Predicted_Winner": "Lake Corey Bears",
    "Actual_Winner": "Draw"
}

with open(TARGET_CSV, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    for i in range(1, 21):
        row = base_match.copy()
        row["s.no"] = i
        row["user_id"] = f"u{i}"
        row["bid_amount"] = get_random_bid()
        writer.writerow(row)

print(f"Successfully generated 20 rows with user_id in {TARGET_CSV}")