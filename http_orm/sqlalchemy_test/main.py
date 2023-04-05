from sqlalchemy import create_engine, Column,Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

#driver://user:password@host:port/db_name
db_url = 'postgresql://Nurik:1@127.0.0.1:5432/sqlalchemy_test'
engine = create_engine(db_url)
#подключение к бд

Base = declarative_base()
# базовый класс для таблиц

# создаем таблицу
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer,primary_key=True)
    title = Column(String)
    price = Column(Integer)

Base.metadata.create_all(bind=engine)
# записываем таблицу в бд

SessionLoocal = sessionmaker(bind=engine)
# создаем класс для сессии(один обьект от данного класса - одна сессия)

session = SessionLoocal()
# создаем сессию

new_product = Product(title = 'product1',price = 120)
# создаем продукт(запись в таблицу)
#  для орм создаем запрос на запись в таблицу

session.add(new_product)
# добавляем запрос в сессию

session.commit()
# отправляем набор запросов бд

