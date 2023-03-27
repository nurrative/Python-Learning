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
DROP DATABASE name_of_db;
--удаление бд
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