def drop_tables(connection):
    genre = connection.execute("""
    DROP TABLE IF EXISTS genre;
    """)
    print('genre==', genre)

    singer = connection.execute("""
    DROP TABLE singer;
    """)
    print('singer==', singer)

    singer_genre = connection.execute("""
    DROP TABLE IF EXISTS  singer_genre;
    """)
    print('singer_genre==', singer_genre)


    album = connection.execute("""
    DROP TABLE IF EXISTS album;
    """)
    print('album==', album)


    singer_albums = connection.execute("""
    DROP TABLE IF EXISTS singer_albums;
    """)
    print('singer_albums==', singer_albums)

    track = connection.execute("""
    DROP TABLE track;
    """)
    print('track==', track)


    collection = connection.execute("""
    DROP TABLE IF EXISTS collection;
    """)
    print('collection==', collection)

    track_collection = connection.execute("""
    DROP TABLE IF EXISTS track_collection;
    """)
    print('track_collection==', track_collection)