# ORM(object-Relation Mapping) - техноглогия программирования, благодаря которой разработчики могут использовать язык программирования для взаимодействия  среляционной базо1 данных (PostgresSQL, MySQL, OraclDB).
# вместо того чтобы писать сырые запросы на опрераторах SQL, вы будите писать код ООП на языке программирования . Это очень сильно ускоряет разроботку приложения и бд, особенно на начальных этапах

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database='orm_db',
    user='sanem0805',
    password='1',
    host='localhost',
    port=5432
)
# db.connect()