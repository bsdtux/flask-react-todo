# project/tests/test_config.py
import os
import unittest

from flask_testing import TestCase

from api import create_app
from api.config import BASE_DIR


class TestDevelopmentConfig(TestCase):
    def setUp(self):
        self.app = self.create_app()

    def create_app(self):
        return create_app('development')

    def test_app_is_development(self):
        self.assertTrue(self.app.config['DEBUG'])
        self.assertTrue(self.app.config['TESTING'] is False)

        db_path = f"sqlite:///{os.path.join(BASE_DIR, '../db/dev_db.sqlite')}"
        self.assertEqual(self.app.config['SQLALCHEMY_DATABASE_URI'], db_path)


class TestTestingConfig(TestCase):
    def setUp(self):
        self.app = self.create_app()

    def create_app(self):
        return create_app('testing')

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['DEBUG'])
        self.assertTrue(self.app.config['TESTING'])

        db_path = f"sqlite:///{os.path.join(BASE_DIR, '../db/testing_db.sqlite')}"
        self.assertEqual(self.app.config['SQLALCHEMY_DATABASE_URI'], db_path)


class TestProductionConfig(TestCase):
    def setUp(self):
        self.app = self.create_app()

    def create_app(self):
        return create_app('production')

    def test_app_is_production(self):
        self.assertTrue(self.app.config['DEBUG'] is False)
        self.assertTrue(self.app.config['TESTING'] is False)

        db_path = f"sqlite:///{os.path.join(BASE_DIR, '../db/production_db.sqlite')}"
        self.assertEqual(self.app.config['SQLALCHEMY_DATABASE_URI'], db_path)


if __name__ == '__main__':
    unittest.main()