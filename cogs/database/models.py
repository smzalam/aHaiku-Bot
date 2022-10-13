from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Text, BigInteger
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Rules(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, nullable=False)
    rule = Column(Text, nullable=False)


class ServerStats(Base):
    __tablename__ = "server_stats"

    server_id = Column(BigInteger, primary_key=True, nullable=False)
    server_name = Column(String, nullable=False)
    channel_id = Column(String, nullable=True)
    channel_name = Column(String, nullable=True)
    streak = Column(Integer, nullable=False)


class Syllables(Base):
    __tablename__ = "syllables"

    server_id = Column(BigInteger, ForeignKey("server_stats.server_id", ondelete="CASCADE"), primary_key = True, nullable=False)
    line_one = Column(Integer, nullable=False)
    line_two = Column(Integer, nullable=False)
    line_three = Column(Integer, nullable=False)