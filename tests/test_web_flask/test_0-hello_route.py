#!/usr/bin/python3
"""
Unit Test for api v1 Flask App
"""
import inspect
import pep8
import web_flask
import unittest


class TestHelloRouteDocs(unittest.TestCase):
    """Class for testing Hello Route docs"""

    all_funcs = inspect.getmembers(web_flask.0-hello_route, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........  Hello Route  ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        actual = app.__doc__
        self.assertIsNotNone(actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions"""
        all_functions = TestHelloRouteDocs.all_funcs
        for function in all_functions:
            self.assertIsNotNone(function[1].__doc__)

    def test_pep8_hello_route(self):
        """... hello_route.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['web_flask/0-hello_route.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main
