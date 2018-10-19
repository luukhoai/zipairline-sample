from django.test import TestCase
import json
from .models import ZipAirline, ZipAirplane


class ZipAirlineTest(TestCase):

    def setUp(self):
        self.url = '/zipairplanes/'
        self.airline = ZipAirline.objects.create(airline_name='TestAirline')

    def test_airplane_object_create(self):
        airplane = ZipAirplane.objects.create(airplane_id=1,passenger_numb=100,airline=self.airline)
        assert airplane.fuel_tank == 200

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
        data = {
            'airplane_id': '1',
            'passenger_numb': '100000',
            'airline': self.airline.id
        }
        response = self.client.post(self.url, data).json()
        assert response['non_field_errors'][0] == 'fly_time should be larger than 1.'

    def test_pass_create_airplane(self):
        data = {
            'airplane_id': '1',
            'passenger_numb': '100',
            'airline': self.airline.id
        }
        response = self.client.post(self.url, data).json()
        assert response['airplane_id'] == 1
        assert response['passenger_numb'] == 100

    def test_validation_when_one_plane_got_error(self):
        url = '/zipairlines/'
        data = {
            'airline_id': self.airline.id,
            'airline_name': 'TestAirline',
            'airplanes': [
                {'airplane_id': '-1', 'passenger_numb': '100'},
                {'airplane_id': '2', 'passenger_numb': '200'},
            ]
        }
        response = self.client.post(url, data, format='json').json()
        assert response['airplanes'][0]['airplane_id'][0] == 'airplane_id should be positive integer value.'

    def test_pass_create_airline(self):
        url = '/zipairlines/'
        data = {
            'airline_id': self.airline.id,
            'airline_name': 'TestAirline',
            'airplanes': [
                        {'airplane_id': '1', 'passenger_numb': '100'},
                        {'airplane_id': '2', 'passenger_numb': '200'},
                        {'airplane_id': '3', 'passenger_numb': '200'},
                        {'airplane_id': '4', 'passenger_numb': '200'},
                        {'airplane_id': '5', 'passenger_numb': '200'},
                        {'airplane_id': '6', 'passenger_numb': '200'},
                        {'airplane_id': '7', 'passenger_numb': '200'},
                        {'airplane_id': '8', 'passenger_numb': '200'},
                        {'airplane_id': '9', 'passenger_numb': '200'},
                        {'airplane_id': '10', 'passenger_numb': '200'},
                    ]
                }
        response = self.client.post(url, data, format='json').json()
        print(response)