from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parent

# Data storage locations
DATA_DIR = BASE_DIR / "data"
CACHE_PATH = DATA_DIR / "cache"
FINGERPRINT_PATH = DATA_DIR / "fingerprints"

# SQLite database file
DATABASE_PATH = DATA_DIR / "stylometry.db"

# NiceGUI application port
APP_PORT = 8080
