import sqlite3


class TriangleDatabase:
    def __init__(self, db_path: str = ":memory:") -> None:
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self) -> None:
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS triangles (
                side1 REAL NOT NULL,
                side2 REAL NOT NULL,
                side3 REAL NOT NULL,
                triangle_type TEXT NOT NULL,
                error_message TEXT,
                PRIMARY KEY (side1, side2, side3)
            )
            """
        )
        self.connection.commit()

    def add_record(self, side1, side2, side3, triangle_type, error_message=None):
        self.connection.execute(
            "INSERT OR REPLACE INTO triangles VALUES (?, ?, ?, ?, ?)",
            (side1, side2, side3, triangle_type, error_message),
        )
        self.connection.commit()

    def get_record(self, side1, side2, side3):
        cursor = self.connection.execute(
            "SELECT triangle_type, error_message FROM triangles "
            "WHERE side1=? AND side2=? AND side3=?",
            (side1, side2, side3),
        )
        return cursor.fetchone()

    def delete_record(self, side1, side2, side3) -> bool:
        cursor = self.connection.execute(
            "DELETE FROM triangles WHERE side1=? AND side2=? AND side3=?",
            (side1, side2, side3),
        )
        self.connection.commit()
        return cursor.rowcount > 0

    def close(self):
        self.connection.close()