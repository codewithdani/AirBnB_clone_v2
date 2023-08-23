#!/usr/bin/python3
"""
unittests for setup_mysql_dev.sql
""" 
import unittest
import pymysql


class TestSetupMySQLDevScript(unittest.TestCase):
    """
    class that tests setup_mysql_dev
    """

    def setUp(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='your_mysql_user',
            password='your_mysql_password',
            database='hbnb_dev_db',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def tearDown(self):
        self.connection.close()

    def test_states_table_exists(self):
        cursor = self.connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'states';")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        
    def test_states_table_columns(self):
        cursor = self.connection.cursor()
        cursor.execute("DESCRIBE states;")
        columns = [row['Field'] for row in cursor.fetchall()]
        expected_columns = ['id', 'created_at', 'updated_at', 'name']
        self.assertEqual(columns, expected_columns)

    def test_cities_table_exists(self):
        cursor = self.connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'cities';")
        result = cursor.fetchone()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
