from pathlib import Path

from jadif.jadif import dependency

from tests.jadif.example_database.db_importer import import_into_db
from tests.jadif.example_database.repo import BaseDBRepo, DummyRepo, SQLiteDbRepo
from tests.jadif.example_reader.base import InputFile
from tests.jadif.example_reader.read_file_service import (
    BaseFileReader,
    DummyFileReader,
    FileReader,
)

DB_FILE = Path(Path(__file__).parent, "data", "example-db.db")
EXAMPLE_FILE = Path(Path(__file__).parent, "data", "example-file.txt")


def make_sqlite_dependency() -> None:
    source_file = EXAMPLE_FILE
    dependency.add_config(InputFile, source_file)
    reader = FileReader()
    dependency.add_config(BaseFileReader, reader)
    repo = SQLiteDbRepo(db=DB_FILE, file_reader=reader)
    dependency.add_config(BaseDBRepo, repo)


def make_dummy_dependency() -> None:
    source_file = Path("dummy.txt")
    dependency.add_config(InputFile, source_file)
    reader = DummyFileReader()
    dependency.add_config(BaseFileReader, reader)
    repo = DummyRepo(db=Path("any"), file_reader=reader)
    dependency.add_config(BaseDBRepo, repo)


def test_dependency_injection_process_normal() -> None:
    make_sqlite_dependency()

    assert import_into_db() == [
        "Example content in file\n",
        "This is the content of the actual file",
    ]


def test_dependency_injection_process_dummy() -> None:
    make_dummy_dependency()

    assert import_into_db() == ["dummy", "data", "any"]
