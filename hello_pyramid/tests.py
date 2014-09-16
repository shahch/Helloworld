import unittest

from webtest import TestApp

from pyramid.paster import get_app
from pyramid import testing


class ViewTests(unittest.TestCase):

    def setUp(self):
       app = get_app('testing.ini')
       self.testapp = TestApp(app)

    def tearDown(self):

       del self.testapp
       #self.driver.close()
    def test_root(self):
       res = self.testapp.get('/')
       # <h1><span class="font-semi-bold">Hello</span> <span class="font-semi-bold">world</span></h1><span class="small">By Chirag Shah</span>
       self.assertTrue(b' <h1><span class="font-semi-bold">Hello</span> <span class="font-semi-bold">world</span></h1><span class="small">By Chirag Shah</span>' in res.body) #Make sure there is remember me checkbox
       