from pathlib import Path

from jadif.jadif import dependency

from tests.jadif.read_file_service import BaseFileReader, DummyFileReader, FileReader
from tests.jadif.read_file_utility import read_file_function

EXAMPLE_FILE = Path(Path(__file__).parent, "data", "example-file.txt")


def make_normal_dependency() -> None:
    reader = FileReader()
    dependency.add_config(BaseFileReader, reader)


def make_dummy_dependency() -> None:
    reader = DummyFileReader()
    dependency.add_config(BaseFileReader, reader)


def test_() -> None:
    assert EXAMPLE_FILE


def test_dependency_injection_process_normal() -> None:
    make_normal_dependency()

    assert read_file_function(filename=EXAMPLE_FILE) == [
        "Example content in file\n",
        "This is the content of the actual file",
    ]


def test_dependency_injection_process() -> None:
    make_dummy_dependency()

    assert read_file_function(filename=EXAMPLE_FILE) == ["dummy", "data"]
