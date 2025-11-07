# Qasimkhan

**Simple calculator & rent calculator — a beginner Python project**

Hello! I'm Qasim from Pakistan. This repository contains a small collection of beginner Python scripts I built while learning the language. The main purpose is educational: to practice writing Python, structure small programs, and share them so others can run and give feedback.

---

## Contents

* `calculator.py` — a simple calculator script (basic arithmetic operations).
* `rent calculator.py` — a rent calculator (calculate rent shares or totals; small CLI utility).
* `Telegram group ban.py` — a small script related to Telegram group moderation (contains code snippets for banning; likely uses `python-telegram-bot`).
* `.gitignore` — ignored files.

> Note: Filenames may contain spaces (e.g. `rent calculator.py`). For easier use, consider renaming to `rent_calculator.py`.

---

## Features

* Minimal, easy-to-read Python scripts suitable for beginners.
* Demonstrates basic input/output, arithmetic, and conditional logic.
* Example of interacting with Telegram bot APIs (if `Telegram group ban.py` is configured).

---

## Requirements

* Python 3.8+ (2.x is not supported)
* If you want to run Telegram-related code, install `python-telegram-bot` or the library used in the script:

```bash
pip install python-telegram-bot
```

---

## Installation / Run locally

1. Clone the repository:

```bash
git clone https://github.com/Qasimjiho/Qasimkhan.git
cd Qasimkhan
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows
```

3. Run the scripts:

```bash
# Run the simple calculator
python "calculator.py"

# Run the rent calculator
python "rent calculator.py"

# If using the Telegram script, follow comments inside to add your bot token
python "Telegram group ban.py"
```

---

## Suggestions & Improvements (quick wins you can make now)

* Rename files to remove spaces (e.g. `rent_calculator.py`).
* Add `README.md` (this file) and a proper `LICENSE` (MIT is recommended for small projects).
* Add a `requirements.txt` listing dependencies (for example `python-telegram-bot` if used).
* Add example inputs and expected outputs for `calculator.py` and `rent_calculator.py` so new users can test quickly.
* Add comments and docstrings to functions to explain behaviour.
* If `Telegram group ban.py` uses a token, make sure to never commit secrets — use environment variables instead.

---

## How you can help / Feedback

Any feedback is welcome — whether it’s code style, better algorithms, or packaging the project. If you'd like, I can help:

* Convert scripts into a single CLI tool (using `argparse` or `click`).
* Add tests (pytest) and a simple CI workflow (GitHub Actions).
* Clean up and refactor the Telegram script to a safe example that uses environment variables for tokens.

---

## License

This repository does not currently include a license file. If you want to make it open source, consider adding an MIT license.

---

*Made with ❤️ by Qasim*
