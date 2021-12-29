from app import connex_app
import directors
import movies
import unittest
import json


class DirectorsUnitTest(unittest.TestCase):
    def test_read_all_directors(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/directors?limit=3')
        self.assertEqual(response.status_code, 200)

    def test_post_directors(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        mock_data = {
            "department": "Test Department",
            "gender": 2,
            "name": "Test Name",
            "uid": 40404
        }
        response = tester.post(
            '/api/directors', data=json.dumps(mock_data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_read_once_directors(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/directors/7111')
        self.assertEqual(response.status_code, 200)

    def test_update_directors(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        mock_data = {
            "department": "Update Department",
            "gender": 1,
            "name": "Update Name",
            "uid": 40405
        }
        response = tester.put(
            '/api/directors/7111', data=json.dumps(mock_data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
    
    def test_seacrh_director_name(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/directors/search/James?limit=2')
        self.assertEqual(response.status_code, 200)
    
    def test_most_movies_director(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/directors/mostmovies?limit=3&director_sort=desc')
        self.assertEqual(response.status_code, 200)


class DirectorsDeleteUnitTest(unittest.TestCase):
    def test_delete_director(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.delete('/api/directors/7111')
        self.assertEqual(response.status_code, 200)


if (__name__ == '__main__'):
    unittest.main()
