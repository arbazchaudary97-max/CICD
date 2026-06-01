import unittest

from hello import say_hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assetEqua(say_hello(), "Hello, World!")