from app import app
import json
import unittest

class FlaskTestCases(unittest.TestCase):
    def test_booking_ticket(self):
        tester = app.test_client(self)
        response = tester.post(
            '/book', data=json.dumps(dict(user_name='dkajfb', timings='12:00', phone_no=5428795213)),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = eval(response.data)
        self.assertEqual(data['user_name'], 'dkajfb')
        self.assertEqual(data['phone_no'], 5428795213)
    
    def test_get_all_tickets(self):
        tester = app.test_client(self)
        response = tester.get('/tickets')
        self.assertEqual(response.status_code, 200)
        data = eval(response.data)
        initial_ticket_count = len(data)
        tester.post(
            '/book',
            data=json.dumps(dict(user_name='dkajfb', timings='12:00', phone_no=7894526425)),
            content_type='application/json')
        response = tester.get('/tickets')
        self.assertEqual(response.status_code, 200)
        data = eval(response.data)
        self.assertEqual(len(data), initial_ticket_count+1)
    
    def test_delete_ticket_from_id(self):
        tester = app.test_client(self)
        response = tester.get('/tickets')
        self.assertEqual(response.status_code, 200)
        data = eval(response.data)
        test_id = data[0]['id']
        tester.delete('/ticket/'+test_id)
        response = tester.get('/ticket/'+test_id)
        data = eval(response.data)
        self.assertEqual(data, {})
    
    def test_get_ticket_from_id(self):
        tester = app.test_client(self)
        response = tester.get('/tickets')
        self.assertEqual(response.status_code, 200)
        data = eval(response.data)
        test_id = data[0]['id']
        test_phone_no = data[0]['phone_no']
        response = tester.get('/ticket/'+test_id)
        self.assertEqual(response.status_code, 200)
        data = eval(response.data)
        self.assertEqual(data['phone_no'], test_phone_no)
    
    





if __name__ == '__main__':
    unittest.main()