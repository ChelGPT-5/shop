import psycopg2


def get_connect(db_name):
    connect = psycopg2.connect(dbname='blog', host='127.0.0.1', port='5432', user='postgres', password='12345')

    return connect

with get_connect('blog') as conn:
    with conn.cursor() as cursor:
        cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS posts(
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)
        """
        )
        conn.commit()
        cursor.execute("""INSERT INTO posts (title, content) VALUES ('title1', 'content1'), ('title2', 'content2')""")
        conn.commit()