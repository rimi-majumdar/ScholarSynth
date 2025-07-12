from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class SessionRecord(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    user = Column(String(100))
    document_name = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)
    questions = relationship("QARecord", back_populates="session")

class QARecord(Base):
    __tablename__ = "qa_records"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    question = Column(Text)
    answer = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    session = relationship("SessionRecord", back_populates="questions")

# DB setup
engine = create_engine("sqlite:///memory.db")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)