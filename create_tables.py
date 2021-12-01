def create_tables(connection):

    genre = connection.execute("""
    CREATE table IF NOT EXISTS genre(
  		id serial PRIMARY KEY,  
  		name varchar(100) not null unique);
    """)
    print('genre==', genre)
    
    singer = connection.execute("""
    CREATE table IF NOT EXISTS singer(
  		id serial PRIMARY KEY,  
  		name varchar(100) not null,
		pseudonym varchar(100) not null);
    """)
    print('singer==', singer)

    singer_genre = connection.execute("""
    CREATE table IF NOT EXISTS singer_genre(
  		id serial PRIMARY KEY,  
  		singer_id integer references singer(id),
        genre_id integer references genre(id));	
    """)
    print('singer_genre==', singer_genre)

    album = connection.execute("""
    CREATE table IF NOT EXISTS album(
  		id serial PRIMARY KEY,  
  		name varchar(100) not null,
		year numeric not null);	
    """)
    print('album==', album)


    singer_albums = connection.execute("""
    CREATE table IF NOT EXISTS singer_albums(
        id serial PRIMARY KEY,
  		album_id integer references album(id),
        singer_id integer references singer(id));	
    """)
    print('singer_albums==', singer_albums)

    track = connection.execute("""
    CREATE table IF NOT EXISTS track(
        id serial PRIMARY KEY,  
        album_id integer references album(id),
  		name varchar(100) not null,
		duration integer not null);
    """)
    print('track==', track)


    collection = connection.execute("""
    CREATE table IF NOT EXISTS collection(
        id serial PRIMARY KEY,  
  		name varchar(100) not null,
		year numeric not null);
    """)
    print('collection==', collection)

    track_collection = connection.execute("""
    CREATE table IF NOT EXISTS track_collection(
        id serial PRIMARY KEY, 
        collection_id integer references collection(id),  
        track_id integer references track(id));
    """)
    print('track_collection==', track_collection)
     




