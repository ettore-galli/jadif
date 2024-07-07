import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path

from jadif.jadif import dependency

from tests.jadif.example_reader.base import InputFile
from tests.jadif.example_reader.read_file_service import BaseFileReader


class BaseDBRepo(ABC):
    @abstractmethod
    def __init__(self, db: Path, file_reader: BaseFileReader) -> None:
        super().__init__()

    @abstractmethod
    def perform(self) -> list[str]:
        pass


class SQLiteDbRepo(BaseDBRepo):
    def __init__(self, db: Path, file_reader: BaseFileReader) -> None:
        super().__init__(db=db, file_reader=file_reader)
        self.db: Path = db
        self.file_reader = file_reader

    def perform(self) -> list[str]:
        connection = sqlite3.connect(self.db)
        cur = connection.cursor()
        cur.execute("DROP TABLE IF EXISTS messages")
        cur.execute("CREATE TABLE messages(message)")
        for text in self.file_reader.read_file(filename=dependency.resolve(InputFile)):
            cur.execute(
                "INSERT INTO messages(message) VALUES(:message)", {"message": text}
            )
        cur.execute("SELECT message FROM messages")
        messages = [row[0] for row in cur.fetchall()]
        connection.close()

        return messages


class DummyRepo(BaseDBRepo):
    def __init__(self, db: Path, file_reader: BaseFileReader) -> None:
        super().__init__(db=db, file_reader=file_reader)
        self.db: Path = db
        self.file_reader = file_reader

    def perform(self) -> list[str]:
        return ["dummy", "data", str(self.db)]
