from app import connex_app
import directors
import movies
import unittest
import json


class MoviesUnitTest(unittest.TestCase):
    def test_read_all_movies_id(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/movies?limit=10')
        self.assertEqual(response.status_code, 200)
    
    def test_read_all_movies_budget(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/movies?limit=10&movie_sort=desc&sorted_by=budget')
        self.assertEqual(response.status_code, 200)
    
    def test_read_all_movies_popularity(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/movies?limit=10&movie_sort=asc&sorted_by=popularity')
        self.assertEqual(response.status_code, 200)
    
    def test_read_all_movies_revenue(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/movies?limit=10&movie_sort=asc&sorted_by=revenue')
        self.assertEqual(response.status_code, 200)

    def test_read_all_movies_vote_count(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/movies?limit=10&movie_sort=asc&sorted_by=vote%20count')
        self.assertEqual(response.status_code, 200)
    
    def test_read_all_movies_vote_average(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/movies?limit=10&movie_sort=asc&sorted_by=vote%20average')
        self.assertEqual(response.status_code, 200)

    def test_seacrh_movie_name(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/movies/search/The%20Cat')
        self.assertEqual(response.status_code, 200)

    def test_post_movies(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        mock_data = {
            "budget": 1000,
            "original_title": "Test Original Title",
            "overview": "Test Overview",
            "popularity": 1000,
            "release_date": "2016-09-10",
            "revenue": 1000,
            "tagline": "Test tagline",
            "title": "Test Title",
            "uid": 40404,
            "vote_average": 8.8,
            "vote_count": 1000
        }
        response = tester.post(
            '/api/directors/4762/movies', data=json.dumps(mock_data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_read_once_movies(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/directors/4762/movies/48400')
        self.assertEqual(response.status_code, 200)

    def test_update_movies(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        mock_data = {
            "budget": 2000,
            "original_title": "Test2 Original Title",
            "overview": "Test2 Overview",
            "popularity": 2000,
            "release_date": "2017-09-10",
            "revenue": 2000,
            "tagline": "Test2 tagline",
            "title": "Test2 Title",
            "uid": 40404,
            "vote_average": 9.9,
            "vote_count": 2000
        }
        response = tester.put(
            '/api/directors/4762/movies/48400', data=json.dumps(mock_data), content_type="application/json")
        self.assertEqual(response.status_code, 200)


class MoviesDeleteUnitTest(unittest.TestCase):
    def test_delete_movies(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.delete('/api/directors/4762/movies/48400')
        self.assertEqual(response.status_code, 200)


if (__name__ == '__main__'):
    unittest.main()
