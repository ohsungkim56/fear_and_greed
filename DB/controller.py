from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy.orm import Session
from sqlalchemy import Date, Integer

from . import engine

class Base(DeclarativeBase):
    pass

class FearAndGreed(Base):
    __tablename__ = "fear_and_greed"

    date: Mapped[Date] = mapped_column(Date, nullable=False, primary_key=True)
    value: Mapped[Integer] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<FearAndGreed(date={self.date}, value={self.value}>"


def insert(date, value):
    with Session(engine) as session:
        record = FearAndGreed(date=date, value=value)
        session.add(record)
        session.commit()

Base.metadata.create_all(engine)
