import os.path

CURRENT_FILE = os.path.abspath(__file__)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, "resources")
print(TMP_DIR)

if not os.path.exists("resources"):
    os.mkdir("resources")