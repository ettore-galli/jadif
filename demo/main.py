import sys
from pathlib import Path

from demo.importer.clock import get_current_datetime
from demo.importer.configuration import get_configuration
from demo.importer.data_repo import DataRepo, get_connection
from demo.importer.read_file_service import FileReader


def get_input_file() -> Path:
    return Path(sys.argv[1])


if __name__ == "__main__":
    configuration = get_configuration(config_file=get_input_file())

    repo = DataRepo(connection=get_connection(configuration=configuration))

    reader = FileReader()

    for line in reader.read_file(Path(configuration.input_file)):
        repo.insert(content=line, import_date=get_current_datetime())

    print(list(repo.get_all_data()))  # noqa: T201
