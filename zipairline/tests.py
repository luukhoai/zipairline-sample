from django.test import TestCase


class ZipAirlineTest(TestCase):

    def setUp(self):
        self.url = '/zipairlines/'

    def test_zipairline_id_is_not_positive(self):
        data = {
            'zipairline_id': '-1',
            'passenger_numb': '100'
        }
        response = self.client.post(self.url, data).json()
        assert response['zipairline_id'][0] == 'zipairline_id should be positive integer value.'

    def test_passenger_numb_is_not_positive(self):
        data = {
            'zipairline_id': '1',
            'passenger_numb': '-100'
        }
        response = self.client.post(self.url, data).json()
        assert response['passenger_numb'][0] == 'passenger_numb shoud be positive integer value.'

    def test_fly_time_is_not_positive(self):
        data = {
            'zipairline_id': '1',
            'passenger_numb': '100000'
        }
        response = self.client.post(self.url, data).json()
        assert response['non_field_errors'][0] == 'fly_time should be larger than 1.'

    def test_pass_value(self):
        data = {
            'zipairline_id': '1',
            'passenger_numb': '100'
        }
        response = self.client.post(self.url, data).json()
        assert response['zipairline_id'] == 1
        assert response['passenger_numb'] == 100