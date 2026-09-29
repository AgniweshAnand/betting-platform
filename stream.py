import csv
import time

TARGET_CSV = "custom_bets.csv"

total_bets = 0

with open(TARGET_CSV, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_bets += 1
        user = row.get("user_id", "Unknown")
        match = f"{row.get('Home_Team', 'Team 1')} vs {row.get('Away_Team', 'Team 2')}"
        bid = row.get("bid_amount", "0")
        
        print(f"Bet #{total_bets:02d} | User: {user} | Match: {match} | Bid: ${bid}")
        time.sleep(1)

print(f"\nDone! Streamed {total_bets} bets from {TARGET_CSV}.")