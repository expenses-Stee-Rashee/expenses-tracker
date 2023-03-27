import unittest
import os
import sys
from unittest.mock import patch

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from app import app

class TestNewTransaction(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

@patch('requests.post')
def test_new_transaction_success(self, mock_post):
    mock_post.return_value.ok = True
    response = self.client.post('/newtransaction', json={
        'date': '2022-03-27',
        'category': 'Food',
        'amount': 10.00,
        'note': 'Lunch'
    })
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, b'Transaction Added')



# class TestNewTransaction(unittest.TestCase):
#     def setUp(self):
#         self.client = app.test_client()

#     @patch('requests.post')
#     def test_new_transaction_success(self, mock_post):
#         mock_post.return_value.ok = True
#         response = self.client.post('/newtransaction', data={
#             'date': '2022-03-27',
#             'category': 'Food',
#             'amount': '10.00',
#             'note': 'Lunch'
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, b'Transaction Added')

#     @patch('requests.post')
#     def test_new_transaction_failure(self, mock_post):
#         mock_post.return_value.ok = False
#         response = self.client.post('/newtransaction', data={
#             'date': '2022-03-27',
#             'category': 'Food',
#             'amount': '10.00',
#             'note': 'Lunch'
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, b'Failed to add transaction')

if __name__ == '__main__':
    unittest.main()
