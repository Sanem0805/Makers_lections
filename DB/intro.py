# PostgreSQL - система управления базами данныхс(СУБД/ DBMS)
#  это ряд программ и инструментов позволяющих создавать БД, управлять ею и манипулировать данными внутри БД(CRUD).

# Posgres - сама база данных, она реалиционная, то есть данные храняться в виде таблиц  и таблицы имеют  связи между собой (relations)&
# SQL(Structured Query Language) - декларативный язык структурированных запросов, он применяетться для создания  и управления данными
#===================================================
# типы полей в postgres
# 1. Numeric types:
# a. smallint (2 bytes) -> -32767 to 32767
# b. integer (4 bytes) -> -2147000 t 2147000
# c. bigint(8 bytes) -> ....
# d. serial (4 bytes) -> auto-increment(integer, 1-214700)
# c. real(4 bytes) - число с плавающей точкой, вещественное число
# f. double precision (8 bytes) - real но только с двойной точностью
# 2. Character types:
# a. varchar(кол-во 255)- можем указатть макс кол-во символов в ручную. Если мы указали макс кол-во символов в 50, а заполнили только 10, то остальные 40 не заполняться
# b. char(255) - еслт если не заполним все символы то остальные заполняться пробелами
# с. text - неограниченное кол-во символов
# 3. Boolean types:
# #boolean(1 bytes) -> True/False
# 4. date - календарная дата (год.месяц.день)
# 5. location (point) - координаты
# SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);
#==================================================
#Связи между таблицами (relation):
    # 1. один к одному (One-to-one) - человек , паспорт
    # 2. Один ко многим(One-to-many) - человек и баковские карты
    # 3. Много ко многим(Many-to-many) - студенты и преподы
    # select * from table1 cross join table2;

#---------------------------------------------------
# constraints(Ограничения):
#         1.CHECK <column> > 5
#         2. UNIQUE - только уникальные значения
#         3. NOT NULL - обязательно к заполнению
#         4. PRIMARY KEY (для установки идентификатора данных в таблице)
#         5. FOREIGN KEY (для установки связи между таблицами)
#         6. DEFAULT <value>- добавляет дефолтное значение
#         Добавление к таблице кторая уже есть
#         ALTER TABLE cities ALTER COLUMN location SET NOT NULL;
#         ALTER TABLE products ADD CONSTRAINT <name_of_constr> UNIQUE (name);
#         ALTER TABLE cities ALTER COLUMN location SET NOT NULL;

#-----------------------------------------------------
# ubuntu: sudo -u postgres psql
# mac: psql postgres
# psql -> для входа через своего юзера
# \q -> выход из СУБД
# \du -> список свех юзеров
# \l -> список всех баз данных
# \c <dbname> -> команда для подключения к бд
#     \dt -> список таблиц в бд
#     \d <table> -> подробная информация про таблицу
# ИМПОР данных при помощи файла 
# psql -U <username> -d <database> -f <path_to_file>
# CREATE DATABASE <dbname>; -> команда для создания бд 
# CREATE TABLE <tablename> (
#     <name_of_column><type>
#     <name_of_column><type>
# ); команда для создания таблицы
# пример:
# СREATE TABLE weather (
#     city varchar(80)
#     temp_lo int,
#     temp_hi int,
#     prcp real,
#     date date
# );
# DROP DATABASE <name_of_db>; - удаление бд
# DROP TABLE <name_of_table>; - удаление таблицы
# DROP ... -> удаление
# CREATE USER <username> WITH PASSWORD '<password>'; -> команда для создания юзера
# ALTER USER <username> WITH SUPERUSER; команда для изменения статуса юзера на суперюзера
# SELECT <column> FROM <table>; команда для получения данных
# WHERE: используеться для фильтрации по полям. будут выводиться только те данные которые соответствуют условию WHERE
#Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему-либо'
# SELECT * FROM products WHERE meat = 'Becon'
# SELECT * FROM products WHERE meat in ('Becon'
# AND:  оператор и, для множесва уловий 
# Операторы сравнения: >, <, >=, <=, =, <>
# BETWEEN: Условие между 
# SELECT * FROM products WHERE id BETWEEN 3 and 8;
# SELECT * FROM produts WHERE id <= 8 and >= 3;
# ORDER BY : сортировка по входящим данным по  убыванию или возрастанию
            #ASC(по возрастанию) и DESC(по убывванию)
