# app/models.py
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, Column
from sqlalchemy import Integer, String, Date, ForeignKey, DateTime, Float
from app.core.db.session import Base
from datetime import datetime


class BtcOhlcv(Base):
    __tablename__ = "btc_ohlcv"
    time = Column(DateTime, primary_key=True)
    open = Column(Integer)
    high = Column(Integer)
    low = Column(Integer)
    close = Column(Integer)
    volume = Column(Float)


class BtcPreprocessed(Base):
    __tablename__ = "btc_preprocessed"
    time = Column(DateTime, primary_key=True)
    open = Column(Integer)
    high = Column(Integer)
    low = Column(Integer)
    close = Column(Integer)
    volume = Column(Float)
    label = Column(Integer)
    ma_7 = Column(Integer)
    ma_14 = Column(Integer)
    ma_30 = Column(Integer)
    rsi_14 = Column(Float)
    rsi_over = Column(Float)