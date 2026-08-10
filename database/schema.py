"""
database/schema.py

Database schema definitions for the
Stylometric Fingerprint Workbench.
"""

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY,
    display_name TEXT,
    created_date TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS documents (
    document_id INTEGER PRIMARY KEY,
    author_id INTEGER NOT NULL,
    filename TEXT,
    text TEXT,
    word_count INTEGER,
    date_added TEXT,
    FOREIGN KEY (author_id)
        REFERENCES authors(author_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fingerprints (
    author_id INTEGER PRIMARY KEY,
    feature_json TEXT,
    total_words INTEGER,
    total_docs INTEGER,
    updated TEXT,
    FOREIGN KEY (author_id)
        REFERENCES authors(author_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS comparisons (
    comparison_id INTEGER PRIMARY KEY,
    date TEXT,
    source_author INTEGER,
    target_author INTEGER,
    distance REAL,
    similarity REAL,
    FOREIGN KEY (source_author)
        REFERENCES authors(author_id),
    FOREIGN KEY (target_author)
        REFERENCES authors(author_id)
);
"""


def create_schema(connection) -> None:
    """
    Create all required database tables.
    """
    cursor = connection.cursor()
    cursor.executescript(SCHEMA_SQL)
    connection.commit()
