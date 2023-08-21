from sqlalchemy import delete, insert, select, update
from db import PostModel


class PostsFacade:
    def __init__(self, engine_db):
        self.__connection = engine_db.connect()
        self.__model = PostModel

    def get_all_posts(self):
        query = select(self.__model)
        cursor = self.__connection.execute(query)
        return cursor.mappings().all()

    def get_post(self, id_):
        query = select(self.__model).where(self.__model.id == id_)
        cursor = self.__connection.execute(query)
        return cursor.mappings().one()

    def update_post(self, id_, title, content):
        query = update(self.__model).where(self.__model.id == id_).values(title=title, content=content)
        self.__connection.execute(query)
        self.__connection.commit()

    def create_post(self, title, content):
        query = insert(self.__model).values(title=title, content=content)
        self.__connection.execute(query)
        self.__connection.commit()

    def remove_post(self, id_):
        query = delete(self.__model).where(self.__model.id == id_)
        self.__connection.execute(query)
        self.__connection.commit()