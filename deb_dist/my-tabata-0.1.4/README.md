
# Tabata Desktop App
![Science-Backed](https://img.shields.io/badge/Science-Backed-green?style=for-the-badge&logo=google-scholar)
![License: CC0](https://img.shields.io/badge/License-CC0-lightgrey?style=for-the-badge)
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)

## 🎯 Overview
**Tabata Desktop App** is a high-precision, configurable timing tool designed for athletes and practitioners of the Tabata protocol. Developed in Python 3.11, this application provides a minimalist yet robust interface to manage High-Intensity Interval Training (HIIT) sessions directly from your desktop.

* **Author:** Marco Baturan
* **Version:** v0.1.4
* **Status:** Stable / Production Ready
* **License:** Creative Commons Zero (CC0)

## 🖼️ Visuals
![Application Interface](https://raw.githubusercontent.com/marcobaturan/tabata_app/refs/heads/master/assets/pictures/Tabata_application_2026-04-22_01-41-23.jpg)

## 🔬 Scientific Foundation
The Tabata protocol is a specialized form of HIIT characterized by **20 seconds of ultra-high-intensity exercise** followed by **10 seconds of rest**, repeated for a specific number of cycles (typically 8). 

This application is engineered to respect these precise physiological requirements, ensuring accurate timing to maximize both aerobic and anaerobic capacity improvements as established in sports science literature.

### Key Evidence & References
* **[Original Study (1996)]**: [Effects of moderate-intensity endurance and high-intensity intermittent training on anaerobic capacity and VO2max](https://pubmed.ncbi.nlm.nih.gov/8897392/) - The foundational research by Dr. Izumi Tabata.
* **[HIIT & Metabolism]**: [High-Intensity Intermittent Training and Fat Loss](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2991639/) - Comprehensive review on metabolic impact.
* **[Professional Analysis]**: [American Council on Exercise (ACE)](https://www.acefitness.org/certifiednewsarticle/3323/is-tabata-all-it-s-cracked-up-to-be/) - Clinical breakdown of protocol effectiveness.

## ⚙️ Installation
This application is optimized for **Python 3.11.2**. Compatibility with other versions is not guaranteed.

### Previously

$ sudo apt install python3-tk
$ sudo apt update
$ sudo apt install mpv ffmpeg

### Using UV (Recommended)
[UV](https://github.com/astral-sh/uv) is the fastest way to manage dependencies and execute the application:

```bash
# Sync dependencies from uv.lock
uv sync

# Run the application
uv run app.py

# or much better
python3 -m my_tabata.app
```

### Traditional Installation (pip)

```bash
# Create and activate environment
python -m venv env
source env/bin/activate  # On Windows: .envScriptsactivate

# Install requirements
pip install -r requirements.txt

# Execute
python app.py
```
### By PIP
```bash
$ pip install my-tabata
```
## 📖 Usage Instructions

1. **Define Intervals:** Set the "Active Duration" (Work) and "Break Duration" (Rest) in seconds.
2. **Set Rounds:** Choose the number of cycles/sets for your session.
3. **Data Persistence:** Use the **Save** button to store your current configuration in a local file. Use **Delete** to clear stored settings.
4. **Session Control:**
   * **START:** Begins the workout sequence.
   * **PAUSE:** Suspends the timer (ideal for unexpected interruptions).
   * **RESTART:** Resumes the session from the current state.
   * **STOP:** Safely terminates the session and exits the cycle.


**Disclaimer:** *High-intensity interval training can be physically demanding. Consult a physician before beginning any new exercise regimen.*

