from __future__ import annotations
from pathlib import Path
from sqlalchemy.ext.declarative import DeclarativeMeta
from Misc.DatabaseManager import DatabaseManager
import os


class InitializationManager:
    SETTINGS_DIRECTORY = '.filesync'

    _instance: InitializationManager = None

    def __init__(self) -> None:
        self._path = os.getcwd()
        self.prepareStructure()
        self._databaseManager = DatabaseManager(self.SETTINGS_DIRECTORY)

    @classmethod
    def instance(cls) -> InitializationManager:
        if cls._instance is None:
            cls._instance = InitializationManager()

        return cls._instance

    def getDatabaseManager(self) -> DatabaseManager:
        return self._databaseManager

    def prepareStructure(self) -> None:
        Path(self._path).joinpath(self.SETTINGS_DIRECTORY).mkdir(parents=True, exist_ok=True)

    def getBaseModel(self) -> DeclarativeMeta:
        return self.getDatabaseManager().getBaseModel()
