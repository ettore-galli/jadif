from demo.importer_with_di.configuration import get_configuration
from demo.importer_with_di.data_repo import DataRepo
from demo.importer_with_di.di import configuration_di, database_di, file_reader_di
from demo.importer_with_di.read_file_service import BaseFileReader, FileReader


def prepare_configuration_di() -> None:
    file_reader_di.add_config(BaseFileReader, FileReader)
    database_di.add_config("DATA_REPO", DataRepo)
    configuration_di.add_config("CONFIGURATION", get_configuration)
