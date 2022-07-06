# from datetime import datetime
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
# from unicodedata import name

from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

class Address_book(Base):
    __tablename__= "addressbook"
    id = Column(Integer, primary_key=True)
    records = relationship("Record", cascade="all, delete", backref="book")

class Record(Base):
    __tablename__= "record"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    birthday = relationship("Birthday", cascade="all, delete", backref="user", uselist=False)
    phones = relationship("Phone", cascade="all, delete", backref="user")
    addresses = relationship("Address", cascade="all, delete", backref="user")
    emails = relationship("Email", cascade="all, delete", backref="user")
    book_id = Column(Integer, ForeignKey(Address_book.id, ondelete="CASCADE"))

class Birthday(Base):
    __tablename__= "birthday"
    id = Column(Integer, primary_key=True)
    bd_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey(Record.id, ondelete="CASCADE"))

class Phone(Base):
    __tablename__= "phone"
    id = Column(Integer, primary_key=True)
    number = Column(String(15), nullable=False)
    user_id = Column(Integer, ForeignKey(Record.id, ondelete="CASCADE"))

class Address(Base):
    __tablename__= "address"
    id = Column(Integer, primary_key=True)
    address = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey(Record.id, ondelete="CASCADE"))

class Email(Base):
    __tablename__= "email"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey(Record.id, ondelete="CASCADE"))
