from dataclasses import dataclass


@dataclass
class Configuration:
    host: str
    port: str
    user: str
    password: str
    database: str


def get_db_connection() -> Configuration:
    return Configuration(
        host="localhost",
        port="3306",
        user="utente",
        password="password",  # noqa: S106
        database="jadif-demo",
    )
