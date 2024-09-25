import requests
from jsonschema import validate
import json
from schemas2.create_user import create_user
from schemas2.login_succesful import login_succesful
from schemas2.user_info import user_info
from schemas2.users_list import users_list

url = 'https://reqres.in'

def test_create_user_with_status_code():
    response = requests.post(url + '/api/users', json={'name': 'morpheus',
                                                      "job": "Zion president"})
    assert response.status_code == 201

def test_update_user_info_with_status_code():
    response = requests.put(url + '/api/users/2', json={'name': 'morpheus',
                                                       "job": "Zion president"})
    assert response.status_code == 200

def test_delete_user_with_status_code():
    response = requests.delete(url + '/api/users/2')
    assert response.status_code == 204

def test_unsuccesful_login_with_status_code():
    response = requests.post(url + '/api/login', json={'email': 'alex@test'})
    assert response.status_code == 400

def test_create_new_user_response_schema_with_status_code():
    response = requests.post(url + '/api/users',
                             json={'name': 'morpheus', 'job': 'Zion president'})
    body = response.json()
    assert response.status_code == 201
    validate(body, schema=create_user)

def test_unsuccesful_user_info_with_status_code():
    response = requests.get(url + '/api/users/23')
    assert response.status_code == 404

def test_login_succesful_with_schema():
    response = requests.post(url + '/api/login', json={
        'email':'eve.holt@reqres.in','password': 'cityslicka'})
    body = response.json()
    assert response.status_code == 200
    validate(body, schema=login_succesful)

def test_get_user_info_with_schema():
    response = requests.get(url + '/api/users/2')
    body = response.json()
    validate(body, schema=user_info)

def test_get_users_list_with_schema():
    response = requests.get(url +'/api/users', params={'page': 2})
    body = response.json()
    validate(body, schema=users_list)

def test_create_user_with_information_with_status_code():
    name = 'Alex'
    job = 'President'
    response = requests.post(url + '/api/users', json={'name': 'Alex',
                                                       'job': 'President'})
    body = response.json()
    assert response.status_code == 201
    assert body.get('name') == name
    assert body.get('job') == job


