"""
run_sfw.py

Stylometric Fingerprint Workbench
startup script.
"""

from database.db import (
    initialize_database,
)

print()
print(
    "Initializing database..."
)

initialize_database()

print(
    "Database ready."
)

print(
    "Launching application..."
)

import app
