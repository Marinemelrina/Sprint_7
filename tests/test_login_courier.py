from const import MessageText
from helpers import *


class TestLoginCourier:
    @allure.title('Проверка на авторизацию курьера')
    def test_login_courier(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(Const.LOGIN_COURIER, data={
            "login": data[0],
            "password": data[1],
        })
        assert response.status_code == 200
        assert MessageText.LOGING_COURIER in response.text
        delete_courier(data[0], data[1])


    @allure.title('Проверка на авторизацию курьера без логина')
    def test_login_courier_without_login(self, helpers):
        data = helpers.register_new_courier_and_return_login_password()
        response = requests.post(Const.LOGIN_COURIER, data={
            "login": data[0],
            "password": '',
        })
        assert response.status_code == 400
        assert MessageText.LOGING_COURIER_WITHOUT_DATA in response.text


    @allure.title('Проверка на авторизацию курьера без пароля')
    def test_login_courier_without_password(self):
        data = register_new_courier_and_return_login_password()
        response = requests.post(Const.LOGIN_COURIER, data={
            "login": '',
            "password": data[1],
        })
        assert response.status_code == 400
        assert MessageText.LOGING_COURIER_WITHOUT_DATA in response.text


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