def insert(connection):

    # =========== genre =============================
    genre = connection.execute("""
    INSERT INTO genre (name) VALUES ('Джаз');
    INSERT INTO genre (name) VALUES ('Кантри');
    INSERT INTO genre (name) VALUES ('Рок');
    INSERT INTO genre (name) VALUES ('Регги');
    INSERT INTO genre (name) VALUES ('Хип-хоп');
    INSERT INTO genre (name) VALUES ('Поп');
    """)
    print('genre==', genre)

    # =========== singer =============================
    singer = connection.execute("""
    INSERT INTO singer (name, pseudonym) VALUES ('Альберт Эйлер','Альберт Эйлер');
    INSERT INTO singer (name, pseudonym) VALUES ('Аллан Холдсуорт','Аллан Холдсуорт');
    INSERT INTO singer (name, pseudonym) VALUES ('Блу Митчелл','Блу Митчелл');

    INSERT INTO singer (name, pseudonym) VALUES ('Джонни Кэш','Джонни Кэш');
    INSERT INTO singer (name, pseudonym) VALUES ('Джордж Харви Стрейт','Джордж Харви Стрейт');
    INSERT INTO singer (name, pseudonym) VALUES ('The Rolling Stones','The Rolling Stones');

    INSERT INTO singer (name, pseudonym) VALUES ('Nirvana','Nirvana');
    INSERT INTO singer (name, pseudonym) VALUES ('Курт Кобейн','Курт Кобейн');
    INSERT INTO singer (name, pseudonym) VALUES ('Джордж Джонс','Джордж Джонс');

    INSERT INTO singer (name, pseudonym) VALUES ('Bob Marley','Bob Marley');
    INSERT INTO singer (name, pseudonym) VALUES ('Sublime','Sublime');
    INSERT INTO singer (name, pseudonym) VALUES ('Sean Paul','Sean Paul');

    INSERT INTO singer (name, pseudonym) VALUES ('Kanye West','Kanye West');
    INSERT INTO singer (name, pseudonym) VALUES ('Gorillaz','Gorillaz');
    INSERT INTO singer (name, pseudonym) VALUES ('Black Eyed Peas','Black Eyed Peas');

    INSERT INTO singer (name, pseudonym) VALUES ('Michael Jackson','Michael Jackson');
    INSERT INTO singer (name, pseudonym) VALUES ('Madonna','Madonna');
    INSERT INTO singer (name, pseudonym) VALUES ('The Beatles','The Beatles')
    """)
    print('singer==', singer)

    # =========== singer_genre =============================
    singer_genre = connection.execute("""
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (1, 1);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (2, 1);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (3, 1);

    INSERT INTO singer_genre (singer_id, genre_id) VALUES (4, 2);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (5, 2);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (6, 2);

    INSERT INTO singer_genre (singer_id, genre_id) VALUES (7, 3);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (8, 3);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (9, 3);

    INSERT INTO singer_genre (singer_id, genre_id) VALUES (10, 4);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (11, 4);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (12, 4);

    INSERT INTO singer_genre (singer_id, genre_id) VALUES (13, 5);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (14, 5);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (15, 5);

    INSERT INTO singer_genre (singer_id, genre_id) VALUES (16, 5);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (17, 5);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (18, 5);

    INSERT INTO singer_genre (singer_id, genre_id) VALUES (19, 6);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (20, 6);
    INSERT INTO singer_genre (singer_id, genre_id) VALUES (21, 6);
    """)
    print('singer_genre==', singer_genre)

    # =========== album =============================

    album = connection.execute("""
    INSERT INTO album (name, year) VALUES ('album 1', 2012);
    INSERT INTO album (name, year) VALUES ('album 2', 2013);
    INSERT INTO album (name, year) VALUES ('album 3', 2012);
    INSERT INTO album (name, year) VALUES ('album 4', 2014);
    INSERT INTO album (name, year) VALUES ('album 5', 2012);
    INSERT INTO album (name, year) VALUES ('album 6', 2015);
    INSERT INTO album (name, year) VALUES ('album 7', 2015);
    INSERT INTO album (name, year) VALUES ('album 8', 2016);
    INSERT INTO album (name, year) VALUES ('album 9', 2012);
    INSERT INTO album (name, year) VALUES ('album 10', 2018);
    INSERT INTO album (name, year) VALUES ('album 11', 2018);
    INSERT INTO album (name, year) VALUES ('album 12', 2018);
    INSERT INTO album (name, year) VALUES ('album 13', 2018);
    INSERT INTO album (name, year) VALUES ('album 14', 2019);
    INSERT INTO album (name, year) VALUES ('album 15', 2020);
    INSERT INTO album (name, year) VALUES ('album 16', 2021);
    """)
    print('album==', album)

    # =========== singer_albums =============================
    singer_albums = connection.execute("""
    INSERT INTO singer_albums (album_id, singer_id) VALUES (1, 1);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (1, 2);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (1, 3);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (2, 2);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (2, 3);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (1, 4);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (3, 4);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (4, 4);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (5, 5);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (6, 6);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (7, 7);
    INSERT INTO singer_albums (album_id, singer_id) VALUES (8, 8);
    """)
    print('singer_albums==', singer_albums)

    # =========== track =============================
    track = connection.execute("""
    INSERT INTO track (album_id, name, duration) VALUES (1, 'track 1', 4);
    INSERT INTO track (album_id, name, duration) VALUES (1, 'track 2', 4);
    INSERT INTO track (album_id, name, duration) VALUES (1, 'track 3', 4);
    INSERT INTO track (album_id, name, duration) VALUES (1, 'track 4', 4);
    INSERT INTO track (album_id, name, duration) VALUES (1, 'track 5', 4);
    INSERT INTO track (album_id, name, duration) VALUES (2, 'track 200', 4);
    INSERT INTO track (album_id, name, duration) VALUES (2, 'track 201', 4);
    INSERT INTO track (album_id, name, duration) VALUES (2, 'track 202', 4);
    INSERT INTO track (album_id, name, duration) VALUES (2, 'track 203', 4);
    INSERT INTO track (album_id, name, duration) VALUES (3, 'track 301', 4);
    INSERT INTO track (album_id, name, duration) VALUES (3, 'track 302', 4);
    INSERT INTO track (album_id, name, duration) VALUES (3, 'track 303', 4);
    INSERT INTO track (album_id, name, duration) VALUES (4, 'track 401', 4);
    INSERT INTO track (album_id, name, duration) VALUES (4, 'track 402', 4);
    INSERT INTO track (album_id, name, duration) VALUES (4, 'track 403', 4);
    INSERT INTO track (album_id, name, duration) VALUES (4, 'track 404', 4);
    INSERT INTO track (album_id, name, duration) VALUES (5, 'track 501', 4);
    INSERT INTO track (album_id, name, duration) VALUES (5, 'track 502', 4);
    INSERT INTO track (album_id, name, duration) VALUES (5, 'track 503', 4);
    INSERT INTO track (album_id, name, duration) VALUES (5, 'track 504', 4);
    INSERT INTO track (album_id, name, duration) VALUES (6, 'track 601', 4);
    INSERT INTO track (album_id, name, duration) VALUES (6, 'track 602', 4);
    INSERT INTO track (album_id, name, duration) VALUES (7, 'track 701', 4);
    INSERT INTO track (album_id, name, duration) VALUES (7, 'track 702', 4);
    INSERT INTO track (album_id, name, duration) VALUES (8, 'track 801', 4);
    INSERT INTO track (album_id, name, duration) VALUES (8, 'track 802', 4);
    INSERT INTO track (album_id, name, duration) VALUES (9, 'track 901', 4);
    INSERT INTO track (album_id, name, duration) VALUES (9, 'track 902', 4);
    INSERT INTO track (album_id, name, duration) VALUES (10, 'track 101', 4);
    INSERT INTO track (album_id, name, duration) VALUES (10, 'track 102', 4);
    INSERT INTO track (album_id, name, duration) VALUES (11, 'track 110', 4);
    INSERT INTO track (album_id, name, duration) VALUES (11, 'track 112', 4);
    INSERT INTO track (album_id, name, duration) VALUES (12, 'track 120', 4);
    INSERT INTO track (album_id, name, duration) VALUES (12, 'track 122', 4);
    INSERT INTO track (album_id, name, duration) VALUES (13, 'track 13', 4);
    INSERT INTO track (album_id, name, duration) VALUES (13, 'track 1313', 4);
    INSERT INTO track (album_id, name, duration) VALUES (14, 'track 14', 4);
    INSERT INTO track (album_id, name, duration) VALUES (14, 'track 1414', 4);
    INSERT INTO track (album_id, name, duration) VALUES (15, 'track 15', 4);
    INSERT INTO track (album_id, name, duration) VALUES (15, 'track 1515', 4);
    INSERT INTO track (album_id, name, duration) VALUES (16, 'track 16', 4);
    INSERT INTO track (album_id, name, duration) VALUES (16, 'track 1616', 4);
    """)
    print('track==', track)

    # =========== collection ============================= 

    collection = connection.execute("""
    INSERT INTO collection (name, year) VALUES ('collection 1', 2021);
    INSERT INTO collection (name, year) VALUES ('collection 2', 2020);
    INSERT INTO collection (name, year) VALUES ('collection 3', 2018);
    INSERT INTO collection (name, year) VALUES ('collection 4', 2021);
    INSERT INTO collection (name, year) VALUES ('collection 5', 2019);
    INSERT INTO collection (name, year) VALUES ('collection 6', 2018);
    INSERT INTO collection (name, year) VALUES ('collection 7', 2019);
    INSERT INTO collection (name, year) VALUES ('collection 8', 2020);
    INSERT INTO collection (name, year) VALUES ('collection 9', 2018);
    INSERT INTO collection (name, year) VALUES ('collection 10', 2020);
    INSERT INTO collection (name, year) VALUES ('collection 11', 2018);
    INSERT INTO collection (name, year) VALUES ('collection 12', 2019);
    """)
    print('collection==', collection)


    # =========== track_collection ============================= 

    track_collection = connection.execute("""
    INSERT INTO track_collection (collection_id, track_id) VALUES (1, 1);
    INSERT INTO track_collection (collection_id, track_id) VALUES (1, 2);
    INSERT INTO track_collection (collection_id, track_id) VALUES (1, 3);
    INSERT INTO track_collection (collection_id, track_id) VALUES (2, 4);
    INSERT INTO track_collection (collection_id, track_id) VALUES (2, 5);
    INSERT INTO track_collection (collection_id, track_id) VALUES (2, 6);
    INSERT INTO track_collection (collection_id, track_id) VALUES (3, 7);
    INSERT INTO track_collection (collection_id, track_id) VALUES (3, 8);
    INSERT INTO track_collection (collection_id, track_id) VALUES (3, 9);
    INSERT INTO track_collection (collection_id, track_id) VALUES (4, 10);
    INSERT INTO track_collection (collection_id, track_id) VALUES (4, 11);
    INSERT INTO track_collection (collection_id, track_id) VALUES (4, 12);
    INSERT INTO track_collection (collection_id, track_id) VALUES (5, 13);
    INSERT INTO track_collection (collection_id, track_id) VALUES (5, 14);
    INSERT INTO track_collection (collection_id, track_id) VALUES (5, 15);
    INSERT INTO track_collection (collection_id, track_id) VALUES (6, 16);
    INSERT INTO track_collection (collection_id, track_id) VALUES (6, 17);
    INSERT INTO track_collection (collection_id, track_id) VALUES (6, 18);
    INSERT INTO track_collection (collection_id, track_id) VALUES (7, 19);
    INSERT INTO track_collection (collection_id, track_id) VALUES (7, 20);
    INSERT INTO track_collection (collection_id, track_id) VALUES (7, 21);
    INSERT INTO track_collection (collection_id, track_id) VALUES (8, 22);
    INSERT INTO track_collection (collection_id, track_id) VALUES (8, 23);
    INSERT INTO track_collection (collection_id, track_id) VALUES (8, 24);
    INSERT INTO track_collection (collection_id, track_id) VALUES (9, 25);
    INSERT INTO track_collection (collection_id, track_id) VALUES (9, 26);
    INSERT INTO track_collection (collection_id, track_id) VALUES (9, 27);
    INSERT INTO track_collection (collection_id, track_id) VALUES (10, 28);
    INSERT INTO track_collection (collection_id, track_id) VALUES (10, 29);
    INSERT INTO track_collection (collection_id, track_id) VALUES (10, 30);
    INSERT INTO track_collection (collection_id, track_id) VALUES (11, 31);
    INSERT INTO track_collection (collection_id, track_id) VALUES (11, 32);
    INSERT INTO track_collection (collection_id, track_id) VALUES (11, 33); 
    INSERT INTO track_collection (collection_id, track_id) VALUES (12, 34);
    INSERT INTO track_collection (collection_id, track_id) VALUES (12, 35);
    INSERT INTO track_collection (collection_id, track_id) VALUES (12, 36);
    """)
    print('track_collection==', track_collection)