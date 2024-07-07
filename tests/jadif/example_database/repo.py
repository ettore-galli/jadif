import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path


class BaseDBRepo(ABC):
    @abstractmethod
    def __init__(self, db: Path) -> None:
        super().__init__()

    @abstractmethod
    def perform(self) -> list[str]:
        pass


class SQLiteDbRepo(BaseDBRepo):
    def __init__(self, db: Path) -> None:
        super().__init__(db=db)
        self.db: Path = db

    def perform(self) -> list[str]:
        connection = sqlite3.connect(self.db)
        cur = connection.cursor()
        cur.execute("DROP TABLE IF EXISTS messages")
        cur.execute("CREATE TABLE messages(message)")
        for text in [
            "Example content in file\n",
            "This is the content of the actual file",
        ]:
            cur.execute(
                "INSERT INTO messages(message) VALUES(:message)", {"message": text}
            )
        cur.execute("SELECT message FROM messages")
        messages = [row[0] for row in cur.fetchall()]
        connection.close()

        return messages


class DummyRepo(BaseDBRepo):
    def __init__(self, db: Path) -> None:
        super().__init__(db=db)
        self.db: Path = db

    def perform(self) -> list[str]:
        return ["dummy", "data", str(self.db)]
