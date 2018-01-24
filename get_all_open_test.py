import unittest
import responses
import requests
from AttResource import get_all_open_issues

class AttResouceTest(unittest.TestCase):
    def test_open_issues_url(self):
        s = get_all_open_issues()
        self.assertRaises(Exception)

        def test_self(self):
         self.assertEqual(True, False)

    @responses.activate
    def test_error(self):
        responses.add(**{
        'method': responses.GET,
        'url': 'https://api.github.com/orgs/att/repos?type=public',
        'body': '{"error": "Exceeded max limit"}',
        'status': 404,
        'content_type': 'application/json'
    })

        response = requests.get('https://api.github.com/orgs/att/repos?type=public"')
        self.assertEqual({'error': 'Exceeded max limit'}, response.json())
        self.assertEqual(404, response.status_code)

if __name__ == '__main__':
    unittest.main()


