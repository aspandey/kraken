import unittest
from main import app

class TestApp(unittest.TestCase):
    def test_hello_route(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello from Flask!', response.data)

if __name__ == '__main__':
    unittest.main()
