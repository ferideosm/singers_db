import sqlalchemy
from create_tables import create_tables
from drop_tables import drop_tables


def sql(connection):

    tsk_1 = connection.execute("""
    SELECT name, year 
    FROM album 
    WHERE year = 2018;
    """)
    print('tsk_1==', tsk_1)

    tsk_2 = connection.execute("""
    SELECT name, duration 
    FROM track 
    WHERE MAX(duration);
    """)
    print('tsk_2==', tsk_2)


    tsk_3 = connection.execute("""
    SELECT name 
    FROM track 
    WHERE duration >= 3.5;
    """)
    print('tsk_3==', tsk_3)

    tsk_4 = connection.execute("""
    SELECT name 
    FROM collection 
    WHERE year between 2018 and 2020; 
    """)
    print('tsk_4==', tsk_4)

    tsk_5 = connection.execute("""
    SELECT name 
    FROM singer 
    WHERE COUNT(name) = 1; 
    """)
    print('tsk_5==', tsk_5)

    tsk_6 = connection.execute("""
    SELECT name 
    FROM track 
    WHERE name LIKE '%%my%%' or name LIKE '%%мой%%'; 
    """)
    print('tsk_6==', tsk_6)


if __name__ == '__main__':
    engine = sqlalchemy.create_engine('postgresql://feride:123456:5432/singers')
    # engine = sqlalchemy.create_engine('postgresql://feride:f:5432/singers')
    connection = engine.connect()

    drop_tables(connection)
    create_tables(connection)
    sql(connection)