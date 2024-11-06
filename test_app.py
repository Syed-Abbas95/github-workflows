import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        # Test the '/' route
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), "Hello world")
        self.assertEqual(response.status_code, 200)

    def test_hello_aditya(self):
        # Test the '/hello' route
        response = self.app.get('/hello')
        self.assertIn("Hello Abbas, You have visited the page for", response.data.decode())
        self.assertEqual(response.status_code, 200)

        # Test multiple visits
        response = self.app.get('/hello')
        self.assertIn("Hello Abbas, You have visited the page for", response.data.decode())

if __name__ == "__main__":
    unittest.main()