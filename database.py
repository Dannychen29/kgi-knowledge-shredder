import sqlite3
import os

DB_PATH = "knowledge.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS KnowledgeDomains (
            domain_id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain_name TEXT NOT NULL UNIQUE,
            description TEXT
        );

        CREATE TABLE IF NOT EXISTS SourceDocuments (
            doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
            trainer_id TEXT DEFAULT 'trainer_01',
            file_name TEXT NOT NULL,
            raw_text TEXT NOT NULL,
            upload_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS Document_Domain_Map (
            map_id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_id INTEGER NOT NULL,
            domain_id INTEGER NOT NULL,
            FOREIGN KEY (doc_id) REFERENCES SourceDocuments(doc_id),
            FOREIGN KEY (domain_id) REFERENCES KnowledgeDomains(domain_id)
        );

        CREATE TABLE IF NOT EXISTS MicroModules (
            module_id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_id INTEGER NOT NULL,
            module_title TEXT,
            module_content TEXT NOT NULL,
            reading_time_minutes REAL DEFAULT 2.0,
            FOREIGN KEY (doc_id) REFERENCES SourceDocuments(doc_id)
        );
    """)

    # Insert default domains
    default_domains = [
        ("Life Insurance", "Topics related to life insurance products and policies"),
        ("Investment Linked", "Investment-linked insurance products and strategies"),
        ("CRM", "Customer Relationship Management and client interaction"),
        ("Compliance", "Regulatory compliance and legal requirements"),
        ("Wealth Management", "Wealth planning and asset management strategies"),
        ("Tax Regulations", "Tax laws and financial tax planning"),
        ("Estate Planning", "Estate planning for high-net-worth individuals"),
        ("Digital Tools", "Internal digital platforms and tools usage"),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO KnowledgeDomains (domain_name, description)
        VALUES (?, ?)
    """, default_domains)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
