import sys
from pathlib import Path

from demo.importer_no_di.clock import get_current_datetime
from demo.importer_no_di.configuration import Configuration, get_configuration
from demo.importer_no_di.data_repo import DataRepo, get_connection
from demo.importer_no_di.read_file_service import FileReader


def get_input_file() -> Path:
    return Path(sys.argv[1])


def import_file(configuration: Configuration) -> None:

    repo = DataRepo(connection=get_connection(configuration=configuration))

    reader = FileReader()

    for line in reader.read_file(Path(configuration.input_file)):
        repo.insert(content=line, import_date=get_current_datetime())


def show_database_content(configuration: Configuration) -> None:
    repo = DataRepo(connection=get_connection(configuration=configuration))

    print(list(repo.get_all_data()))  # noqa: T201


if __name__ == "__main__":
    configuration = get_configuration(config_file=get_input_file())

    import_file(configuration=configuration)
    show_database_content(configuration=configuration)
