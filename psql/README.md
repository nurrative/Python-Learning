# Slash commands
* \l - список всех бд
* \c - показывает через какого юзера и к какой бд мы подключены
* \c name_of_db - подключаемся к какой-то бд
* \du - список всех юзеров в postgres
* \dt - список всех таблиц в текущей бд
* \d+ - более подробная информация о таблицах в текущей бд
* \d+ name_of_table - более подробная информация о таблице
* \q - выход из субд(psql)

# Создание бд и таблиц
```sql
CREATE DATABASE name_of_db;
-- создание бд
```

```sql
CREATE TABLE name_of_table(
    column1 data_type1,
    column2 data_type2,
    ...
);
```

# Удаление базы данных
```sql
DROP DATABASE name_of_db;
--удаление бд
```
# Удаление таблицы
```sql
DROP TABLE name_of_db;
--удаление таблицы
```


# Заполнение таблиц 
```sql
INSERT INTO name_of_db VALUES
(val1,val2),
(val1.2,val2.2);
-- заполнение данных таблицу (заполнение всех полей)
```

# Вывод данных из таблицы
```sql
SELECT * FROM name_of_table;
-- вывод всех записей со всеми полями
```

```sql
SELECT column1,column3 FROM name_of_table;
-- вывод конкретных полей
```

# Условия
```sql
DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответствующих данному условию
```

``` sql
# (короче ilike и like чаше используется в поиске в таблице)
-- like - чувствительный к регистру (World - не пройдет)
SELECT * FROM name_of_table WHERE title ilike '%world%';
-- ilike - не чувствительный к регистру
-- WORLD
-- World
-- worLD
-- hello World
-- world Hello
-- HEllo WORLD hello
 SELECT * FROM name_of_table ORDER BY column1;
-- сортировка по определенному полю (по возрастанию ASC)
SELECT * FROM name_of_table ORDER BY column1 DESC;
-- сортировка по определенному полю (по убыванию DESC)
 SELECT * FROM name_of_table LIMIT 10;
-- выводит первые 10 записей
select * from product  where id > 4 limit 3;
(тут я поставила условие если айдишка больше 4 - букв вытащи мне 3 таких продуктов)
SELECT * FROM name_of_table OFFSET 10;
-- пропускает первые 10 записей
SELECT * FROM name_of_table LIMIT 5 OFFSET 10;
-- пропускает первые 10 записей
-- выбирает следующие 5 записей#
```

# Обновление таблицы 

```sql
ALTER TABLE name_of_table ADD COLUMN col_name col_type constraint;
--добавляем новую колонку в таблицу
```

```sql
ALTER TABLE name_of_table DROP COLUMN col_name;
--удаляем колонку в таблицу
```

```sql
ALTER TABLE name_of_table RENAME COLUMN col_name TO new_column_name;
--переименование колонки
```

# Ограничения 
```sql
* UNIQUE - не разрешает дубликаты
* NOT NULL - Требует обязательного заполнения поля
* PRIMARY KEY - как UNIQUE и NOT NULL + строит binary tree для быстрого поиска
* FOREIGN KEY - ссылается на pk в другой таблице и проверяет существует ли такое id

```

# Связи
## Виды связей
> Один к одному(one to one)
* один человек - один профиль
* один автор - одна автобиография

> один ко многим(one to many)
* один блогер много постов
* одна марка - много моделей
* один продукт - много комментариев

> многие ко многим(many to many)
* один разработчик - много проектов, один проект - много разработчиков

## реализация one2many в postgres
```sql
CREATE TABLE blogger(
    id serial PRIMARY KEY,
    name varchar(50),
    email varchar(70),             
    age int);

CREATE TABLE post(
    id serial PRIMARY KEY,
    title varchar(100),
    body text,
    bloger_id int,
    CONSTRANT fk_post_blogger
    FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);
```

# JOINS
> **join** - инструкция, которая позволяет одним SELECT, брать данные из двух таблиц (у которых есть связанные поля)

> **INNER JOIN(JOIN)** - достаются только те записи у которых есть данные в обоих таблицах
> **FULL JOIN** - достаются все записи и с первой таблицы и со второй