# SELECT <row> FROM <table> ORDER BY <row> [ASC/DESC]
# LIMIT:  позволяет нам вернуть данные в ограниченном колличечтве 
# SELECT <row> FROM <table> LIMIT 1;
# LIKE: выводит результат который соответствует введенному шабллону. Зависит от регистра
# ILIKE: не зависит от регистра
# Cинтаксис: SELECT * FROM products WHERE name LIKE 'S%';
# DISTINCT: Позволяет нам убрать  дубликаты и возвращает тоько уникальные значения 
# SELECT DISTINCT name FROM product
# SELECT first_name || ' ' || last_name FROM customer;

# select name || ' ' || last_name as "full name" from info; 
# select name || ' ' || last_name as "full name", email from info;
# select name as na, last_name as l_n from info;
# select * from info order by last_name; - сортировка по фамилии
# select * from info order by last_name, name; - сортировка по фамилии и по имени
# select * from info order by last_name asc, name desc;
# select * from info order by last_name asc nulls first;
# select * from info order by last_name asc nulls last;
# select distinct on(country) country, last_name from info order by country, last_name;
# select * from info where country = 'Kyrgyzstan';
# select * from info where age > 20;
# select name || ' ' || last_name as "full name", experience from info where experience >= 4;
# select name, last_name, email from info where name <> 'Katie';
# select name, last_name, email from info where last_name = 'Grey' or last_name = 'Far';
# select name, last_name, email from info where not last_name = 'Grey' or last_name = 'Far';
# select name, last_name, country from info where not country = 'USA';
# select name, last_name, country from info where not country in ('USA', 'France', 'England');
# select * from info where age between 20 and 30;
# select * from info where experience between 3 and 9;
# select * from info where (experience between 3 and 9) and (age between 20 and 30);

# select * from info where name like 'A%';
# select * from info where email like 'K%';
# select * from info where email like 'K_';
# select * from info where last_name like '%m' or  name like '%m';
# select * from info where last_name like '__m' or  name like '%m'; - где _ значит один символ
# select * from info where last_name ilike '%m'; - ilike чувствителен к регистру
# select * from info where last_name ilike '%m' and age between 20 and 25;
# select * from info where not last_name is null;

# select * from info limit 2;
# select * from info order by id limit 3;
# select * from info order by experience desc limit 3;
# select * from info order by experience desc limit 3 offset 4; -  скакого индекса начинаем сортировать
# select * from info order by experience desc FETCH FIRST (3) row only; - никакой разницы с limit только синтаксис другой
# select * from info order by experience desc offset 5 FETCH FIRST (3) row only;

# select sum(age) as age_sum from info where country = 'England';
# select sum(experience) as age_sum from info where country = 'England';

# select count(id) from info where email like '%gmail.com';

# select avg(experience) from info;
# select avg(experience) from info where country = 'England';

# select max(age) from info;
# select country, count(id) from info group by country;
# select programming_language, count(id) from info group by programming_language;

# select country, sum(experience) from info group by country;
# select country, avg(age) from info group by country;

# select programming_language, avg(experience) from info group by programming_language having avg(experience) > 2;
# select country, avg(experience) from info group by country having avg(experience) >= 3; - having  то же самое что и where используеться с group by

# update info set last_name='Snow', country='Kyrgyzstan' where id=9;
# update info set email='mike@lolo.com', experience=3 where id=5;
# update info set last_name='Broooo' where name='Lary'; - лучше и надо менять по id а не по имени

# alter table info alter column name type varchar(80);- изменение varchar() на кол-во

