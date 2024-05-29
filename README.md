***Проект 7-го спринта***
  
Перед началом работы с репозиторием выполнила команды:

1. Подключила виртуальное окружение

***python -m venv venv***
***venv\Scripts\activate***

2. Подключила pytest

***pip install pytest***

3. Подключила selenium

***pip install selenium****

4. Установила зависимости

***pip3 install -r requirements.txt***

5. Запустила все тесты из директории tests

***pytest tests --alluredir=allure_results***

6. Сформировала отчёт в формате веб версии

***allure serve allure_results***

--------------------------------------------------------------------------------------

Тесты, которые были проведены:

test_create_courier.py - создание курьера
test_login_courier.py - авторизация курьера
test_create_order.py - создание заказа
test_order_list.py - проверка полного списка заказов
test_delete_courier.py - удаление курьера