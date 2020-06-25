from __future__ import annotations
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta


class DatabaseManager:
    DB_FILE_NAME = 'db.sqlite'

    def __init__(self, settingsDirectory: str) -> None:
        self._models: List[DeclarativeMeta] = []
        self._settingsDirectory = settingsDirectory
        self._databaseEngine: Engine = create_engine(f'sqlite:///{self._settingsDirectory}/{self.DB_FILE_NAME}')
        self._databaseBaseModel: DeclarativeMeta = declarative_base()

    def registerModel(self, model: DeclarativeMeta) -> None:
        self._models.append(model)

    def getBaseModel(self) -> DeclarativeMeta:
        return self._databaseBaseModel

    def initializeModels(self):
        self.getBaseModel().metadata.create_all(bind=self._databaseEngine)
