from collections.abc import Generator
from datetime import datetime

import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from demo.importer.configuration import Configuration


def get_connection(
    configuration: Configuration,
) -> PooledMySQLConnection | MySQLConnectionAbstract:
    return mysql.connector.connect(
        user=configuration.user,
        password=configuration.password,
        host=configuration.host,
        port=configuration.port,
        database=configuration.database,
    )


class DataRepo:
    def __init__(
        self, connection: PooledMySQLConnection | MySQLConnectionAbstract
    ) -> None:
        self.connection: PooledMySQLConnection | MySQLConnectionAbstract = connection

    def get_all_data(self) -> Generator[tuple, None, None]:
        cursor = self.connection.cursor()

        query = "SELECT * FROM import_data "

        cursor.execute(query)

        for row in cursor:  # type: ignore[union-attr]
            yield tuple(row)

        cursor.close()

    def insert(self, content: str, import_date: datetime) -> None:
        cursor = self.connection.cursor()

        query = "INSERT INTO import_data(CONTENT, IMPORT_DATE) VALUES(%s, %s) "

        cursor.execute(query, (content, import_date))

        self.connection.commit()

        cursor.close()
