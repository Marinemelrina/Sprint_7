import requests

from const import MessageText
from helpers import *


class TestLoginCourier:

    @allure.title('Проверка на авторизацию курьера без логина')
    def test_login_courier_without_login(self):
        response_create = register_new_courier_and_return_login_password()
        payload = {
            "login": "",
            "password": response_create,
        }
        response_post = requests.post(f'{Const.LOGIN_COURIER}', json=payload)
        assert response_post.status_code == 400
        assert MessageText.LOGING_COURIER_WITHOUT_DATA in response_post.text


    @allure.title('Проверка на авторизацию курьера без пароля')
    def test_login_courier_without_password(self):
        response_create = register_new_courier_and_return_login_password()
        payload = {
            "login": response_create,
            "password": "",
        }
        response_post = requests.post(f'{Const.LOGIN_COURIER}', json=payload)
        assert response_post.status_code == 400
        assert MessageText.LOGING_COURIER_WITHOUT_DATA in response_post.text


    @allure.title('Проверка на авторизацию курьера без логина и пароля')
    def test_login_courier_without_data(self):
        response = requests.post(Const.LOGIN_COURIER, data={
            "login": '',
            "password": '',
        })
        assert response.status_code == 400
        assert MessageText.LOGING_COURIER_WITHOUT_DATA in response.text


    @allure.title('Проверка на авторизацию с несуществующими данными')
    def test_login_courier_fake_data(self):
        response = requests.post(Const.LOGIN_COURIER, data={
            "login": 'marina',
            "password": 'erfirfnenetopk',
        })
        assert response.status_code == 404
        assert MessageText.LOGING_COURIER_FAKE_DATA in response.text