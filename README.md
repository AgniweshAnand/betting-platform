# Live Terminal Sports Betting Engine

A real-time, terminal-based sports betting simulator written in Python. The system ingests match data, streams incoming simulated bets from a CSV ledger at a fixed interval, and allows a user to place manual bets concurrently through an interactive command-line interface without disrupting the live display.

---

## Features

- **Match Filtering & Ingestion**: Reads from `sports_betting_predictive_analysis.csv`, filtering specifically for non-draw Football matches with valid odds.
- **Mock Ledger Generation**: Generates structured test records in `custom_bets.csv` with randomized bid amounts and sequential user identifiers (`u1`, `u2`, ...).
- **Multi-Threaded Architecture**:
  - **Streamer Thread**: Iterates through existing bets at set intervals to simulate live incoming market volume.
  - **Countdown Timer Thread**: Ticks down a fixed 60-second live betting window.
  - **Main Thread**: Runs an interactive input listener alongside an in-place status bar.
- **Scroll-Free Terminal HUD**: Uses carriage return (`\r`) status updates so streaming bets and clock ticks do not disrupt user typing.
- **Live Bet Logging**: Appends user-placed bets immediately into `custom_bets.csv` with thread-safe synchronization (`threading.Lock`).

---

## Project Structure

```text
.
├── sports_betting_predictive_analysis.csv   # Source dataset containing historical/scheduled matches
├── custom_bets.csv                          # Target ledger storing streamed and manual bets
├── generate_bets.py                         # Utility script to filter matches and generate initial mock bets
├── stream_engine.py                         # Main interactive terminal engine
└── README.md