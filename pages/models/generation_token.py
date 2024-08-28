import allure
from selene import browser, be, have


class GenerationToken:

        def open_account_page(self):
            with allure.step('Открытие страницы просмотра аккаунта'):
                browser.open('/account/default')


        def press_key(self):
            with allure.step('Нажатие кнопки "Сгенерировать токен"'):
                browser.element('a.btn.grey.mini').click()

        def check_message(self):
            with allure.step('Проверка всплывающего сообщения об успешной генерации токена'):
                element = browser.element('div.alert.in.fade.alert-success')
                element.should(be.visible)
                element.should(have.text('Новый токен успешно сгенерирован'))


generation_token = GenerationToken()
