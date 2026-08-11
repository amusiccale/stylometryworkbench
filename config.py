from pathlib import Path

#
# Base project directory
#

BASE_DIR = Path(__file__).resolve().parent

#
# User data directory
#

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

CACHE_PATH = DATA_DIR / "cache"
FINGERPRINT_PATH = DATA_DIR / "fingerprints"

CACHE_PATH.mkdir(
    parents=True,
    exist_ok=True,
)

FINGERPRINT_PATH.mkdir(
    parents=True,
    exist_ok=True,
)

DATABASE_PATH = (
    DATA_DIR /
    "stylometry.db"
)

APP_PORT = 8080
