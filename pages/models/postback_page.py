from selene import browser, have, command
import allure


class Postback:
    @staticmethod
    def open_global_postback():
        with allure.step("Вход на страницу глобального бостбэка"):
            browser.open('/app/globalPostbacks')

    @staticmethod
    def transition_global_postback():
        with allure.step("Переход в создание глобального постбэка"):
            button = browser.element('.lds-btn_bordered')
            button.click()

    @staticmethod
    def create_global_postback():
        with allure.step("Переключение между 'Готовая ссылка' и 'Настроить вручную'"):
            browser.all('.leads-radio').element_by(have.exact_text('Готовая ссылка')).click()
            browser.all('.leads-radio').element_by(have.exact_text('Настроить вручную')).click()

        with allure.step("Вводим название постбэка"):
            browser.element('[type=text]').click().type(
                'Автотест глобал постбэк')
        with allure.step("Вводим название базовой ссылки"):
            browser.element('.lds-input-placeholder_tooltip').element('[type=text]').click().type('https://vk.com/')

        with allure.step("Выбираем 'Статус конверсии' и 'Тип события'"):
            browser.element('#conversion-status-pending').click()
            browser.element('#conversion-status-approved').click()
            browser.element('#conversion-status-rejected').click()
            browser.element('#conversion-event-created').click()
            browser.element('#conversion-event-payout-updated').click()
            browser.element('#conversion-event-updated').click()
            browser.element('#conversion-status-pending').click()
            browser.element('#conversion-status-approved').click()
            browser.element('#conversion-status-rejected').click()
            browser.element('#conversion-event-created').click()
            browser.element('#conversion-event-payout-updated').click()
            browser.element('#conversion-event-updated').click()
            browser.element('#conversion-status-pending').click()
            browser.element('#conversion-status-approved').click()
            browser.element('#conversion-status-rejected').click()
            browser.element('#conversion-event-created').click()
            browser.element('#conversion-event-payout-updated').click()
            browser.element('#conversion-event-updated').click()

        with allure.step("Выбираем HTTP-метод отправки"):
            browser.all('.leads-radio__label').element_by(have.exact_text('GET')).click()
            browser.all('.leads-radio__label').element_by(have.exact_text('POST')).click()
            browser.all('.leads-radio__label').element_by(have.exact_text('GET')).click()

        with allure.step("Добавляем группу условий"):
            browser.all('.lds-btn').element_by(have.text('+ Добавить группу условий')).click()
            browser.all('.lds-input-placeholder').element_by(have.text('Параметр')).click()
            browser.all('[role=option]').element_by(have.text('Площадка')).click()
            browser.all('.lds-input-placeholder').element_by(have.text('Условие')).click()
            browser.all('[role=option]').element_by(have.text('= Равно')).click()
            browser.element('.condition-fields').element('[type=text]').click().type('Тест')

        with allure.step("Добавляем параметры"):
            browser.element('.push-fields').perform(command.js.scroll_into_view)
            browser.all('.lds-input-placeholder').element_by(have.text('Название метки')).click()
            browser.all('[role=option]').element_by(have.text('conversion_id')).click()

        with allure.step("Проверяем итоговую ссылку"):
            browser.element('.postback-page__result').should(
                have.text('https://vk.com/?conversion_id={conversion_id}'))

    @staticmethod
    def save_global_postback():
        with allure.step("Сохраняем постбэк"):
            browser.element('.postback-page__save-button').click()


postback = Postback()