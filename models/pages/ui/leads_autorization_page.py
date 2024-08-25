import allure
from selene import browser, have, query
import os


class AuthenticationForm:
    with allure.step('Открытие страницы'):
        def open(self):
            browser.open('/login')

    with allure.step('Ввод логина и пароля'):
        def logpass_enter(self):
            login = os.getenv('LOG')
            password = os.getenv('PASS')
            browser.element('#webmaster_models_web_LoginForm_email').type(login)
            browser.element('#webmaster_models_web_LoginForm_password').type(password)
            browser.element('[type=submit]').click()

    with allure.step('Проверка входа'):
        def check_id(self):
            browser.element('.home').get(query.attribute('.user-info__id'))
            browser.element('.user-info__id').should(have.text('ID 197767'))


authentication_form = AuthenticationForm()
