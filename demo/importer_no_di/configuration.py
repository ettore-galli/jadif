import configparser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Configuration:
    host: str
    port: str
    user: str
    password: str
    database: str
    input_file: str


def get_configuration(config_file: Path) -> Configuration:
    config = configparser.ConfigParser()
    config.read(config_file)
    database_section = config["DATABASE"]
    return Configuration(
        host=database_section["host"],
        port=database_section["port"],
        user=database_section["user"],
        password=database_section["password"],
        database=database_section["database"],
        input_file=config["INPUT"]["input_file"],
    )
