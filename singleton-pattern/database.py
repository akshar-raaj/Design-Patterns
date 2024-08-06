class Database(object):
    _connection = None

    def __init__(self):
        self.num_queries = 0
        if Database._connection is not None:
            raise Exception("Database already initialized")
        else:
            Database._connection = self

    def execute_query(self, query):
        self.num_queries += 1
        print("Executing query")

    @staticmethod
    def get_connection():
        if Database._connection is None:
            Database._connection = Database()
        return Database._connection
