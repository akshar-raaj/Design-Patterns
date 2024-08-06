import pytest

from database import Database


def test_init():
    # Database is a Singleton class
    # Second invocation of __init__ must raise an exception
    Database()

    with pytest.raises(Exception):
        Database()


def test_get_connection():
    c1 = Database.get_connection()
    c2 = Database.get_connection()

    # Assert that both calls to get_connection return the same object
    assert c1 == c2


def test_execute_query():
    c = Database.get_connection()
    c.execute_query("SELECT 1;")
    assert c.num_queries == 1

    c2 = Database.get_connection()
    c2.execute_query("SELECT 2;")
    assert c.num_queries == 2
    assert c2.num_queries == 2
