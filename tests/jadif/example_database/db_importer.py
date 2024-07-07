from jadif.jadif import dependency

from tests.jadif.example_database.repo import BaseDBRepo


def import_into_db_injectable(repo: BaseDBRepo) -> list[str]:
    return repo.perform()


def import_into_db() -> list[str]:
    repo = dependency.resolve(BaseDBRepo)
    return repo.perform()
