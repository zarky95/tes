from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Langkah 1: Tentukan koneksi database
# (SQLite digunakan di contoh ini)
engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Langkah 2: Buat base class untuk model
Base = declarative_base()

# Langkah 3: Definisikan model/tabel
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

# Langkah 4: Buat tabel di database
Base.metadata.create_all(engine)

# Langkah 5: Buat sesi untuk interaksi dengan database
Session = sessionmaker(bind=engine)
session = Session()
