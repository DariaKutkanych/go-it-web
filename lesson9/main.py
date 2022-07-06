from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date


from models import Address_book, Address, Birthday, Phone, Email, Record


engine = create_engine("sqlite:///helper.db")
Session = sessionmaker(bind=engine)
session = Session()

bd1 = Birthday(bd_date=date(day=1, month=12, year=1998))
bd2 = Birthday(bd_date=date(day=14, month=8, year=2000))

ad1 = Address(address="Peremohy str")
ad2 = Address(address="Bohunska str")
ad3 = Address(address="Theatralna str")

email1 = Email(email="u1@gmail.com")
email2 = Email(email="u2@gmail.com")
email3 = Email(email="u3@gmail.com")

phone1 = Phone(number="0948684832")
phone2 = Phone(number="04950684958")
phone3 = Phone(number="9847564234")

user1 = Record(name="Daria", birthday=bd1)
user2 = Record(name="Claire", birthday=bd2)

user1.phones = [phone1, phone2]
user2.phones = [phone3]

user1.emails = [email1]
user2.emails = [email2, email3]

user1.addresses = [ad1, ad2]
user2.addresses = [ad3]

book = Address_book()

book.records = [user1, user2]


session.add(book)
session.commit()
session.close()