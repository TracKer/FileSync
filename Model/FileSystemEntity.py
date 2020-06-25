from sqlalchemy import Column, Integer, String, TIMESTAMP, SmallInteger
from Misc.InitializationManager import InitializationManager


class FileSystemEntity(InitializationManager.instance().getBaseModel()):
    TYPE_FILE: int = 0
    TYPE_DIR: int = 1

    __tablename__ = 'fs_entity'

    id = Column(Integer, primary_key=True)
    type = Column(SmallInteger, nullable=False)
    path = Column(String(255), nullable=False, comment='Relative file path')
    created_at = Column(TIMESTAMP, nullable=False, comment='File creation date')
    modified_at = Column(TIMESTAMP, nullable=False, comment='File modification date')
    hash = Column(String(32), nullable=False, comment='File MD5 hash')
