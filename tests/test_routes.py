from unittest import TestCase
from microblog import app


class Test(TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_index(self):
        ret = self.app.get("/", follow_redirects=False)
        if ret.status_code != 200:
            self.fail()
