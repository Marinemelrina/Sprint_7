from const import MessageText
from helpers import *


class TestDeleteCourier:
    @allure.title('Удаляю курьера со всеми обязательными полями')
    def test_delete_courier(self):
        data = register_new_courier_and_return_login_password()
        response_post = requests.post(Const.LOGIN_COURIER, data={
            "login": data[0],
            "password": data[1],
        })
        id = response_post.json()['id']
        payload = {'id': id}
        response_delete = requests.delete(f'{Const.DELETE_COURIER}{id}', data=payload)
        assert response_delete.status_code == 200
        assert MessageText.DELETE_COURIER in response_delete.text


    @allure.title('Удаляю курьера без id курьера')
    def test_delete_courier_without_id(self):
        response_delete = requests.delete(Const.DELETE_COURIER)
        assert response_delete.status_code == 404
        assert MessageText.DELETE_COURIER_WITHOUT_ID in response_delete.text
        # здесь баг, ответ не совпадает со свагером


    @allure.title('Удаляю курьера с несуществующим id курьера')
    def test_delete_courier_fake_id(self):
        data = register_new_courier_and_return_login_password()
        response_post = requests.post(Const.LOGIN_COURIER, data={
            "login": data[0],
            "password": data[1],
        })
        id = response_post.json()['id']
        payload = {'id': id}
        response_delete = requests.delete(f'{Const.DELETE_COURIER}{id}1', data=payload)
        assert response_delete.status_code == 404
        assert MessageText.DELETE_COURIER_FAKE_ID in response_delete.text