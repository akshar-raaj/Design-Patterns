class Database(object):
    _connection = None

    def __init__(self):
        if Database._connection is not None:
            raise Exception("Database already initialized")
        else:
            Database._connection = self

    @staticmethod
    def get_connection():
        if Database._connection is None:
            Database._connection = Database()
        return Database._connection
