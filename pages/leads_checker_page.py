from selene import browser, be, have, by
import allure


class Checker:
    @staticmethod
    def open_checker():
        with allure.step('Открытие страницы Чекера'):
            browser.open('/app/phone-checker')

    @staticmethod
    def check_header_elements():
        with allure.step('Проверка отображения заголовка'):
            browser.element('.phone-checker-header__title').should(have.text('Checker'))
            browser.all('.phone-checker-offers__item').should(have.size(20))

    @staticmethod
    def check_block_api_integration():
        with allure.step('Проверка блока API-интеграция'):
            browser.element('#phone-checker-integration-token').should(be.not_.blank)
            browser.element('#popover-check-phones-request').should(be.not_.blank)
            browser.element('#popover-get-report-request').should(be.not_.blank)

    @staticmethod
    def check_input_fields():
        with allure.step('Ввод значений в поля'):
            browser.open('/app/phone-checker')
            browser.element(
                'div.phone-checker-entry__field div.lds-input-placeholder input.lds-input-placeholder__field').type(
                '12345678')
            browser.element('div.vs__selected-options input.vs__search').click()
            browser.element('#vs1__option-1').click()
            browser.element(
                'div.phone-checker-entry__field div.lds-input-placeholder input.lds-input-placeholder__field').click()
            browser.element('div.phone-checker-entry__field textarea.lds-input-placeholder__field').type('123')

    @staticmethod
    def check_input_buttons():
        with allure.step('Проверка работы кнопки отправки'):
            browser.element(by.text('Очистить поле')).click()
            browser.element('div.phone-checker-entry__field textarea.lds-input-placeholder__field').type('123')
            browser.element(by.text('Отправить на проверку')).click()
            browser.element('.phone-checker-history__item').should(be.not_.blank)

    @staticmethod
    def download_file():
        with allure.step('Проверка скачивания'):
            browser.element('.phone-checker-history__download').should(be.visible).click()


phone_checker = Checker()
