from pathlib import Path

from demo.importer.configuration import get_configuration
from demo.importer.data_repo import DataRepo, get_connection
from demo.importer.read_file_service import FileReader

if __name__ == "__main__":

    configuration = get_configuration()

    repo = DataRepo(connection=get_connection(configuration=configuration))

    print(list(repo.get_all_data()))  # noqa: T201

    reader = FileReader()

    print(reader.read_file(Path(configuration.input_file)))  # noqa: T201
