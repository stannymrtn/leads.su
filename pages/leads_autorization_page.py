import allure
from selene import browser, have, query
import os


class AuthenticationForm:
    with allure.step('Открытие страницы'):
        @staticmethod
        def open():
            browser.open('/login')

    with allure.step('Ввод логина и пароля'):
        @staticmethod
        def pass_enter():
            login = os.getenv('LOG')
            password = os.getenv('PASS')
            browser.element('#webmaster_models_web_LoginForm_email').type(login)
            browser.element('#webmaster_models_web_LoginForm_password').type(password)
            browser.element('[type=submit]').click()

    with allure.step('Проверка входа'):
        @staticmethod
        def check_id():
            browser.element('.home').get(query.attribute('.user-info__id'))
            browser.element('.user-info__id').should(have.text('ID 197767'))


authentication_form = AuthenticationForm()
