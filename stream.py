import csv
import random
import time

TARGET_CSV = "custom_bets.csv"
FILTERED_CSV = "filtered.csv"

streamed_rows = []
total_bets = 0


def calculate_payout(user_pick, actual_winner, bid_amount, home_team, home_odds, away_odds):
    """Calculates settlement status, total payout, and net profit."""
    is_win = (user_pick.strip().lower() == actual_winner.strip().lower())
    odds = float(home_odds) if user_pick.strip().lower() == home_team.strip().lower() else float(away_odds)

    if is_win:
        payout = round(bid_amount * odds, 2)
        profit = round(payout - bid_amount, 2)
        status = "WON"
    else:
        payout = 0.0
        profit = round(-bid_amount, 2)
        status = "LOST"

    return status, payout, profit


# 1. Stream bets line by line from custom_bets.csv
with open(TARGET_CSV, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames or []

    for row in reader:
        total_bets += 1
        streamed_rows.append(row)

        user = row.get("user_id", "Unknown")
        home = row.get("Home_Team", "Team 1")
        away = row.get("Away_Team", "Team 2")
        bid = row.get("bid_amount", "0")

        print(f"Bet #{total_bets:02d} | User: {user} | Match: {home} vs {away} | Bid: ${bid}")
        time.sleep(1)

print(f"\nStream finished! Total bets received: {total_bets}")
print(f"Calculating settlements and writing to {FILTERED_CSV}...")

# 2. Process settlements after the stream completes
filtered_fieldnames = list(fieldnames)
for col in ["User_Pick", "Result", "payout_amount", "net_profit"]:
    if col not in filtered_fieldnames:
        filtered_fieldnames.append(col)

with open(FILTERED_CSV, mode="w", newline="", encoding="utf-8") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=filtered_fieldnames)
    writer.writeheader()

    for row in streamed_rows:
        home_team = row.get("Home_Team", "")
        away_team = row.get("Away_Team", "")
        actual_winner = row.get("Actual_Winner", "")
        home_odds = row.get("Home_Team_Odds", "1.0")
        away_odds = row.get("Away_Team_Odds", "1.0")
        bid = float(row.get("bid_amount", 0.0))

        # Assign user pick if not present in raw file
        user_pick = row.get("User_Pick") or random.choice([home_team, away_team])

        status, payout, profit = calculate_payout(
            user_pick, actual_winner, bid, home_team, home_odds, away_odds
        )

        row["User_Pick"] = user_pick
        row["Result"] = status
        row["payout_amount"] = payout
        row["net_profit"] = profit

        writer.writerow(row)

print(f"Successfully processed and saved {len(streamed_rows)} bets to {FILTERED_CSV}.")