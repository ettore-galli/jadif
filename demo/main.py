from demo.importer.configuration import get_db_connection
from demo.importer.data_repo import DataRepo, get_connection

if __name__ == "__main__":
    repo = DataRepo(connection=get_connection(configuration=get_db_connection()))

    print(list(repo.get_all_data()))  # noqa: T201
