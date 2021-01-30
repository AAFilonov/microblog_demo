import ast
from unittest import TestCase
from unittest.mock import *

from microblog import app

"""
 Разбираем AST wsgi.py
 выбираем все декораторы app.route и собираем все маршруты. 
"""


class Walker(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        # print("Instance",repr(node.name),"\n\t",ast.dump(node))
        for d in node.decorator_list:
            # print("Found Decorator",ast.dump(d))
            if d.func.value.id == 'app' and d.func.attr == 'route':
                # print("Found route to",repr(d.args[0].s))
                # print(repr(d.args[0].s))
                self.ret_value.append(d.args[0].s)
        # мы не будем обходить вложенные функции
        # ast.NodeVisitor.generic_visit(self, node)


class Test_Flask(TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def tearDown(self):
        pass

    def get_routes(self, fname):
        walker = Walker()
        walker.ret_value = []
        with open(fname, "r") as f:
            code = f.read()
        wast = ast.parse(code)
        # print(ast.dump(wast))
        walker.visit(wast)
        return walker.ret_value

    #@patch('logger.app_logger.error')
    #@patch('logger.app_logger.info')

    def test_all_routes(self):
        routes = self.get_routes("microblog.py")
        # проверяем что нет неучтенных "500"
        for uri in routes:
            ret = self.app.get(uri, follow_redirects=False)
            if ret.status_code >= 500:
                self.assertTrue(ret.data.startswith(
                    b'<html><head><title>Error</title></head><body><pre>'))

        # print(repr(mock_log_error.mock_calls))
