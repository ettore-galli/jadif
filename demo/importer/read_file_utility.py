from pathlib import Path

from jadif.jadif import dependency
from tests.jadif.example_reader.read_file_service import BaseFileReader


def read_file_function(filename: Path) -> list[str]:
    file_reader: BaseFileReader = dependency.resolve(BaseFileReader)
    return file_reader.read_file(filename=filename)
