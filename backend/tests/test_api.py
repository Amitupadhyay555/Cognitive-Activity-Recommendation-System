
# tests/test_api.py

import unittest
import requests

class TestCognitiveActivityAPI(unittest.TestCase):

    BASE_URL = "http://localhost:5000/recommendations"  # or your deployed URL

    def test_get_recommendations(self):
        response = requests.get(self.BASE_URL, params={"category": "Memory"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", response.json()[0])

    def test_invalid_category(self):
        response = requests.get(self.BASE_URL, params={"category": "Invalid"})
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
