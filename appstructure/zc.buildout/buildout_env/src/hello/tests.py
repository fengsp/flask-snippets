# -*- coding: utf-8 -*-
import unittest
import hello


class HelloTestCase(unittest.TestCase):
    
    def setUp(self):
        """Before each test, set up a blank database"""
        self.app = hello.app.test_client()
        hello.init_db()

    def tearDown(self):
        """Get rid of the database again after each test."""
        pass

    def test_hello(self):
        """Test rendered page."""
        hello.app.config['USERNAME'] = 'jean'
        rv = self.app.get('/')
        assert 'Hello Jean!' in rv.data


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(HelloTestCase))
    return suite


if __name__ == "__main__":
    unittest.main()