# alter table info rename column last_name to surname; - изменение имени столбца
# alter table info add constraint name_of_constraint unique (name); - меняем ограничение
# alter table info drop age, drop email; - удаляем колонки

#=======================
# JOIN - Оператор, который позволяет в запросах селект брать данные из нескольких таблиц

# INNER JOIN() - достаються только те записи, у котрых есть связь

# FULL JOIN - достаються все записи с обеих таблиц

# LEFT JOIN - достает все записи с слевой таблицы, а а справой только те записи у которых есть с левой таблицей

# RIGHT JOIN- достает все записи с правой таблицы а с левой только те записи у которых есть связь с правой таблицей

# где "левая" таблица это та таблица  которая записана до join а "правая" таблица котрая после join
# select * from table1 inner join table2 on table1.num = table2.num;
# select * from table1, table2 where table1.num = table2.num;
# select * from table1 inner join table2 USING(num);
# select * from table1 as t1 FULL JOIN table2 as t2 ON t1.num = t2.num;
# select * from table1 as t1 left join table2 as t2 on t1.num = t2.num;
# select * from table1 as t1 right join table2 as t2 on t1.num = t2.num;
# select * from table1 as t1 right join table2 as t2 on t1.name = t2.value; - когда не совпадают
# select * from table1 as t1 right join table2 as t2 on t1.num = t2.num and t2.value='xxx';
#===============================================================================
shop_db=# create table users(
id serial primary key,
name varchar(50),
last_name varchar(100));

shop_db=# create table email(
user_id int,
email varchar(60),
constraint email_unique unique (user_id));

alter table email add constraint fk_email_users foreign key(user_id) references users (id); - отошения one-to-one

