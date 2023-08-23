#!/usr/bin/python3
"""
unittests to test setup_mysql_test.sql
"""
import unittest
import subprocess
import pymysql

class TestMySQLSetup(unittest.TestCase):
    """
    class to test setup_mysql_test.sql
    """
    @classmethod
    def setUpClass(cls):
        subprocess.run(['mysql', '-hlocalhost', '-uroot', '-p', '<',
			'setup_mysql_test.sql'], text=True, input='password')
        cls.connection = pymysql.connect(
            host='localhost',
            user='hbnb_test',
            password='hbnb_test_pwd',
            db='hbnb_test_db'
        )

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def test_database_exists(self):
        cursor = self.connection.cursor()
        cursor.execute("SHOW DATABASES LIKE 'hbnb_test_db';")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
    
    def test_user_exists(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT user FROM mysql.user WHERE user='hbnb_test';")
        result = cursor.fetchone()
        self.assertIsNotNone(result)

    def test_user_privileges(self):
        cursor = self.connection.cursor()
        cursor.execute("SHOW GRANTS FOR 'hbnb_test'@'localhost';")
        grants = cursor.fetchall()
        self.assertIn("ALL PRIVILEGES ON `hbnb_test_db`.*", grants)
        self.assertIn("SELECT ON `performance_schema`.*", grants)

if __name__ == '__main__':
    unittest.main()
