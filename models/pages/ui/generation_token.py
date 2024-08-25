import allure
from selene import browser, be, have


class Generation_token:

    with allure.step('Открытие страницы просмотра аккаунта'):
        def open_account_page(self):
            browser.open('/account/default')

    with allure.step('Нажатие кнопки "Сгенерировать токен"'):
        def press_key(self):
            browser.element('a.btn.grey.mini').click()

    with allure.step('Проверка всплывающего сообщения об успешной генерации токена'):
        def check_message(self):
            element = browser.element('div.alert.in.fade.alert-success')
            element.should(be.visible)
            element.should(have.text('Новый токен успешно сгенерирован'))


generation_token = Generation_token()
