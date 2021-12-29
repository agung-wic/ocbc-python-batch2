from app import connex_app
import people
import notes
import unittest
import json

class FlaskUnitTest(unittest.TestCase):
    def test_get_people_response(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/people')
        self.assertEqual(response.status_code, 200)
    
    # def test_post_people_response(self):
    #     connex_app.app.testing = True
    #     tester = connex_app.app.test_client(self)
    #     mock_data = {
    #         'fname': 'Agung',
    #         'lname': 'Wicaksono'
    #     }
    #     response = tester.post('/api/people', data=json.dumps(mock_data), content_type="application/json")
    #     self.assertEqual(response.status_code, 201)
    
    # def test_put_people_response(self):
    #     connex_app.app.testing = True
    #     tester = connex_app.app.test_client(self)
    #     mock_data = {
    #         'fname': 'Agung',
    #         'lname': 'Laksono'
    #     }
    #     response = tester.put('/api/people/4', data=json.dumps(mock_data), content_type="application/json")
    #     self.assertEqual(response.status_code, 200)

    def test_delete_people_response(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.delete('/api/people/4')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()