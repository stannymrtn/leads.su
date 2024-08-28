import allure
from selene import browser, have, query
import os


class AuthenticationForm:
        @staticmethod
        def open():
            with allure.step('Открытие страницы'):
                browser.open('/login')

        @staticmethod
        def pass_enter():
            with allure.step('Ввод логина и пароля'):
                login = os.getenv('LOG')
                password = os.getenv('PASS')
                browser.element('#webmaster_models_web_LoginForm_email').type(login)
                browser.element('#webmaster_models_web_LoginForm_password').type(password)
                browser.element('[type=submit]').click()

        @staticmethod
        def check_id():
            with allure.step('Проверка входа'):
                browser.element('.home').get(query.attribute('.user-info__id'))
                browser.element('.user-info__id').should(have.text('ID 197767'))


authentication_form = AuthenticationForm()
