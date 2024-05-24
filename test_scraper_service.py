import unittest
import requests

class TestScraperService(unittest.TestCase):
    def test_scrape_phaidra_ai(self):
        url = "http://phaidra.ai"
        response = requests.post("http://localhost:8080", json={"url": url})
        data = response.json()
        self.assertEqual(data['url'], url)
        self.assertIn('status_code', data)
        self.assertIsInstance(data['status_code'], int)

    def test_scrape_trackrecord(self):
        url = "https://phaidra.ai/trackrecord"
        response = requests.post("http://localhost:8080", json={"url": url})
        data = response.json()
        self.assertEqual(data['url'], url)
        self.assertIn('status_code', data)
        self.assertIsInstance(data['status_code'], int)

    def test_scrape_google(self):
        url = "https://google.com"
        response = requests.post("http://localhost:8080", json={"url": url})
        data = response.json()
        self.assertEqual(data['url'], url)
        self.assertIn('status_code', data)
        self.assertIsInstance(data['status_code'], int)

    def test_metrics_endpoint(self):
        response = requests.get("http://localhost:9095/metrics")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
