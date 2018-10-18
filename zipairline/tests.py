from django.test import TestCase
from .models import ZipAirline


class ZipAirlineTest(TestCase):

    def setUp(self):
        self.url = '/zipairplanes/'

    def test_airplane_id_is_not_positive(self):
        data = {
            'airplane_id': '-1',
            'passenger_numb': '100',
        }
        response = self.client.post(self.url, data).json()
        assert response['airplane_id'][0] == 'airplane_id should be positive integer value.'

    def test_passenger_numb_is_not_positive(self):
        data = {
            'airplane_id': '1',
            'passenger_numb': '-100'
        }
        response = self.client.post(self.url, data).json()
        assert response['passenger_numb'][0] == 'passenger_numb shoud be positive integer value.'

    def test_fly_time_is_not_positive(self):
        airline = ZipAirline.objects.create(airline_name='AirlineTest')
        data = {
            'airplane_id': '1',
            'passenger_numb': '100000',
            'airline': airline.id
        }
        response = self.client.post(self.url, data).json()
        assert response['non_field_errors'][0] == 'fly_time should be larger than 1.'

    def test_pass_value(self):
        airline = ZipAirline.objects.create(airline_name='AirlineTest')
        data = {
            'airplane_id': '1',
            'passenger_numb': '100',
            'airline': airline.id
        }
        response = self.client.post(self.url, data).json()
        assert response['airplane_id'] == 1
        assert response['passenger_numb'] == 100

    # def test_airlines_pass(self):
    #     url = '/zipairlines/'
    #     data = {'airplanes': [
    #                     {'airplane_id': '1', 'passenger_numb': '100'}
    #                 ]
    #             }
    #     response = self.client.post(url, data).json()
    #     print(response)