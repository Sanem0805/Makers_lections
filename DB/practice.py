# практика для блога

# create table blogger (
# id serial primary key,
# name varchar(50));

# create table post (
# id serial primary key,
# owner_id int references blogger(id),
# body text,
# created_at date);

# заполнение данных
# insert into blogger(name) values ('John'), ('Sultan'), ('Jamie');

# insert into post (owner_id, body, created_at) values (1, 'My first blog. Hello world!', '2023.02.24'), (1, 'Today is good day!', '2023.02.01'), (1, 'today is my bad day', '2022.03.05');

# insert into post (owner_id, body, created_at) values (3, 'Lanister is the best', '2023.02.01'), (3, 'I will be bakc', '2022.03.05');

# insert into post (owner_id, body, created_at) values (2, 'I\m good man', '2022.03.05');

# shoop
# create table customer (
# id serial primary key,
# name varchar(50));

# create table product (
# id serial primary key,
# title varchar(50),
# price decimal);

# create table card (
# id serial primary key,
# customer_id int references customer(id),
# product_id int references product(id));

# запонение таблиц
# insert into customer (name) values ('Sultan'), ('John'), ('Jamie');

# insert into product(title, price) values ('KKS', 340),
# ('Iphone 14', 70000),
# ('potato', 200),
# ('anas', 400),
# ('ice_cream', 120);

# insert into card(customer_id, product_id) values (1, 1), (1, 1), (1, 1), (1,3), (1, 3), (2, 2), (2, 2), (3, 4), (3, 5);
# group by разделяет данные которые мы получаем в select, приэтом групписруя их по определенному  признаку, и теперь для каждой группы можно использовать агрегатную функцию

# SELECT city , max(temp_hi), avg(prcp) from wearher group by city;

# HAVING: он работает так же как и WHERE, только  с опреатором GROUP BY

# АГРЕГАТНАЯ ФУНКЦИЯ
# SUM -функция которая считывает сумму всух записей в сгруппированном поле

# пример из shop
# select c.name, sum(p.price) as total_price from product as p join card on p.id=card.product_id join customer as c on c.id= card.customer_id group by c.name;

# select post.id , b.name, post.body, post.created_at from blogger as b, post where b.id=post.owner_id;

# ARRAY_AGG -объединяет записи сгрупированного поля в массив
# select b.name, ARRAY_AGG(post.body)  as post from blogger as b join post on b.id = post.owner_id group by b.name;

# select title, source totlparagraphs from work where source = 'Moby' and totalparagraphs < 100;

# 2.найти коль-во произведений 
# select count(*), work.title from chapter join work on work.workid=chapter.workid group by work.title order by count(*) desc limit 10;

# 3юнайти сколько произведений относяться к каждому жанру
# select count(*), genretype from work group by genretype order by count;

# 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений
# select title, total paragraphs from work;

# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания

# select ch.charname, ch.speechcount, work.title, work.genretype, work.year
# from character_work as ch_w 
# join character as ch on ch_w.charid = ch.charid 
# join work on ch_w.workid = work.workid
# where ch.speechcount > 200 order by work.year;

# select ch.charname, max(ch.speechcount), array_agg(work.title)
# from character_work as ch_w 
# join character as ch on ch_w.charid = ch.charid 
# join work on ch_w.workid = work.workid
# where ch.speechcount > 200 group by ch.charname order by max(ch.speechcount) desc limit 10;

# 6. Вытащить героя, который чаще всех появляется в произведениях
# select ch.charname, count(*) as works_count 
# from character_work as ch_w
# join character as ch  on ch.charid = ch_w.charid
# group by ch.charname order by works_count desc limit 1;


