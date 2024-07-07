from pathlib import Path

from jadif.jadif import dependency

from tests.jadif.example_database.db_importer import import_into_db
from tests.jadif.example_database.repo import BaseDBRepo, DummyRepo, SQLiteDbRepo

DB_FILE = Path(Path(__file__).parent, "data", "example-db.db")


def make_sqlite_dependency() -> None:
    repo = SQLiteDbRepo(db=DB_FILE)
    dependency.add_config(BaseDBRepo, repo)


def make_dummy_dependency() -> None:
    reader = DummyRepo(db=Path("any"))
    dependency.add_config(BaseDBRepo, reader)


def test_dependency_injection_process_normal() -> None:
    make_sqlite_dependency()

    assert import_into_db() == [
        "Example content in file\n",
        "This is the content of the actual file",
    ]


def test_dependency_injection_process_dummy() -> None:
    make_dummy_dependency()

    assert import_into_db() == ["dummy", "data", "any"]
