import sqlite3

from src.core.paths import REGISTRY_DIR

DB_PATH = REGISTRY_DIR / "documents.db"


class DocumentRegistry:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL,
                file_path TEXT UNIQUE NOT NULL,
                file_hash TEXT NOT NULL,
                file_size INTEGER,
                source_type TEXT,
                status TEXT,
                chunk_count INTEGER DEFAULT 0,
                embedding_model TEXT,
                error_message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                processed_at TIMESTAMP,
                last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.conn.commit()

    def get_document_by_path(self, file_path):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM documents
            WHERE file_path = ?
            """,
            (file_path,)
        )

        return cursor.fetchone()

    def get_document_by_hash(self, file_hash):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM documents
            WHERE file_hash = ?
            """,
            (file_hash,)
        )

        return cursor.fetchone()

    def register_document(self, document):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO documents (
                file_name,
                file_path,
                file_hash,
                file_size,
                source_type,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                document["file_name"],
                document["file_path"],
                document["file_hash"],
                document["file_size"],
                document["source_type"],
                "pending"
            )
        )

        self.conn.commit()

    def update_document_hash(self, file_path, new_hash, file_size):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE documents
            SET
                file_hash = ?,
                file_size = ?,
                status = 'pending',
                last_seen = CURRENT_TIMESTAMP
            WHERE file_path = ?
            """,
            (
                new_hash,
                file_size,
                file_path
            )
        )

        self.conn.commit()

    def update_status(self, file_path, status):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE documents
            SET status = ?
            WHERE file_path = ?
            """,
            (
                status,
                file_path
            )
        )

        self.conn.commit()

    def mark_completed(
        self,
        file_path,
        chunk_count,
        embedding_model
    ):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE documents
            SET
                status = ?,
                chunk_count = ?,
                embedding_model = ?,
                processed_at = CURRENT_TIMESTAMP
            WHERE file_path = ?
            """,
            (
                "completed",
                chunk_count,
                embedding_model,
                file_path
            )
        )

        self.conn.commit()

    def mark_failed(self, file_path, error_message):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE documents
            SET
                status = ?,
                error_message = ?
            WHERE file_path = ?
            """,
            (
                "failed",
                error_message,
                file_path
            )
        )

        self.conn.commit()

    def get_all_documents(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT *
            FROM documents
        """)

        return cursor.fetchall()

    def close(self):
        self.conn.close()

    def delete_document(self, file_path):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            DELETE FROM documents
            WHERE file_path = ?
            """,
            (file_path,)
        )

        self.conn.commit()
