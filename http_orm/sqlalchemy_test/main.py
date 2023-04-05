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

    def __repr__(self) -> str:
        return f"{self.id} -> {self.title} <-> {self.price} "

Base.metadata.create_all(bind=engine)
# записываем таблицу в бд

SessionLoocal = sessionmaker(bind=engine)
# создаем класс для сессии(один обьект от данного класса - одна сессия)

session = SessionLoocal()
# создаем сессию

new_product = Product(title = 'product1',price = 120)
# создаем продукт(запись в таблицу)
# для орм создаем запрос на запись в таблицу

# session.add(new_product)
# добавляем запрос в сессию

# session.commit()
# отправляем набор запросов бд

products = session.query(Product).all()
# получаем все записи из таблиы product
print(products)

# session.add(Product(title='product2', price=34))
# session.add(Product(title='product3', price=245))
# session.add(Product(title='product4', price=45))
# session.add(Product(title='product5', price=345))
# session.commit()
products = session.query(Product).all()
# получаем все записи из таблиы product
print(products)

products = session.query(Product).filter(Product.price>100).all()
# получаем все записи из таблиы product у которых цена больше 100
print(products)

product3 = session.query(Product).get(3)
# получаем продукт под id 3
print(product3)

# product4 = session.query(Product).get(4)
# session.delete(product4)
# session.commit()

product3.title = 'new title'
product3.price = 100

session.commit()