shop_db=# create table product(
shop_db(# id serial primary key,
shop_db(# title varchar(150),
shop_db(# price int,
shop_db(# quantity int default 1);

shop_db=# create table orders(
shop_db(# id serial primary key,
shop_db(# user_id int,
shop_db(# address varchar(255),
shop_db(# constraint fk_order_users foreign key(user_id) references users(id));

shop_db=# create table order_product(
shop_db(# product_id int not null,
shop_db(# order_id int not null,
shop_db(# constraint fk_order_product_product foreign key(product_id) references product(id),
shop_db(# constraint fk_order_product_order foreign key(order_id) 
references orders(id));

select users.id, users.name, users.last_name, email.email from users inner join email on users.id=email.user_id; - связываем две таблицы
select u.id, u.name, u.last_name, e.email from users as u inner join email as e on u.id=e.user_id; - аналогично верней строке inner использовалт чтобы не выходтлт email если их нет

select u.id, u.name, u.last_name, e.email from users as u  left outer join email as e on u.id=e.user_id; - с левой части таблице

select u.id, u.name, u.last_name, e.email from users as u right  outer join email as e on u.id=e.user_id; - c левой таблицы начинаеться и так как bibbo не имеет emil он и не выходит

select u.id, u.name, u.last_name, e.email from users as u full  outer join email as e on u.id=e.user_id; - вытаскивает все записи

select o.id, o.address, u.name, u.last_name from orders as o inner join users as u on o.user_id=u.id; - связали две таблицы через id

select u.name, u.last_name, e.email, o.address from users as u inner join email as e on e.user_id=u.id inner join orders as o on o.user_id=u.id; - связали 3 сзвязи
select u.name, u.last_name, e.email, o.address from users as u full join email as e on e.user_id=u.id full join orders as o on o.user_id=u.id;- 3 cвязи и выводиться не зависимо есть у них email тлт нет

select p.title, o.address from order_product as op inner join product as p on op.product_id=p.id inner join orders as o on o.id=op.order_id;- связали две таблицы через таблицу посредник

select u.name, u.last_name, p.title, o.address from order_product as op inner join product as p on op.product_id=p.id inner join orders as o on op.order_id=o.id inner join users as u on o.user_id=u.id;- связали 3 таблицы
  name  | last_name |  title  |      address       
--------+-----------+---------+--------------------
 John   | Snow      | Asus    | London. Bakers St.
 John   | Snow      | Poco    | London. Bakers St.
 Jesica | Brown     | Poco    | London. Beauty St.
 Bimbo  | Tokoi     | Samsung | USA. Green St.
 Bimbo  | Tokoi     | Iphone  | USA. Green St.

select u.name, e.email, p.title, o.address, o.id from order_product as op inner join product as p on op.product_id=p.id inner join orders as o on op.order_id=o.id inner join users as u on o.user_id=u.id inner join email as e on u.id=e.user_id;- связали 4 таблицы

  name  |     email      | title |      address       | id 
--------+----------------+-------+--------------------+----
 John   | john@gmail.com | Asus  | London. Bakers St. |  1
 John   | john@gmail.com | Poco  | London. Bakers St. |  1
 Jesica | jes@yahoo.com  | Poco  | London. Beauty St. |  2
(3 rows)
select u.name, e.email, p.title, o.address, o.id from order_product as op full join product as p on op.product_id=p.id full join orders as o on op.order_id=o.id full join users as u on o.user_id=u.id full join email as e on u.id=e.user_id;- 4 таблицы исполтзовали full join
 name  |     email      |  title  |      address       | id 
--------+----------------+---------+--------------------+----
 John   | john@gmail.com | Asus    | London. Bakers St. |  1
 John   | john@gmail.com | Poco    | London. Bakers St. |  1
 Jesica | jes@yahoo.com  | Poco    | London. Beauty St. |  2
 Bimbo  |                | Samsung | USA. Green St.     |  4
 Bimbo  |                | Iphone  | USA. Green St.     |  4
 Jesica | jes@yahoo.com  |         | Vanice. Beauty St. |  3
 Sasha  | saha@mail.ru   |         |                    |   
(7 rows)

SELECT title, price, CASE WHEN price > 40000 THEN 'too much' ELSE 'ok' END effordability from product;
  title  | price | effordability 
---------+-------+---------------
 Samsung |  4000 | ok
 Asus    |  3000 | ok
 Iphone  |  8000 | ok
 Poco    |  3000 | ok
(4 rows)

select title, price, case when quantity = 0 then 'out of stock' when quantity between 1 and 10 then 'hurry up!!!' else 'in stock' end from product;
  title  | price |    case     
---------+-------+-------------
 Samsung |  4000 | in stock
 Asus    |  3000 | in stock
 Iphone  |  8000 | hurry up!!!
 Poco    |  3000 | hurry up!!!
(4 rows)

# INSERT INTO <tablename> (<columns>) VALUES
#     # (datas_to_comuns); - команда для заполнения данных в таблицу
    
#     INSERT INTO cities (name, location)
#     VALUES ('Bishkek', '(42.52, 74.59)') title

# weather_db=# create table singer (
# weather_db(# id serial primary key,
# weather_db(# name varchar(50) not null,
# weather_db(# last_name varchar(50) not null,
# weather_db(# age int check ( age > 0));
# CREATE TABLE
# weather_db=# CREATE TABLE song(
# weather_db(# id serial primary key, 
# weather_db(# title varchar(100),
# weather_db(# owner int REFERENCES singer(id),
# weather_db(# feat int,
# weather_db(# CONSTRAINT fk_feat FOREIGN KEY (feat) REFERENCES singer(id));
# CREATE TABLE

# UPDATE <tablename> SET <row> = <new_value>
# WHERE <row> = <value>; - команда для обнавления данных 
# Указываем после WHERE то какой объект обновить

# DELETE FROM <tablename> WHERE <column> = <data>; - команда для удаления

# СREATE USER <username> WITH PASSWORD '<password>'; - команда для создания юзера

# ✅1. Создайте таблицу makers в БД mydb;

# CREATE DATABASE mydb;

# \c mydb

#     ✅2. В этой таблице создайте следующие поля:
#      Mentor_id 
#      Name
#      Position (choose from: mentor, tracker, scrum)
#      Birthdate
#      Salary

# CREATE TABLE makers (
# Menthor_id SERIAL,
# Name VARCHAR(50),
# Position VARCHAR(7),
# Birthday int,
# Salary int);

#     ✅Заполните таблицу не менее, чем 15 записями

# INSERT INTO makers (Name, Position, Birthday, Salary) VALUES
# ('Sanzhar','Mentor', 2000, 2000),
# ('Sultan', 'Tracker', 2000, 1500),
# ('Aigerim', 'Scrum', 2002, 1500),
# ('Aibek', 'Mentor', 1999, 1000),
# ('Sezim', 'Tracker', 1998, 1500),
# ('Samat', 'Scrum', 2001, 5500),
# ('Aika', 'Mentor', 1996, 8000),
# ('Meerim', 'Tracker', 1999, 6000),
# ('Tariel', 'Scrum', 1995, 9000),
# ('Robert', 'Mentor', 1990, 7000),
# ('Bermet', 'Tracker', 2002, 3000),
# ('Saikal', 'Scrum', 1997, 4400),
# ('Azamat', 'Mentor', 1998, 5000),
# ('Kanybek', 'Tracker', 2000, 3500),
# ('Bek', 'Scrum', 2002, 6600);

# SELECT * FROM makers;

#     ✅Вытащите position и name в одном столбце под
#     названием mentors

# SELECT name  ' '  position AS mentors FROM makers;

#     ✅Вытащите все поля в порядке убывания возрастов
#     менторов

# SELECT * FROM makers ORDER BY birthday;

#     ✅Вытащите только те записи, в которых позиция либо
#     mentor, либо tracker, и имя начиналось на ‘A’ или ‘S’

# 1) SELECT * FROM makers WHERE position = 'Mentor' or position = 'Tracker';
# 2) SELECT * FROM makers WHERE name LIKE 'S%' or name LIKE 'A%';
# Не получается объединить 2 условия. Выдает ошибку!

#     ✅Вытащите только те записи, в которых salary находится
#     в промежутке от 5000$ до 8000$

# SELECT * FROM makers WHERE salary BETWEEN 5000 and 8000;

#     ✅Вытащите первые три записи, в которых максимальная
#     зарплата

# SELECT * FROM makers ORDER BY salary DESC LIMIT 3;

#     ✅Вытащите количество работников, группируя по
#     позиции position (сколько работников на каждой
#     позиции)

# SELECT COUNT(*) FROM makers WHERE position = 'Mentor';
# SELECT COUNT(*) FROM makers WHERE position = 'Tracker'; 
# SELECT COUNT(*) FROM makers WHERE position = 'Scrum'; 

#     ✅Определите среднюю заработную плату у scrum

# SELECT AVG(salary) FROM makers WHERE position = 'Scrum';

#     ✅Вытащите имя и длину имён работников  в порядке
#     возрастания длин их имён

# select name, length(name) from makers order by length(name);

#     ✅Измените одну запись в таблице (любую)

# UPDATE makers SET salary=5000 WHERE menthor_id=9;

#     ✅Удалите одну запись из таблицы (любую)

# DELETE FROM makers WHERE salary < 2000;

#     ✅Удалите поле salary из таблицы

# ALTER TABLE makers DROP COLUMN salary;

#     ✅Переименуйте поле mentor_id на employee_id

# ALTER TABLE makers
# RENAME COLUMN menthor_id TO employee_id;

#1
# SELECT plaintext FROM wordform GROUP BY plaintext ORDER BY count(*) DESC LIMIT 10;
#2
# SELECT plaintext FROM wordform WHERE plaintext ILIKE 'a%';
#3
# SELECT title, genretype FROM work WHERE genretype = 'p';
#4
# SELECT AVG(totalparagraphs) FROM work WHERE genretype = 't';
#5
# SELECT title FROM work WHERE totalwords >=(SELECT AVG(totalwords) FROM work);
#6
# SELECT character.charname, speechcount, work.title FROM character LEFT JOIN character_work ON character.charid = character_work.charid LEFT JOIN work ON character_work.workid = work.workid
#7
