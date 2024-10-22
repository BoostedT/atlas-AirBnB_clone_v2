#!/usr/bin/python3
"""Unittest for DBStorage class"""
import unittest
import os
import MySQLdb
from datetime import datetime

from models import storage
from models.user import User

import unittest
import os
import MySQLdb
from datetime import datetime
from your_storage_module import DBStorage
from your_user_module import User

class TestDBStorage(unittest.TestCase):

    def setUp(self):
        self.dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cursor = self.dbc.cursor()

    def tearDown(self):
        self.cursor.close()
        self.dbc.close()

    def test_new(self):
        new = User(
            email='johndoe@gmail.com',
            password='password',
            first_name='John',
            last_name='doe'
        )
        self.assertFalse(new in storage.all())
        new.save()
        self.assertTrue(new in storage.all())
        self.cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = self.cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('john2020@gmail.com', result)

    def test_delete(self):
        new = User(
            email='johndoe@gmail.com',
            password='password',
            first_name='John',
            last_name='doe'
        )
        new.save()
        obj_key = f'User.{new.id}'
        self.assertIn(obj_key, storage.all(User))
        new.delete()
        self.assertNotIn(obj_key, storage.all(User))

    def test_reload(self):
        self.cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password, first_name, last_name) ' +
            'VALUES(%s, %s, %s, %s, %s, %s, %s);',
            ['4447-by-me', str(datetime.now()), str(datetime.now()), 'ben_pike@yahoo.com', 'pass', 'Benjamin', 'Pike']
        )
        self.dbc.commit()
        storage.reload()
        self.assertIn('User.4447-by-me', storage.all())

    def test_save(self):
        new = User(
            email='johndoe@gmail.com',
            password='password',
            first_name='John',
            last_name='doe'
        )
        new.save()
        self.cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = self.cursor.fetchone()
        self.assertTrue(result is not None)

    def test_storage_var_created(self):
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)

if __name__ == '__main__':
    unittest.main()
