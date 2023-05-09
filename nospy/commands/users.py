import os
from pathlib import Path

from nospy.config import DATA_DIR

def users():
    # Ensure the data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    current_user = os.getenv("NOSPY_USER", "default")

    for filename in os.listdir(Path.home() / '.config/nospy/'):
        if filename == ".DS_Store":
            continue

        username = filename.split('.json')[0]

        if username == current_user:
            # print( f"* {username}" )
            print( f"\033[1;33m{username}\033[0m <--" )
        else:
            print( username )
