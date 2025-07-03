import os

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime


# Создаем базовый класс для моделей
Base = declarative_base()

# Определяем классы-модели (таблицы)
class User(Base):
    """Модель пользователя"""
    __tablename__ = 'nfs_users'

    telegram_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=True)
    birthday = Column(DateTime, nullable=False)
    is_admin = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    registered_at = Column(DateTime,default=datetime.utcnow)


    def __repr__(self):
        return f"<User(id={self.telegram_id}, username='{self.username}')>"

engine = create_engine(
    os.getenv("NFS_DATA_URL", "sqlite:///nfs.db"), echo=True)





