import os
from pathlib import Path

def users():
    for filename in os.listdir(Path.home() / '.config/nospy/'):
        if filename == ".DS_Store":
            continue

        print(filename.split('.json')[0])
