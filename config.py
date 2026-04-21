import os


def load_config(default_soft, default_hard, default_steps):
    """
    Reads configuration from 'config.txt'.
    Format:
    Line 1: Soft interval (int)
    Line 2: Hard interval (int)
    Line 3: Steps (int)

    If the file is missing or corrupted, it returns the provided defaults.
    """
    # Ensure we look for the file in the same directory as this script
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "configuration.txt")

    if not os.path.exists(file_path):
        print(f"Config file not found at {file_path}. Using defaults.")
        return default_soft, default_hard, default_steps

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]

            if len(lines) >= 3:
                soft = int(lines[0])
                hard = int(lines[1])
                steps = int(lines[2])
                print("Configuration loaded successfully.")
                return soft, hard, steps
            else:
                print("Config file is incomplete. Using defaults.")

    except (ValueError, IOError) as e:
        print(f"Error reading config file: {e}. Using defaults.")

    return default_soft, default_hard, default_steps